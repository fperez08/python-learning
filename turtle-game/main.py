import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Tell the screen to listen for keyboard input
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()   # Maybe spawn a new car (every 6th tick)
    car_manager.move_cars()    # Slide all existing cars to the left

    # If the player reaches the top, start next level behavior.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

    # End the game if the player touches any car.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    screen.update()

screen.exitonclick()
