# This file was created by Alan Kim
# Game Name: Snake
# Goal of the game: player starts game off as a snake, and uses arrow keys to collect food.
# When the snake eats food, represented by a yellow circle, it grows longer.
# The game ends if the snake runs into the border or its head comes in direct contact with its body.

# Sources: 
# https://www.geeksforgeeks.org/python-turtle-screen-setup-method/
# https://docs.python.org/3/library/turtle.html


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setting up screen, width/height, background color, and title of the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("🐍 ⓈⓃⒶⓀⒺ ⒼⒶⓂⒺ 🐍")

# tracer function turns automatic updates on/off, can also delay drawings in turtle
screen.tracer(0)
# define snake and food as turtle
snake = Snake()
food = Food()


# scoreboard
scoreboard = Scoreboard()

# function that listens for keys - arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game on loop, time interval so snake keeps moving
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect Collision with food: when detect in range adds another block to snake's body
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #Detect Collision with wall: snake and food resets/refreshes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        food.refresh()


    #Detect Collision with Tail: snake and food resets/refreshes
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <5:
            scoreboard.reset()
            snake.reset()
