/*
    Name: Shane Corrie
    DTSC660: Data and Database Management with SQL
    Assignment 6
*/

--------------------------------------------------------------------------------
/*				                   Part 1   		  		                  */
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				    Chosen Data Set and Reason for Selecting		          */
--------------------------------------------------------------------------------

  /*NETLIX: I chose the netflix data set because I thought it was potentially the most interesting, I wanted to group on director and see if I might find a movie by one of my favorite directors that I haven't seen yet. While doing that, I was surprised to see Clint Eastwood among the most prolific directors having directed 7 movies. The data would have been hugely more interesting if it included a times viewed or some other viewer ranking data imo.
  
  A review of the data beforehand led me to be confident that I could satisfy the requirements with the Netflix data. The most difficult part for me was trying to find out where to "Group similar values" in Q# but eventually I noticed that West Germany was needlessly separated from Germany and as a result, I could re-group it*/

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                 Select Statement      		  		          */
--------------------------------------------------------------------------------

SELECT show_id, title, director FROM netflix
WHERE director = 'Not Given';

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                   Backup Table     		  		          */
--------------------------------------------------------------------------------

CREATE TABLE netflix_backup AS SELECT * 
FROM netflix;

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                 Duplicate Column      		  		          */
--------------------------------------------------------------------------------

ALTER TABLE netflix ADD COLUMN type_duplicate text;

UPDATE netflix SET type_duplicate = type;

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                   PART 2           		  		          */
--------------------------------------------------------------------------------
-- For each question 1-4, you must include the following:
	-- One single SELECT query demonstrating the data needing cleaning.
	-- The query that performs the update to the table.
	-- A query validating the change.
	-- A comment detailing your rationale. 
--------------------------------------------------------------------------------
/*				                 Question 1     		        		      */
--------------------------------------------------------------------------------

-- One single SELECT query demonstrating the data needing cleaning.
SELECT director, count(director)
FROM netflix
GROUP BY director
ORDER BY count(director) DESC;
-- The query that performs the update to the table.
UPDATE netflix
SET director = NULL
WHERE director = 'Not Given';
-- A query validating the change.
SELECT director, count(director)
FROM netflix
GROUP BY director
ORDER BY count(director) DESC;
-- A comment detailing your rationale.
/* The data is good in that director was consistently labeled as 'Not Given', still, NULL is more appropriate */
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                 Question 2     		        		      */
--------------------------------------------------------------------------------

-- One single SELECT query demonstrating the data needing cleaning.
SELECT rating, count(rating) FROM netflix
GROUP BY rating;
-- The query that performs the update to the table.
DELETE FROM netflix
WHERE rating = 'UR';
-- A query validating the change.
SELECT rating, count(rating) FROM netflix
GROUP BY rating;
-- A comment detailing your rationale. 
/*I removed 3 rows with values of UR from the rating column. My initial thought was that UR would stand for unrated but since there is a NR for not rated, it was not clear what UR was intended to mean. Since there were only 3 movies rated as UR, I felt the loss of three rows was not a big deal*/
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                 Question 3     		        		      */
--------------------------------------------------------------------------------

-- One single SELECT query demonstrating the data needing cleaning.
SELECT country, COUNT(country) FROM netflix
GROUP BY country
ORDER BY country DESC;
-- The query that performs the update to the table.
UPDATE netflix
SET country = 'Germany'
WHERE country = 'West Germany';
-- A query validating the change.
SELECT country, COUNT(country) FROM netflix
GROUP BY country
ORDER BY country DESC;
-- A comment detailing your rationale. 
/*Grouping the similar values (West Germany and Germany) to make the data correct and consistent. In this case the movie was filmed in 1977 prior to the reunification of Germany in 1990, the distinction is no longer relevant*/

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
/*				                 Question 4     		        		      */
--------------------------------------------------------------------------------

-- One single SELECT query demonstrating the data needing cleaning.
SELECT type, duration FROM netflix;
-- The query that performs the update to the table.

/*to add the column used to separate durations of shows from durations of movies. Because movie durations are listed in minutes and show duration is given in number of seasons*/

ALTER TABLE netflix ADD COLUMN show_duration VARCHAR(12);

--to bring over all durations into the show_duration column
UPDATE netflix 
SET show_duration = duration
WHERE type = 'TV Show';

--to set Movie durations to null within the show_duration column
UPDATE netflix
SET show_duration = NULL 
WHERE type = 'Movie';

--To rename the column to include only the duration where type is Movie
ALTER TABLE netflix
RENAME COLUMN duration TO movie_duration;


--to set NULL the TV Show durations remaining in the movie_duration column 
UPDATE netflix
SET movie_duration = NULL 
WHERE type = 'TV Show'; 

-- A query validating the change.
SELECT type, title, show_duration, movie_duration FROM netflix;

-- A comment detailing your rationale. 
/*It is not optimal to have 2 different rates of measure in the same column (e.g. miles & kilometers), in this case separating total minutes for a movie and # of seasons for a show allows us to analyze the duration column for movies and shows using math and aggregates*/

--------------------------------------------------------------------------------
