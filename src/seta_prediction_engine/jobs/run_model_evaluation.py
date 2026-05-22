"""Run first-pass sklearn model evaluation against SETA feature frames."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd

from seta_prediction_engine.backtesting.model_evaluate import evaluate_models_walk_forward
from seta_prediction_engine.config import load_config
from seta_prediction_engine.features.catalog import load_feature_catalog
from seta_prediction_engine.features.frame import build_feature_frame, summarize_feature_frame
from seta_prediction_engine.jobs.run_baseline_evaluation import load_source
from seta_prediction_engine.models.sklearn_classifiers import (
    RESEARCH_CHALLENGER_MODEL_NAMES,
    SKLEARN_MODEL_NAMES,
)
from seta_prediction_engine.reporting.asset_universe import (
    build_asset_universe_report,
    summarize_asset_universe,
)


def _safe_suffix(value: str | None) -> str:
    if not value:
        return ""
    cleaned = re.sub(r"[^A-Za-z0-9_]+", "_", str(value).strip())
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned


def _resolve_model_names(model_set: str, explicit_models: list[str] | None) -> list[str]:
    """Resolve the model list for an evaluation run.

    Production/default runs intentionally use the stable public-card candidate
    list. Research runs explicitly expand the candidate surface with conservative
    hyperparameter variants. Passing --models still wins for one-off experiments.
    """
    if explicit_models:
        return explicit_models
    if model_set == "research":
        return RESEARCH_CHALLENGER_MODEL_NAMES
    return SKLEARN_MODEL_NAMES


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run SETA sklearn walk-forward model evaluation.")
    parser.add_argument("--catalog", default="configs/feature_catalog_v0_1.csv")
    parser.add_argument("--profile", default="baseline_v0_1")
    parser.add_argument("--source", default=None)
    parser.add_argument("--input-csv", default=None)
    parser.add_argument("--env-file", default=None)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--train-window", type=int, default=40)
    parser.add_argument("--test-window", type=int, default=5)
    parser.add_argument("--step-size", type=int, default=None)
    parser.add_argument("--split-mode", choices=["global", "grouped"], default="grouped")
    parser.add_argument("--group-column", default="term")
    parser.add_argument(
        "--model-set",
        choices=["production", "research"],
        default="production",
        help=(
            "Named model set to evaluate when --models is not supplied. Production keeps "
            "the stable public-card candidate set; research adds conservative challenger "
            "hyperparameter variants."
        ),
    )
    parser.add_argument("--models", nargs="+", default=None)
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument("--output-dir", default="artifacts/model_evaluation")
    parser.add_argument(
        "--artifact-suffix",
        default=None,
        help=(
            "Optional extra suffix for output artifacts, useful for asset-class or research "
            "runs that would otherwise overwrite the same profile/split files."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(env_file=args.env_file)
    catalog = load_feature_catalog(args.catalog)
    source_df, source_label = load_source(args)
    model_names = _resolve_model_names(args.model_set, args.models)

    feature_frame = build_feature_frame(
        source_df=source_df,
        catalog_df=catalog,
        profile=args.profile,
        target_column=config.target_column,
        include_target=True,
        dropna_target=True,
    )

    result = evaluate_models_walk_forward(
        source_df=source_df,
        feature_frame=feature_frame,
        train_window=args.train_window,
        test_window=args.test_window,
        step_size=args.step_size,
        split_mode=args.split_mode,
        group_column=args.group_column,
        model_names=model_names,
        random_state=args.random_state,
    )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix_parts = [args.profile, args.split_mode]
    artifact_suffix = _safe_suffix(args.artifact_suffix)
    if artifact_suffix:
        suffix_parts.append(artifact_suffix)
    suffix = "_".join(suffix_parts)
    metrics_path = output_dir / f"model_metrics_{suffix}.csv"
    predictions_path = output_dir / f"model_predictions_{suffix}.csv"
    summary_path = output_dir / f"feature_frame_summary_{suffix}.json"
    asset_universe_path = output_dir / f"asset_universe_{suffix}.csv"

    result.metrics.to_csv(metrics_path, index=False)
    result.predictions.to_csv(predictions_path, index=False)
    feature_summary = summarize_feature_frame(feature_frame)

    asset_universe = build_asset_universe_report(
        source_df=source_df.loc[feature_frame.X.index].copy(),
        predictions=result.predictions,
        group_column=args.group_column,
        date_column="date",
        target_column=config.target_column,
        train_window=args.train_window,
        test_window=args.test_window,
    )
    asset_summary = summarize_asset_universe(asset_universe)
    feature_summary.update(asset_summary)
    if artifact_suffix:
        feature_summary["artifact_suffix"] = artifact_suffix
    feature_summary["model_set"] = args.model_set
    feature_summary["model_count"] = len(model_names)

    pd.Series(feature_summary).to_json(summary_path, indent=2)
    asset_universe.to_csv(asset_universe_path, index=False)

    print(f"source={source_label}")
    print(f"profile={args.profile}")
    print(f"split_mode={args.split_mode}")
    print(f"model_set={args.model_set}")
    print(f"model_count={len(model_names)}")
    print(f"models={','.join(model_names)}")
    print(f"artifact_suffix={artifact_suffix or None}")
    print(f"group_column={args.group_column if args.split_mode == 'grouped' else None}")
    print(f"train_window={args.train_window}")
    print(f"test_window={args.test_window}")
    print(f"splits={result.split_count}")
    print(f"asset_count={asset_summary['asset_count']}")
    print(f"eligible_asset_count={asset_summary['eligible_asset_count']}")
    print(f"latest_predicted_asset_count={asset_summary['latest_predicted_asset_count']}")
    print(f"insufficient_history_asset_count={asset_summary['insufficient_history_asset_count']}")
    print(f"metrics={metrics_path}")
    print(f"predictions={predictions_path}")
    print(f"feature_summary={summary_path}")
    print(f"asset_universe={asset_universe_path}")
    print(result.metrics.groupby("model")["accuracy"].mean().sort_values(ascending=False))


if __name__ == "__main__":
    main()
