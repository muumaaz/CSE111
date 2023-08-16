#1

#Write your codes for subtasks here.
class HackathonTeam:
    def __init__(self, *name):
        self.title = name[0]
        self.team = name[1::]

    def information(self):
        print(f"Team name: {self.title}")
        print(f"Participants: ")
        for i in self.team:
            print(i)

team_1 = HackathonTeam("Atlantean", "Aquaman")
team_1.information()


print("=================")


team_2 = HackathonTeam("Avengers", "Ironman", "Thor", "Hulk")
team_2.information()


print("=================")


team_3 = HackathonTeam("X-Men", "Storm", "Mystique")
team_3.information()
