import turtle
import time

# Setup the screen
wn = turtle.Screen()
wn.title("Turtle Chase Game")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)

# Create the player turtle
player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("green")
player.penup()
player.goto(-200, 0)

# Create the shark
shark = turtle.Turtle()
shark.speed(0)
shark.shape("triangle")
shark.color("red")
shark.penup()
shark.goto(200, 0)

# Create boundaries
boundary = turtle.Turtle()
boundary.penup()
boundary.goto(-400, -300)
boundary.pendown()
boundary.goto(400, -300)
boundary.goto(400, 300)
boundary.goto(-400, 300)
boundary.goto(-400, -300)
boundary.hideturtle()

# Score display
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

# Functions to move the player
def go_left():
    x = player.xcor()
    x -= 20
    if x < -390:
        x = -390
    player.setx(x)

def go_right():
    x = player.xcor()
    x += 20
    if x > 390:
        x = 390
    player.setx(x)

def go_up():
    y = player.ycor()
    y += 20
    if y > 290:
        y = 290
    player.sety(y)

def go_down():
    y = player.ycor()
    y -= 20
    if y < -290:
        y = -290
    player.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the shark towards the player
    shark.setheading(shark.towards(player))
    shark.forward(2)

    # Check for collision with the player
    if shark.distance(player) < 20:
        print("Game Over")
        score_display.clear()
        score_display.write(f"Game Over! Final Score: {score}", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)  # Add a delay of 2 seconds before restarting
        player.goto(-200, 0)
        shark.goto(200, 0)
        score = 0
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Update score based on time survived
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    time.sleep(0.05)  # Control the speed of the game

wn.mainloop()
