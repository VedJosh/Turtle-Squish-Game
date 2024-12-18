import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player generated
PLAYER = Player()
LEVEL = 1 # starting with 1st level

# setting key control
screen.listen()
screen.onkeypress(fun=PLAYER.move_forward,key='Up')

# setting screenboard
SCOREBOARD = Scoreboard()

# car obstacles 
cars = CarManager()
for i in range(40):
    x = randint(-260,260)
    y = randint(-260,260)
    cars.generate_car(x,y)

# loop of the game
game_interation_num = 0
game_is_on = True

while game_is_on:
    # generating new cars on right hand corner
    if game_interation_num%6==0:
        cars.generate_car(300,randint(-260,260))
    
    # moving each and every car
    cars.move_cars()

    # deleting cars from screen as well as memory for efficient gaming
    for car in cars.cars_list:
        if car.xcor() < -300:
            car.hideturtle()
            cars.cars_list.remove(car)

    # updating scoreboard
    SCOREBOARD.write_score(LEVEL)
    
    # if player reached the top corner sucessfully, increase the level
    if PLAYER.is_finished():
        LEVEL+=1
        PLAYER.go_back_to_origin()
    
    # if the PLAYER collides with the car, game over
    for car in cars.cars_list:
        if car.distance(PLAYER)<20:
            SCOREBOARD.game_over()
            game_is_on = False

    time.sleep(0.1)
    screen.update()

screen.exitonclick()