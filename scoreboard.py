from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def update_score(self, player):
        if player == 'l':
            self.l_score += 1
        elif player == 'r':
            self.r_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.setposition(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.setposition(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))