import turtle
import time       # this module is used for creating for the screen update.
import random


def go_up():
    if snake.direction != "down" : 
        snake.direction = "up"

def go_down():
    if snake.direction != "up" : 
        snake.direction = "down"
    
def go_left():
    if snake.direction != "right" : 
        snake.direction = "left"
    
def go_right():
    if snake.direction != "left" :
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
        

wn = turtle.Screen()
wn.bgcolor("green")
            # tracer is the amountof delay that will be caused for updating the animation that we will be creating
wn.title("Snake game by Aryan garg!!")
wn.setup(width = 600, height = 600)
wn.tracer(0)     # if tracer is there then the updates of the screen stop

# after tracer is there then UPDATE the scrren again and again.

snake = turtle.Turtle()
snake.penup()
snake.goto(0,0)
snake.shape("square")
snake.color("red")
snake.speed(0)
snake.direction = "right"


food = turtle.Turtle()
food.penup()
food.shape("circle")
food.goto(0,100)
food.color("blue")
snake.speed(0)


# this is the turtle that we are creating for the scoring.

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.shape("square")
pen.color("white")
pen.write("Score : 0   High Score : 0", align = "center", font = ("courier", 24, "normal"))





'''
triangle = turtle.Turtle()
triangle.setpos(30,60)
triangle.left(60)
triangle.forward(100)
triangle.right(120)
triangle.forward(100)
triangle.right(120)
triangle.forward(100)
'''

score = 0
high_score = 0 


# we will also have to develop the events for the key press

wn.listen()

wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


segments = []     # This list will store all the parts of the snake body

while True:
    
    wn.update()          # This is required for modification wrt to the tracer
    time.sleep(0.2)
    
    
    if snake.distance(food) < 20 :     # then we will have to move the snake to a random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        
        # then in this we also have to add a new segment
        
        segment = turtle.Turtle()   # the position of this turtle will be the poition of the last segment ka agla
        segment.speed(0)
        segment.penup()
        segment.shape("square")
        segment.color("grey")
        segments.append(segment)
        
        score += 10
        
        if score > high_score :
            high_score = score
        
        pen.clear()     # We will remove the older entry
        
        pen.write("Score : {}   High Score : {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))
        
        
        
        
        
        
        
        # The list will have the last index to [len(list)-1] and the index 0  will not be included there rather till index 1 it is there
        
        
    for index in range(len(segments)-1, 0, -1):
        x =  segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
        
    if len(segments) > 0 :
        tx = snake.xcor()
        ty = snake.ycor()
        segments[0].goto(tx, ty)
    
    # after adding of the new segment we will check whether the snake is not touching its body part or not
    
    move()
    
    for part in segments:
        if part.distance(snake) < 20:
            snake.goto(0,0)
            snake.direction = "stop"
            time.sleep(1)
            
            score = 0
            
            pen.clear()
            
            pen.write("Score : {}  High Score : {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))
            
            for part in segments :
                part.goto(1000, 1000)
            
            segments.clear()
    
    # We will also check whether the snake is not colliding with the borders of the screen
    
    if snake.xcor() < -290 or snake.xcor() > 290 or snake.ycor() < -290 or snake.ycor() > 290 :
        snake.goto(0, 0)
        snake.direction = "stop"
        time.sleep(1)
        
        score = 0
        
        pen.clear()
        
        pen.write("Score : {}  High Score : {}".format(score, high_score), align = "center", font = ("courier", 24, "normal"))
        
        for part in segments:
            part.goto(1000, 1000)
            
        segments.clear()
        
    

        
        
    
    
wn.mainloop()
