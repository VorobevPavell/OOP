class SoccerPlayer():

    def __init__(self,name,surname,goals=0,assits=0) -> None:
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assits = assits
    def score(self,goals=1):
        self.goals = goals
    def make_assist(self,passes=1):
        self.assits = passes
    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals},передачи: {self.assits}')
leo = SoccerPlayer('Leo','Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()
kokorin = SoccerPlayer('Alex','Kokorin')
kokorin.score()
kokorin.statistics()

""" Messi Leo - голы: 700,передачи: 500
Kokorin Alex - голы: 1,передачи: 0 """