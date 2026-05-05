class Movie:
    
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        
        return f"Movie: {self.title} (Directed by {self.director}, {self.year})"



titulo_input = input("Enter title: ")
director_input = input("Enter director: ")
years_input = input("Enter year: ")


mi_pelicula = Movie(titulo_input, director_input, years_input)


print(mi_pelicula)