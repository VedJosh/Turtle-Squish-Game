from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shapesize(1)
        self.shape('turtle')
        self.up()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def is_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
    
    def go_back_to_origin(self):
        self.goto(STARTING_POSITION)
    