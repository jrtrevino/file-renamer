FileRenamer is a simple python3 program to parse movie files into a readable format. It is currently in development with hopes of supporting TV show parsing.

Usage: python3 movie_parse.py filename-a filename-b filename-c ...

In the future, a ping to a movie/tv database website will help enhace the renaming process if information cannot be found.

Examples:

If a video file has the title "The Lost Pyramids Of China 2020 1080p", FileRenamer will rename the file as "The Lost Pyramids Of China (2020)." Additionally, a movie object is created that has information regarding the title.

Notes:

This program will only rename. In the future, I hope the add the ability to ping a movie database to return a movie result based off of the title. This is to help parsing when there is no instance of a year in the movie title.

Thus, a movie title named "John.Wick.3.Parabellum" will simply rename the file to "John Wick 3 Parabellum". I hope by allowing a future database ping, it will be able to rename the file to John Wick 3 Parabellum (2019)", by parsing the database result for a release-date.
