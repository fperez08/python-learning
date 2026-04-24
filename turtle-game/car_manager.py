import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Cars spawn on the right edge and drive left
START_X = 300

# The screen runs from -300 to +300 on both axes.
# We keep a 50px safe zone at the top and bottom.
Y_MIN = -300 + 50   # -250
Y_MAX = 300 - 50  # 250


class CarManager:

    def __init__(self):
        self.all_cars = []          # List that holds every active car Turtle
        self.car_speed = STARTING_MOVE_DISTANCE
        self._loop_counter = 0      # Counts game-loop ticks

    def _create_car(self):
        """Spawn one car at a random y position on the right side."""
        car = Turtle("square")      # "square" shape is easy to resize
        car.color(random.choice(COLORS))
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)  # 20px tall, 40px wide
        random_y = random.randint(Y_MIN, Y_MAX)
        car.goto(START_X, random_y)
        self.all_cars.append(car)

    def create_car(self):
        """Only generate a new car on every 6th call (once per 6 game loops)."""
        self._loop_counter += 1
        if self._loop_counter % 6 == 0:
            self._create_car()

    def move_cars(self):
        """Move every car to the left by the current speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """Make cars move faster after the player reaches the finish line."""
        self.car_speed += MOVE_INCREMENT
