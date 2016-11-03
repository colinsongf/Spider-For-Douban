from datetime import datetime


from typing import TypeVar

TypeStr = TypeVar(str, None)

class Movie(object):
    """Movie Model Class"""

    def __init__(self, title: TypeStr, score: int=0, comment: str=None, date:datetime=None, uri:str=None,
                 poster_uri:str=None):
        """ Initialize a Movie object

        :param title:       Movie title.
        :param score:       Score (0 ~ 100) of movie.
        :param comment:     Movie comment.
        :param date:        Date of the movie user watched.
        :param uri:         Douban movie link of the movie.
        :param poster_uri:  Douban movie's poster link of the movie.
        """
        if title is None:
            pass