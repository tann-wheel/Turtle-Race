from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(500,400)

user_bet=screen.textinput(title="Enter the bet",prompt="Who is going to win?: ")
y_positions=[-70,-40,-10,20,50,80]
colors=["red","green","blue","yellow","orange","purple"]
all_turtles=[]
is_still_on=False

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)




if user_bet:
    is_still_on=True

while is_still_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_still_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print("You Won")
            else:
                print("You lost")
            print(f"{winning_color} won the race")

        random_num = random.randint(0, 10)
        turtle.forward(random_num)











screen.exitonclick()