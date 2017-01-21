import fresh_tomatoes
import media


# Each assignment below calls a class object named Movie that is defined in a
# different file with a filename of media. This is called instantiation because
# it creates a new instance of the class Movie. The arguments given are passed
# on to the __init__() function over in the file where class Movie is defined.


toy_story = media.Movie("Toy Story", "Release date: November 22, 1995",
                        "Starring Tom Hanks",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


lone_survivor = media.Movie("Lone Survivor", "Release date: December 25, 2013",
                            "Starring Mark Wahlberg",
                            "True story of a soldier who endured incredible "
                            "hardship",
                            "http://www.impawards.com/2013/posters/lone_survivor.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=yoLFk4JK_RM")


american_sniper = media.Movie("American Sniper",
                              "Release date: December 25, 2014",
                              "Starring Bradley Cooper",
                              "U.S. Navy SEAL Chris Kyle is sent "
                              "to Iraq with only one mission, to protect his "
                              "brothers-in-arms.",
                              "http://boulevarddrivein.com/wordpress/wp-content/uploads/2015/03/American-Sniper-poster.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=99k3u9ay1gs")


no_escape = media.Movie("No Escape", "Release date: August 26, 2015",
                        "Starring Owen Wilson",
                        "In their new overseas home, an American family soon "
                        "finds themselves caught in the middle of a coup.",
                        "http://www.impawards.com/2015/posters/no_escape_ver7_xxlg.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=DOjj07EuO50")


unbroken = media.Movie("Unbroken", "Release date: November 17, 2014",
                       "Starring Jack O'Connell",
                       "A chronicle of the life of Louis Zamperini, an Olympic"
                       " runner who was taken prisoner by Japanese forces",
                       "http://ecx.images-amazon.com/images/I/91nsiO3qvLL.jpg",
                       "https://www.youtube.com/watch?v=kk1M_HwmFMM")


mcfarland_usa = media.Movie("McFarland, USA",
                            "Release date: February 20, 2015",
                            "Starring Kevin Costner",
                            "A recently fired football coach becomes a "
                            "legendary track coach in one of the most "
                            "economically challenged towns in the USA",
                            "https://upload.wikimedia.org/wikipedia/en/1/12/McFarland,_USA_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=j-VAOlHGE6Q")


movies = [toy_story, lone_survivor, american_sniper, no_escape, unbroken,
          mcfarland_usa]


# Calls the function open_movies_page which is a function defined in a
# different file with a filename of fresh_tomatoes and passes the list
# of movies which was created above.
fresh_tomatoes.open_movies_page(movies)
