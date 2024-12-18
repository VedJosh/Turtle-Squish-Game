from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars_list = []
    
    def generate_car(self,x,y):
        color_of_car = choice(COLORS)
        car = Turtle(shape='square')
        car.up()
        car.color(color_of_car)
        car.goto(x,y)
        car.shapesize(stretch_len=2,stretch_wid=1)
        self.cars_list.append(car)
    
    def move_cars(self):
        for car in self.cars_list:
            car.backward(MOVE_INCREMENT)