# create a movie object with title of the movie.
class Movie:

    def __init__ (self, title, year):
        self.title = title
        if year == None:
            self.year = -1
        self.year = year

    def print_movie_info(self):
        print("Movie Title:" + self.title)
        print("Movie Release: " + str(self.year))

    def search_string(self):
        if self.year != -1:
            return (str(self.title +
            " (" + str(self.year)) + ")")
        else:
            return self.title
