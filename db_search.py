# used tmdbsimple wrapper created by celiao.
# https://github.com/celiao/tmdbsimple/

import tmdbsimple as tmdb
import movie

tmdb.API_KEY = 'e9316003ecb292af5e895d5c58f36f4e'

def search_for_movie(mov_obj):
    # create search_obj
    search = tmdb.Search()
    response = search.movie(query=mov_obj.get_title())
    counter = 1

    if int(response['total_results']) >= 1 and mov_obj.get_year() == -1:
        print(response['total_results'], " total search results. Listing...")
        for results in search.results:
            print("[" + str(counter) + "] ", results['title'], results['release_date'])
            counter += 1

    elif int(response['total_results']) >= 1:
        for results in search.results:
            if str(mov_obj.get_year()) in results['release_date']:
                print("Best match found: ", results['title'], results['release_date'])
                break
