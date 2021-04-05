class Movies:
    movie_name = "IT"
    def __init__(self,genre):
        self.genre = genre
        print(self.genre)
    def rating(self):
        print(4)    
class Actor(Movies):
    actor_name = "Smith"
    def __init__(self,genre):
        super().__init__(genre)
        print(self.movie_name)
        

p1 = Actor("horror")

