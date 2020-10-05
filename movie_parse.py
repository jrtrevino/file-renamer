import os
import sys
import movie
import re

def find_title(file_array):
    filename = ""
    year = -1
    for element in file_array:
        # check if number in filename is the year
        if element.isnumeric():
            num = int(element)
            if (num > 1940 and num < 2030):
                year = num
                break
        else:
            filename += element
            filename += " "
    if year != -1 and len(filename) > 0:
        return movie.Movie(filename, year)
    return movie.Movie(filename, None)

# returns an array with elements consisting of the file information/
def split_file (filename):
    # check for spaces or periods.
    split_name = filename.replace('.', " ")
    split_name = split_name.split(" ")

    return split_name

def parse_movie(path):
    filename = os.path.basename(path)
    temp = split_file(filename)
    movie1 = find_title(temp)
    print(movie1.search_string())


def check_arg():
    num_files = len(sys.argv)
    if num_files == 1:
        print("Usage: movie_parse.py <inputfile> ...")
        return -1
    for id in range(1, num_files):
        parse_movie(sys.argv[id])
    return 0

if __name__ == '__main__':
    check_arg()
