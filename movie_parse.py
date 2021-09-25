import os
import sys
import movie
import db_search
import re

# top level function to begin parsing process.


def begin_program():
    num_files = len(sys.argv)
    for id in range(1, num_files):
        new_name = parse_movie(sys.argv[id])

# begins the process to parse movie information from a filename.


def parse_movie(path):
    # check for file existance.
    if not (check_path_existance(path)):
        return -1
    # begin parsing!
    filename = os.path.basename(path)
    temp = split_file(filename)
    movie_info_array = find_movie_info(temp)
    mov_obj = create_movie_object(movie_info_array)
    rename_movie(path, mov_obj)
    return mov_obj

# returns a movie object containing information found from parsing.


def create_movie_object(info_arr):
    temp_movie_obj = movie.Movie(info_arr["title"], info_arr["year"])
    temp_movie_obj.add_codec(info_arr["codec"])
    temp_movie_obj.add_quality(info_arr["quality"])
    temp_movie_obj.add_source(info_arr["source"])
    return temp_movie_obj

# determines if current word in filename is considered a valid year.


def find_year(dict, word):
    return_val = -1
    # remove possible parenthesis from year
    new_word = word.replace("(", "")
    newer_word = new_word.replace(")", "")
    if newer_word.isnumeric():
        num = int(newer_word)
        if (num > 1940 and num < 2030):
            year = num
            return_val = 1
            dict["year"] = year
    return return_val

# determines if current word in filename is a valid resolution.


def find_quality(dict, word):
    if (word.lower() == "480p" or word.lower() == "720p" or
            word.lower() == "1080p" or word.lower() == "2160p"):
        dict["quality"] = word
        return 1
    return -1

# determines if current word in filename is a valid video codec.


def find_codec(dict, word):
    if (word.casefold() == "x264" or word.casefold() == "x265"
            or "hevc" in word.casefold() or "xvid" in word.casefold()):
        dict["codec"] = word
        return 1
    return -1

# attempts to determines the source of a video based off of keywords.


def find_source(dict, word):
    if ("bluray" in word.casefold() or "dvdrip" in word.casefold()
            or "hdtv" in word.casefold()):
        dict["source"] = word
        return 1
    return -1

# attempts to find the movie title through parsing.


def find_movie_info(file_array):
    title_found = False
    filename = []
    file_info = {
        'title': "",
        'year': -1,
        'quality': "",
        'codec': "",
        'source': ""}
    # cycle through filename and match informaiton.
    for element in file_array:
        # check if number in filename is the year
        if (find_year(file_info, element)) == 1:
            title_found = True  # big assumption...
            continue
        elif find_quality(file_info, element) == 1:
            title_found = True  # big assumption...
            continue
        elif find_codec(file_info, element) == 1:
            title_found = True  # big assumption...
            continue

        elif find_source(file_info, element) == 1:
            title_found = True  # big assumption...
            continue

        else:
            if title_found == False:
                filename.append(element)
    final_name = " ".join(filename)

    file_info["title"] = final_name
    return file_info

# returns an array with elements consisting of the file information/


def split_file(filename):
    # check for spaces or periods.
    split_name = filename.replace('.', " ")
    new_split = split_name.replace('-', " ")
    split_name = new_split.split(" ")
    return split_name

# creates path for movie and renames old file.


def rename_movie(path, movie):
    # find path directory and extension to properly name.
    extension = "." + os.path.splitext(path)[1][1:]
    dir = os.path.dirname(path) + "/"
    # we will ping themoviedb.org to get the movie title from parsed
    # info from the given file.
    api_name = db_search.search_for_movie(movie)
    print("Result from api: {}".format(api_name))
    if api_name:
        final_name = dir + api_name + extension
    else:
        final_name = dir + movie.search_string() + extension
    os.rename(path, final_name)

# checks if file exists. If not, next file (if any) begin parsing.


def check_path_existance(path_to_file):
    if(os.path.exists(path_to_file)):
        return True
    else:
        (print("movie_parse: File does not exist: "
               + str(path_to_file)))
        return False

# ensures the user inputted at least 1 file to be parsed.


def check_arg():
    num_files = len(sys.argv)
    if num_files == 1:
        print("Usage: movie_parse.py <fileA> <fileB> ...")
        return 0
    return num_files


if __name__ == '__main__':
    if (check_arg()):
        begin_program()
    else:
        sys.exit(-1)
