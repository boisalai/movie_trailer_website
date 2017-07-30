import webbrowser

class Movie():
    """ This class provides a way to store movie related information.

    This class was adapted from the course "Full Stack Web Developer"
    by Alain Boisvert on Sunday 30 July 2017.
    
    Attributes:
        movie_title: Title of the movie.
        movie_storyline: Storyline of the movie.
        poster_image: Poster URL of the movie from the wikipedia site.
        trailer_youtude: Trailer URL of the movie from the youtube site.
                
    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Initialize Movie."""
	self.title = movie_title
	self.storyline = movie_storyline
	self.poster_image_url = poster_image
	self.trailer_youtube_url = trailer_youtube
	
    def show_trailer(self):
        """Show trailer of the movie."""
	webbrowser.open(self.trailer_youtube_url)
