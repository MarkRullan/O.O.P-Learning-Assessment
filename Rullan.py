#L.A 14
#Mark Rullan
class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)
        
    def describeSpiderman(self):
        print(f"Name:{self.name.upper()}, Age: {self.age}, {self.movieTitle.upper()}.")
        
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age,)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age,)
        self.movieTitle = movieTitle
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age,)
        self.movieTitle = movieTitle
        
tobey = Tobey("Tobey", 49, "Spider-Man")
andrew = Andrew("Andrew", 41, "The Amazing Spider-Man")
tom = Tom("Tom", 28, "Spider-Man: No Way Home")

print(tobey.name.upper(), tobey.movieTitle)
print(andrew.name.upper(), andrew.movieTitle)
print(tom.name.upper(), tom.movieTitle)
