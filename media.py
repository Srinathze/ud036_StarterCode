import logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
if logger.handlers:
    logger.handlers = []
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False

class Movie(object):
    title = ""
    poster_image_url = ""
    trailer_youtube_url = ""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

