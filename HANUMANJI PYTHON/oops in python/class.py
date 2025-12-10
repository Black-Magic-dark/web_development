# class Employee:
#     lang="py"
#     salary=120000


# rupam=Employee()
# name1="rupam"
# print(rupam.lang,rupam.salary,name1)
# ajit=Employee()
# ajit.name= "ajit"
# print(ajit.salary,ajit.name)

from turtle import *
import colorsys
bgcolor("black")
speed(0)
pensize(1)

for i in range(12):
    color(colorsys.hsv_to_rgb(i/12, 1.0, 1.0))
    left(30)
    for j in range(20):
        circle(150-j*5, 90)
        left(90)
        circle(150-j*5, 90)
        left(10)
hideturtle()
done()