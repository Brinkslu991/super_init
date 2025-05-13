class Human:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def think(self):
        print("The human is thinking deeply.")

    def communicate(self):
        print("The human is communicating clearly.")

class AI(Human):
    def __init__(self, name, age, occupation, intelligence_level):
        self.intelligence_level = intelligence_level
        super().__init__(name, age, occupation)

    def think(self):
        print("The A`perform_task()` online.")

    def communicate(self):
        print("The AI is communicating digitally with its human.")

    def learn(self):
        print("The AI is learning and improving its capabilities.")
    
    def analyze(self):
        print(f'The AI is analyzing data.')

class Robot(Human):
    def __init__(self, name, age, occupation):
        super().__init__(name, age, occupation)

    def task(self):
        print(f'{self.name} is throwing a large containmet crate.')


my_ai = AI("Athena", 5, "Virtual Assistant", 9.8)
ai1 = AI('John', 1, 'Virtual Assistant', 1)
robo1 = Robot('Ethan', 6, 'Enhanced Tactical Humanoid 3rd Revision')
print(my_ai.name)
print(my_ai.age)
print(my_ai.occupation)
print(my_ai.intelligence_level)
my_ai.think()
my_ai.communicate()
my_ai.learn()

ai1.analyze()

print(robo1.name)
print(robo1.age)
print(robo1.occupation)
robo1.task()