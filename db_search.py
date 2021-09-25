# used tmdbsimple wrapper created by celiao.
# https://github.com/celiao/tmdbsimple/
import movie
import secrets
import sys

try:
    import tmdbsimple as tmdb
except ImportError as e:
    print("Import Missing: {}".format(e))
    sys.exit(-1)

tmdb.API_KEY = secrets.get_api_key()


def search_for_movie(mov_obj):
    search = tmdb.Search()
    counter = 0
    new_title = None
    response = search.movie(query=mov_obj.get_title())
    # print(response)
    # show all results because we are unsure of the movie's year from parsing
    if response['total_results'] >= 1 and mov_obj.get_year() == -1:
        print(response['total_results'],
              " total search results. Listing Titles...")
        for results in search.results:
            print("[{}]".format(counter),
                  results['title'], results['release_date'])
            counter += 1
        try:
            movie_val = int(input(
                '\nPlease enter the number of the movie to rename the file to. Or -1 to cancel.\n'))
            if movie_val >= 0 and movie_val <= counter:
                results = search.results[movie_val]
                print("Renaming movie to: {} ({})".format(
                    results['title'], results['release_date'][:4]))
                new_title = "{} ({})".format(
                    results['title'], results['release_date'][:4])
            elif movie_val == -1:
                print("Canceling.")
            else:
                print(
                    "Sorry, please enter a valid number between 0 and {}".format(counter))
        except Exception as e:
            print(e)
            print("Sorry, we couldn't rename the file using the API query. Try again.")

    elif int(response['total_results']) >= 1:
        for results in search.results:
            if str(mov_obj.get_year()) in results['release_date']:
                print("Match Found. Title: {}, Year: {}".format(
                    results['title'], results['release_date'][:4]))
                new_title = "{} ({})".format(
                    results['title'], results['release_date'][:4])
                break
    if new_title:
        return new_title
    else:
        return None
