class Movie:
    
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"

title = input("Enter title: ")
director = input("Enter director: ")
year = input("Enter year: ")

movie = Movie(title, director, year)


print(movie)