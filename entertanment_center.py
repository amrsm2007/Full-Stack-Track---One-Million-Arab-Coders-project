import media
import fresh_tomatoes


avatar=media.Movie("Avatar",
                   "A paraplegic marine dispatched to the moon Pandora on a unique mission "
                   "becomes torn between following his orders and protecting the world he "
                   "feels is his home.",
                   "https://images-na.ssl-images-amazon.com/images/M"
                   "/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                   "https://www.youtube.com/watch?v=5PSNL1qE6VY")

horton=media.Movie("Horton Hears a Who!",
                   "Horton the Elephant struggles to protect a microscopic community "
                   "from his neighbors who refuse to believe it exists.",
                   "https://images-na.ssl-images-amazon.com/images/M/"
                   "MV5BMWFiYTRiMDEtODU1Ny00ZTg4LWE1ZTMtMWYxMDYyNzNlMjk4XkEyXkFqcGdeQXVyNzYxODQ5NjM@._V1_.jpg",
                   "https://www.youtube.com/watch?v=0c57WC9Vc30")
how_to_train_your_dragone=media.Movie("How to Train Your Dragon",
                                      "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend "
                                      "of a young dragon himself",
                                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMj"
                                      "A5NDQyMjc2NF5BMl5BanBnXkFtZTcwMjg5ODcyMw@@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                      "https://www.youtube.com/watch?v=TgmJPcs6BE8"
                                      )
croods=media.Movie("The Croods",
                   "After their cave is destroyed, a caveman family must trek through an unfamiliar fantastical world"
                   " with the help of an inventive boy.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyOTc2OTA1Ml5BMl5BanBnXkFtZT"
                   "cwOTI1MjkzOQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=4fVCKy69zUY")
avengers=media.Movie("The Avengers",
                     "Earth's mightiest heroes must come together and learn to fight as a team if they are going to"
                     " stop the mischievous Loki and his alien army from enslaving humanity.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg"
                     "0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=eOrNdBpGMv8"
                     )
dory=media.Movie("Finding Dory",
                 "Dory, begins a search for her long-lost parents, and everyone learns a few things about"
                 " the real meaning of family along the way.",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwM"
                 "zk3MTgyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                 "https://www.youtube.com/watch?v=0tkLUap7oGQ")




movies=[avatar,horton,how_to_train_your_dragone,croods,avengers,dory]

fresh_tomatoes.open_movies_page(movies)

#print media.Movie.__doc__
#print (media.Movie.__name__)
#print (media.Movie.__module__)
