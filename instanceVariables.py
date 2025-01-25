class Team:
    team = 'Manchester Utd.'
    #initialising instance variables in a constructor
    def __init__(self, name, jersey):
        self.name = name
        self.jersey = jersey
    #initialising instance variable inside a instance method
    def play(self, position):
        self.position = position

    def showDetails(self):
        print(f"{self.name} has a jersey no: {self.jersey} and playing as a {self.position}.")

#taking input from the user
name = input("Enter the name: ")
jersey = input('Enter the jersey no: ')
position = input('Enter the position: ')

p1 = Team(name,jersey)
# p2 = Team(name,jersey)
p1.play(position)
# p2.play(position)

p1.showDetails()
print(Team.team)
print(p1.team)
print(p1.__dict__)
# p2.showDetails()


    