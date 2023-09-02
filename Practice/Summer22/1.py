class Monster:
    monsterCount = 0
    
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.alive = True
     
        Monster.monsterCount += 1

    def get_details(self):
        return f"Name: {self.name}\nPower: {self.power}\nAlive: {self.alive}"

    def attack(self, *monsters):
        if not monsters:
            print("No monsters to attack")
        elif self.alive == False:
            print(f"{self.name} is not alive to attack")
        else:
            for mon in monsters:
                if mon.alive:
                    if self.power > mon.power:
                        print(f"Attack successful. {self.name} defeated {mon.name}")
                        mon.alive = False
                        Monster.monsterCount -= 1
                    else:
                        print(f"Attack unsuccessful. {self.name} was defeatd by {mon.name}")
                        self.alive = False
                        Monster.monsterCount -= 1
                else:
                    print(f"Cannot attack {mon.name}. It's not alive")

monster1 = Monster('Godzilla', 40)
monster2 = Monster('Hydra', 30)
monster3 = Monster('KingKong', 50)
print(f"Number of monsters alive:{Monster.monsterCount}")
print('1--------------------------------')
print(monster1.get_details())
print('2--------------------------------')
print(monster2.get_details())
print('3--------------------------------')
print(monster3.get_details())
print('4--------------------------------')
monster1.attack()
print('5--------------------------------')
monster1.attack(monster2)
print('6--------------------------------')
monster1.attack(monster2, monster3)
print('7--------------------------------')
print(f"Number of monsters alive:{Monster.monsterCount}")
print('8--------------------------------')
print(monster2.get_details())
print('9--------------------------------')
monster2.attack(monster1)