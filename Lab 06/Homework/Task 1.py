class Movie:
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre = genre
        self.duration = duration

    def movieinfo(self):
        print("==========Movie Information==========")
        print(f"Name: {self.name}\nGenre: {self.genre}\nDuration: {self.duration}")
    
    @classmethod
    def createMovie_fromString(cls, string):
        name, genre, duration = string.split('-')
        return cls(name, genre, int(duration))

class StarCinema:
    all_branch_info = {}

    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.movie_list = []

    def addMovies(self, *movie_objects):
        for movie in movie_objects:
            self.movie_list.append(movie)
            print(f"{movie.name} added to Star Cinema {self.branch_name}")
        StarCinema.all_branch_info[self.branch_name] = self.movie_list
    
    def removeMovie(self, movie_obj):
        if movie_obj in self.movie_list:
            self.movie_list.remove(movie_obj)
            StarCinema.all_branch_info[self.branch_name] = self.movie_list
    
    @classmethod
    def check(cls, movie_name):
        found = False
        for branch, movies in cls.all_branch_info.items():
            for movie in movies:
                if movie_name == movie:
                    print(f"{movie_name} is available in {branch}")
                    found = True
        if not found:
            print(f"{movie_name} is not available in any branch")
    
    @classmethod
    def showAllBranchinfo(cls):
        for branch, movies in cls.all_branch_info.items():
            n = 1
            for movie in movies:
                print(f"Branch Name: {branch}")
                print(f"Movie No: {n}")
                print(f"Movie Name: {movie.name}")
                print(f"Movie Genre: {movie.genre}")
                print(f"Movie Genre: {movie.duration}")
                n += 1


movie1 = Movie("Oppenheimer", "Biography", 120)
movie1.movieinfo()
movie2 = Movie.createMovie_fromString("Barbie-Comedy-120")
movie2.movieinfo()
cinema = StarCinema("Banani")
cinema.addMovies(movie1, movie2)
movie3 = Movie.createMovie_fromString("The Dark Knight-Action-120")
cinema.removeMovie(movie2)
cinema.addMovies(movie3)
StarCinema.check("Oppenheimer")
cinema1 = StarCinema("Uttara")
cinema1.addMovies(movie1, movie2)
StarCinema.showAllBranchinfo()
