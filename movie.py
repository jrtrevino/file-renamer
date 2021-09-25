# create a movie object containing information regarding the movie.
class Movie:

    title = ""
    year = -1
    codec = ""  # Xvid, h264, h265, etc.
    quality = ""  # 720p, 1080p, 2160p, etc.
    uploader = ""  # name of the file uploader
    source = ""  # dvdRip, blurayRip, HDTV, etc.

    def __init__(self, title, year):
        self.title = title
        if year == None:
            self.year = -1
        self.year = year

    def print_movie_info(self):
        print("Movie Title:" + self.title)
        print("Movie Release: " + str(self.year))

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    # returns the string used to search for a movie in a database.
    def search_string(self):
        if self.year != -1:
            return (str(self.title +
                        " (" + str(self.year)) + ")")
        else:
            return self.title

    def set_title(self, title):
        self.title = title

    def add_codec(self, codec_type):
        self.codec = codec_type

    def add_source(self, source_format):
        self.source = source_format

    def add_quality(self, quality):
        self.quality = quality
