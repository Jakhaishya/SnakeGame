import turtle
import random
import time
import pygame

# Setting up the game screen
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)  
screen.bgcolor("#333333")  

# Creating a colorful border
border_turtle = turtle.Turtle()
border_turtle.speed(0)
border_turtle.pensize(4)
border_turtle.penup()
border_turtle.goto(-300, 250)
border_turtle.pendown()
border_turtle.color("#FF5733")
for _ in range(2):
    border_turtle.forward(600)
    border_turtle.right(90)
    border_turtle.forward(500)
    border_turtle.right(90)
border_turtle.hideturtle()

# Initialize game variables
score = 0
delay = 0.1  

# Create the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

# Food initialization
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")  
fruit.color("#FF5733")  
fruit.penup()
fruit.goto(30, 30)

# Keep track of the snake's tail
snake_body = []

# Score display
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 270)  
scoring.write("Score: 0", align="center", font=("Courier", 24, "bold"))

# Initialize pygame
pygame.init()

eat_sound = pygame.mixer.Sound("eat_sound.mp3")  # Sound for eating fruit
game_over_sound = pygame.mixer.Sound("game_over.mp3")  # Sound for game over


# Snake movement functions
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"        

# Function to move the snake
def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    elif snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    elif snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    elif snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main game loop
while True:
    screen.update()  # Update the screen to reflect changes
    
    # Check if snake collides with fruit
    if snake.distance(fruit) < 20:

        # Move fruit to a new random location
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        # Increase score and update scoring display
        score += 1
        scoring.clear()
        scoring.write(f"Score: {score}", align="center", font=("Courier", 24, "bold"))
        eat_sound.play()
        

        # Add a new body segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")  # Color can vary based on segment
        new_segment.penup()
        snake_body.append(new_segment)

    # Move the body segments in reverse order
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index - 1].xcor()
        y = snake_body[index - 1].ycor()
        snake_body[index].goto(x, y)

    # Move the first segment to where the snake is
    if len(snake_body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x, y)
    snake_move()
    
    # Check for collisions with the border
    if snake.xcor() > 280 or snake.xcor() < -280 or snake.ycor() > 240 or snake.ycor() < -240:
        game_over_sound.play()
        
        # Game over sequence
        time.sleep(2)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write(f"Game Over\nYour score is {score}", align="center", font=("Courier", 30, "bold"))
        break
    
    # Check for collisions with the snake's own body
    for segment in snake_body:
        if segment.distance(snake) < 20:
            # Game over sequence
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write(f"Game Over\nYour score is {score}", align="center", font=("Courier", 30, "bold"))
            break
    time.sleep(delay)
    
pygame.quit()
turtle.done()  
