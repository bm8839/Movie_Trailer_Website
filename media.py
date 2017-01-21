import webbrowser


class Movie():
    """ Classes are like blueprints that describe certain features or
    contain information or data about the objects in that class. The
    objects in this class are movie title, release date, star,
    storyline, poster image, and youtube trailer.
    """

    def __init__(self, movie_title, release_date, movie_stars, movie_storyline,
                 poster_image, trailer_youtube):
        """ This function is a constructor. It intializes or creates
        space in memory for a new instance of Movie which contains the
        title, release date, star, storyline, poster image, and youtube
        trailer.
        """
        self.title = movie_title
        self.release_date = release_date
        self.movie_stars = movie_stars
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
