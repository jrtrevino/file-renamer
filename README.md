# FileRenamer

FileRenamer is a simple python3 program to parse movie files into a readable format. It is currently in development with hopes of supporting TV show parsing.

Usage: 

```
python3 movie_parse.py filename-a filename-b filename-c ...
```
## TMDB API
To further enhance results, a query is sent to the TMDB API. This allows the user to select which movie to rename the file to in cases where parsing wasn't successful. To use this feature, please provide a TMDB API Key which can be obtained here:

https://www.themoviedb.org/documentation/api

## Examples

```
>> python3 movie_parse The.Lost.Pyramids.Of.China.2020.1080p.mp4
The Lost Pyramids of China (2020).mp4

```
If a video file has the title "The.Lost.Pyramids.Of.China.2020.1080p", FileRenamer will rename the file as "The Lost Pyramids Of China (2020)." Additionally, a movie object is created that has information regarding the title and year in case a user wants that functionality.

In cases where the movie title is ambiguous (namely, no year was found in the title), a search to the TMDB API is made to help determine the correct name of the movie. For example, the Movie 'The Matrix', is ambiguous because there are many potential choices of what to rename the file to. In this case, the program prints out the following output:

```
>> python3 movie_parse The.Matrix.mp4 

42  total search results. Listing Titles...
[0] The Matrix 1999-03-30
[1] The Matrix Resurrections 2021-12-15
[2] The Matrix Reloaded 2003-05-15
[3] The Matrix Revolutions 2003-11-05
[4] The Matrix Revisited 2001-11-19
[5] The Matrix Recalibrated 2004-04-06
[6] The Matrix Reloaded Revisited 2004-12-07
[7] The Matrix Reloaded: Pre-Load 2003-10-14
[8] The Matrix: What Is Bullet-Time? 1999-09-21
[9] Making 'Enter the Matrix' 2003-10-14
[10] A Glitch in the Matrix 2021-02-05
[11] The Matrix Revolutions Revisited 2004-12-07
[12] Making 'The Matrix' 1999-09-21
[13] The Matrix Reloaded: Car Chase 2004-12-07
[14] The Roots of the Matrix 2004-12-07
[15] The Matrix: What Is the Concept? 1999-09-21
[16] A Glitch in the Matrix 2018-02-17
[17] The Matrix Revolutions: Neo Realism - Evolution of Bullet Time 2004-04-06
[18] Sex and the Matrix 2000-01-01
[19] Cable Two's The Matrix 

Please enter the number of the movie to rename the file to. Or -1 to cancel.
>> 0

Renamed file to: The Matrix (1999).mp4
```

The user will then select the appropriate name of the movie to rename the file to.
