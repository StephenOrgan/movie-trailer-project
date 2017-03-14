import stevemovies
import media


#Generate instances of the movie object to represent favourite movies.  

pulp_fiction = media.Movie("Pulp Fiction",
                           "You won't know the facts until you've seen the fiction.",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_(1994)_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

the_big_lebowski = media.Movie("The Big Lebowski",
                        "The Coen brothers and their agreeable cast make more "
                        "fun than sense with this scattered farce about a "
                        "pothead bowler who is mistaken for a deadbeat "
                        "philanthropist and drawn into a cluster of kidnapers, "
                        "nihilists, porn mobsters and Busby Berkeley beauties.",
                        "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                        "https://www.youtube.com/watch?v=cd-go0oBF4Y")


goon = media.Movie("Goon",
                        "Meet Doug, The Nicest Guy You'll Ever Fight.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/Goonfinalposter.jpg/220px-Goonfinalposter.jpg",
                        "https://www.youtube.com/watch?v=NfOZaquIhG8")

memento = media.Movie("Memento",
                        "Some memories are best forgotten",
                        "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
                        "https://www.youtube.com/watch?v=0vS0E9bBSL0")

prestige = media.Movie("The Prestige",
                        "Are You Watching Closely?",
                        "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                        "https://www.youtube.com/watch?v=o4gHCmTQDVI")

twenty_eight_days_later = media.Movie("28 Days Later",
                        "His fear began when he woke up alone. His terror began "
                        "when he realised he wasn't.",
                        "http://vignette2.wikia.nocookie.net/horrormovies/images/e/e1/28-Days-Later-Posters.jpg",
                        "https://www.youtube.com/watch?v=HEkJAaGhJhQ")


#Store movie instances as an array so it can be passed to stevemovies

movie_array = [pulp_fiction, the_big_lebowski, goon, memento, prestige,
               twenty_eight_days_later]

stevemovies.open_movies_page(movie_array)


