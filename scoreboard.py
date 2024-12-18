from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.goto(-280,280)
    
    def write_score(self,score):
        self.clear()
        self.write(f'Level {score}',align='center',font=FONT)
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'GAME OVER',align='center',font=FONT)