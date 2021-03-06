import media
import urllib.request
import json
import logging
import os
LOG_FILENAME = os.path.abspath("mylog.log")
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
if logger.handlers:
    logger.handlers = []
fh = logging.FileHandler(LOG_FILENAME)
logger.addHandler(fh)
logger.propagate = False
API_KEY = "d094aee99018937c03e6d492ebb80d11"


class entertainment_center(object):

    def getmovies(self):
        movie1 = media.Movie("Interstellar", "http://image.tmdb.org/t/p/w185//nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg",
                             "https://www.youtube.com/watch?v=Rt2LHkSwdPQ")
        movie2 = media.Movie("Beauty and the Beast", "http://image.tmdb.org/t/p/w185/2HjngGzVK3NTzptEtsT8E0Hi3ZB.jpg",
                             "https://www.youtube.com/watch?v=tWapqpCEO7Y")
        movie3 = media.Movie("Guardians of the Galaxy -2", "http://image.tmdb.org/t/p/w185/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg",
                             "https://www.youtube.com/watch?v=wUn05hdkhjM")
        movie4 = media.Movie("Alien:Covenant", "http://image.tmdb.org/t/p/w185/ewVHnq4lUiovxBCu64qxq5bT2lu.jpg",
                             "https://www.youtube.com/watch?v=H0VW6sg50Pk")
        movie5 = media.Movie("The Fate of the Furious", "http://image.tmdb.org/t/p/w185/iNpz2DgTsTMPaDRZq2tnbqjL2vF.jpg",
                             "https://www.youtube.com/watch?v=vve9TtFg9wM")
        movie6 = media.Movie("Logan", "http://image.tmdb.org/t/p/w185/45Y1G5FEgttPAwjTYic6czC9xCn.jpg",
                             "https://www.youtube.com/watch?v=XaE_9pfybL4")
        movie7 = media.Movie("Pirates of the Caribbean", "http://image.tmdb.org/t/p/w185/tkt9xR1kNX5R9rCebASKck44si2.jpg",
                             "https://www.youtube.com/watch?v=naQr0uTrH_s")
        movie8 = media.Movie("Sing", "http://image.tmdb.org/t/p/w185/eSVtBB2PVFbQiFWC7CQi3EjIZnn.jpg",
                             "https://www.youtube.com/watch?v=Zvjmt4pwtdg")
        movieList = [movie1, movie2, movie3,
                     movie4, movie5, movie6, movie7, movie8]
        return movieList

    def getMoviesFromAPI(self, pageNumber):
        # gets the most popular movies from the api.
        url = "http://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=" + \
            API_KEY + "&page=" + pageNumber
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode('utf-8'))['results']
     #   logger.debug(result)
        movieList = []
        for temp in result:
            vidUrl = "http://api.themoviedb.org/3/movie/" + \
                str(temp['id']) + \
                "/videos?api_key=d094aee99018937c03e6d492ebb80d11"
            vidReq = urllib.request.Request(vidUrl)
            vidResponse = urllib.request.urlopen(vidReq)
            vidResult = json.loads(
                vidResponse.read().decode('utf-8'))['results'][0]
       #     logger.debug(vidResult)
            movie = media.Movie(temp['title'], "http://image.tmdb.org/t/p/w185" + temp[
                                'poster_path'], "https://www.youtube.com/watch?v=" + vidResult['key'])
            movieList.append(movie)
            logger.debug("movie: " + movie.title + " poster: " +
                         movie.poster_image_url + " youtubeUrl: " + movie.trailer_youtube_url)
        return movieList
