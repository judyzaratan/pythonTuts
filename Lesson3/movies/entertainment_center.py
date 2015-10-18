import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
#calls init function to create a new movie

#print (toy_story.storyline)


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://moviecultists.com/wp-content/uploads/2009/11/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print(avatar.storyline)
#avatar.show_trailer()


guardians = media.Movie("Guardians of the Galaxy",
                       "A comic based movie",
                       "http://static2.hypable.com/wp-content/uploads/2014/05/guardians-of-the-galaxy-poster-new-HD.jpg",
                       "https://www.youtube.com/watch?v=GQRqShJGIJc")
guardians.show_trailer()
