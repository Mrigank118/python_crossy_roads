
import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car.create_cars()
    car.move()
    screen.update()
    # Detect Collision with Block
    for x in car.all_cars:
        if player.distance(x) <= 30:
            time.sleep(1)
            scoreboard.game_over()
            game_is_on = False
    # Detect Finish Line
    if player.ycor() == 300:
        player.goto(0, -280)
        scoreboard.increase_level()
        car.increase_speed()









