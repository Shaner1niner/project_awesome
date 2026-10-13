# Provenance and certificate link adaptations

The three published certificate documents are **link-adjusted copies**, not verbatim reprints of the private-repository originals. Their mathematical content and original numeric tables are retained. All original code/verifier sources referred to below remain outside this narrow supplement.

| Certificate | Original Git blob SHA-1 | Public-copy Git blob SHA-1 |
| --- | --- | --- |
| `EVENT_BRANCH_CERTIFICATE.md` | `199d14ec24b436dbcdbeba1e34392f39ebf06822` | `b7a045c8e2d427383c7cc26481ab0712de536e34` |
| `FAILURE_WORDS_CERTIFICATE.md` | `e6509d1b09e39efa7eeb0a0b1c1d47da17384d58` | `5b04e996aa1f2fccc34c2dabb267d4a124662e62` |
| `V02_KERNEL_AND_STATEWISE_AUDIT.md` | `6262276e6dabe615762c9ef5101786a3df802a52` | `2402710d4304fc694f9e1ba253e9536008050f3f` |

For exact SHA256 byte digests and source/copy line counts, see [`PROVENANCE_SOURCE_AND_PUBLIC_COPY_HASHES.json`](PROVENANCE_SOURCE_AND_PUBLIC_COPY_HASHES.json).

## Changes to the public-reading copies

- **Event-order certificate:** Label the original `verify_eventword_p5.py` verifier as omitted; link to the *different* bundled root-band verifier; clarify the latter does not reproduce every assertion of the original program.
- **Failure-word certificate:** Clarify the original event-word source is omitted; link the separate bundled full-family checker without implying program identity; remove the broken private issue link; distinguish unavailable original output-replay commands from the packaged `run_checks.py` commands.
- **V0.2 statewise/kernel audit:** Replace the unavailable original V0.2 script link with an explicit omitted-source notice and a link to the distinct bundled checker.
- Each adapted document carries a top-of-file declaration of its source Git blob identity. **All 15 failure-word rows and all 14 event-band rows are numerically unchanged.**

The reader-facing package deliberately does not include private referee correspondence, original owner verifier source, private issue/commit link targets, third-party data, or any proof of publication priority. The three bundled checkers are **assistant-origin, code-independent implementations**; their correctness has not been certified by a separate-person human referee. The public release makes no claim that the complete private-repository verification process is reproduced by these three scripts alone.
