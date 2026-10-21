import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
time_interval = (1, 5)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")


class Spawner:
    def __init__(self):
        self.cars = []
        self.last_time = time.time()
        self.delay = random.randint(1, 2)

    def setup(self):
        self.current_time = time.time()
        if self.delay <= (self.current_time - self.last_time):
            new_car = CarManager()
            self.cars.append(new_car)
            self.last_time = time.time()
            self.delay = random.randint(1, 2)


CarControl = Spawner()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    CarControl.setup()
    for car in CarControl.cars:
        car.move()
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 280:
        time.sleep(3)
        scoreboard.reset()
        player.refresh()
        CarControl.cars.remove(car)
        CarManager.increase_speed()

screen.exitonclick()
