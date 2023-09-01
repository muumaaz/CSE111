class Netflix: 
    shows = []
    def __init__(self, name, genre, episode = 10):
        self.name = name
        self.genre = genre
        self.episode = episode
        Netflix.shows.append(self.name)

    def __str__(self):
        return f"Show Name: {self.name} \nEpisode: {self.episode} \nGenre: {', '.join(self.genre)}"

    @classmethod
    def printDetails(cls):
        print(f"Total Number of shows: {len(Netflix.shows)}")
        print('\n'.join(Netflix.shows))

    
s1 = Netflix("Wednesday",["Mystery","Supernatural"],15)
print("==========1==========")
print(s1)
s2 = Netflix("Dark",["Mind-Bending","Sci-fi"])
print("==========2==========")
print(s2)
print("==========3==========")
Netflix.printDetails()
s3 = Netflix("Suits",["Comedy","Courtroom"],20)
print("==========4==========")
print(s3)
s4 = Netflix("Demon Slayer",["Anime"],22)
print("==========5==========")
print(s4)
print("==========6==========")
Netflix.printDetails()