#3
class Song:
    def __init__(self, title, duration, artist = "Unknown Artist"):
        self.__title = title
        self.__duration = duration
        self.__artist = artist

    def info(self):
        min = self.__duration // 60
        sec = self.__duration % 60
        return f"{self.__title} by {self.__artist} ({min}:{sec})"

class Playlist():
    def __init__(self, name, song_list = None, now_id = 1):
        self.__name = name
        self.__song_list = song_list
        self.__now_id = now_id

    def play_next(self):


s1 = Song("The Flower Duet", "Leo Delibes", 86)
print(s1.info())
# Output:
# The Flower Duet by Leo Delibes (1:26)

print('===============')
s2 = Song("Winter")
print(s2.info())
# Output:
# Cannot create song without title and duration!
# --- Error --- by --- Error --- (0:0)

print('===============')
s2.set_title("Winter")
s2.set_duration(223)
s2.set_artist("Vivaldi")
print(s2.info())
# Output:
# Winter by Vivaldi (3:43)

print('===============')
s3 = Song("Ride of the Valkyries", "Wagner", 137)
s4 = Song("Russian Dance - Nutcracker", 71)

p1 = Playlist("Classical Orchestra", s1, s2, s3)
p1.show_playlist()
# Output:
# Playlist: Classical Orchestra
# Total Songs: 3
# 1. The Flower Duet by Leo Delibes (1:26)
# 2. Winter by Vivaldi (3:43)
# 3. Ride of the Valkyries by Wagner (2:17)

print('===============')
p1.play_next()
# Output:
# Now playing: The Flower Duet by Leo Delibes (1:26)

print('===============')
p1.play_prev()
# Output:
# Cannot go to previous from the first song.
# Now playing: The Flower Duet by Leo Delibes (1:26)

print('===============')
p1.play_next()
# Output:
# Now playing: Winter by Vivaldi (3:43)

print('===============')
p1.play_next()
# Output:
# Now playing: Ride of the Valkyries by Wagner (2:17)

print('===============')
p1.play_next()
# Output:
# Reached the end of the playlist, starting from the first song.
# Now playing: The Flower Duet by Leo Delibes (1:26)

print('===============')
p1.play_next()
# Output:
# Now playing: Winter by Vivaldi (3:43)

print('===============')
p1.add_songs(s4)
# Output:
# Added 1 song(s) to the playlist Classical Orchestra

print('===============')
p1.play_next()
# Output:
# Now playing: Ride of the Valkyries by Wagner (2:17)

print('===============')
p1.play_next()
# Output:
# Now playing: Russian Dance - Nutcracker by Unknown Artist (1:11)

print('===============')
p1.play_prev()
# Output:
# Now playing: Ride of the Valkyries by Wagner (2:17)

print('===============')
p1.show_playlist()
# Output:
# Playlist: Classical Orchestra
# Total Songs: 4
# 1. The Flower Duet by Leo Delibes (1:26)
# 2. Winter by Vivaldi (3:43)
# 3. Ride of the Valkyries by Wagner (2:17)
# 4. Russian Dance - Nutcracker by Unknown Artist (1:11)
