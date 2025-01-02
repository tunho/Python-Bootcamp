# colorgram 모듈듈
import turtle
import colorgram
import math
import random

# rgb_colors = []
# colors = colorgram.extract('18/a.jpg', 25)

# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)

# color_list = [(229, 228, 226), (255, 223, 224), (199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209)]
# t = Turtle()
# t.speed(0)
# a = 1
# for i in color_list:
#         t.color(i[0]/255,i[1]/255,i[2]/255)
#         t.pensize(10) 
#         t.circle(10) 
#         t.begin_fill()
#         t.circle(6)
#         t.end_fill()   
#         t.penup()
#         if a % 5 == 0 : 
#            t.right(180)
#            t.forward(200)
#            t.left(90)
#            t.forward(50)
#            t.left(90)
#            t.pendown()
#            a += 1
#            continue
#         t.forward(50)
#         t.pendown()
#         a += 1
        
           
          
# s = Screen()
# s.exitonclick()
turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()
color_list = [(229, 228, 226), (255, 223, 224), (199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209)]
t.setheading(225)
t.forward(300)
t.setheading(0)
n = 100
for i in range(1,n) :
 t.dot(20, random.choice(color_list))
 t.forward(50)

 if i % 10 == 0 :
  t.setheading(90)
  t.forward(50)
  t.setheading(180)
  t.forward(500)
  t.setheading(0) 




s = turtle.Screen()
s.exitonclick()
