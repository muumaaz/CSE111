class Netflix: 
    total = 0
    lst = []
    def __init__(self, name, genre, episode = 10):
        self.name = name
        self.genre = ', '.join(i for i in genre)
        self.episode = episode
        Netflix.total += 1
        Netflix.lst.append(self.name)


    def __str__(self):
        return f"Show Name: {self.name} \nEpisode: {self.episode} \nGenre: {self.genre}"

    @classmethod
    def printDetails(cls):
        print(f"Total Number of shows: {Netflix.total}")
        for i in Netflix.lst:
            print(i)
    
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