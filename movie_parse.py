import os
import sys
import movie
import re

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
def find_title(file_array):
    title_found = False
    filename = []
    file_info = {
        'title' : "",
        'year' : -1,
        'quality' : "",
        'codec' : "",
        'source' : ""}
    # cycle through filename and match informaiton.
    for element in file_array:
        # check if number in filename is the year
        if (find_year(file_info, element)) == 1:
            title_found = True # big assumption...
            continue
        elif find_quality(file_info, element) == 1:
            title_found = True # big assumption...
            continue
        elif find_codec(file_info, element) == 1:
            title_found = True # big assumption...
            continue

        elif find_source(file_info, element) == 1:
            title_found = True # big assumption...
            continue

        else:
            if title_found == False:
                filename.append(element)
    final_name = " ".join(filename)

    file_info["title"] = final_name
    return file_info

# returns an array with elements consisting of the file information/
def split_file (filename):
    # check for spaces or periods.
    split_name = filename.replace('.', " ")
    new_split = split_name.replace('-', " ")
    split_name = new_split.split(" ")
    return split_name


# begins the process to parse movie information from a filename.
def parse_movie(path):
    # save directory information for renaming purposes.
    extension = "." + os.path.splitext(path)[1][1:]
    filename = os.path.basename(path)
    dir = os.path.dirname(path) + "/"
    # begin parsing!
    temp = split_file(filename)
    movie_info_array = find_title(temp)
    mov_obj = create_movie_object(movie_info_array)
    final_path = dir + mov_obj.search_string() + extension
    # rename!
    os.rename(path, final_path)
    #print(mov_obj.search_string())
    # print(path, os.path.dirname(path))
    return mov_obj

# ensures the user inputted at least 1 file to be parsed.
def check_arg():
    num_files = len(sys.argv)
    if num_files == 1:
        print("Usage: movie_parse.py <inputfile> ...")
        return -1
    for id in range(1, num_files):
        new_name = parse_movie(sys.argv[id])
    return 0

if __name__ == '__main__':
    check_arg()
