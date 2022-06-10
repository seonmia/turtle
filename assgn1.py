

path = 'C:/Users/Seonmi Shin/Desktop/assn1_skeleton (1)/data.txt'
f = open(path, 'r')
file_str = f.read()

bar_arr = file_str.split()

import turtle as t


# parameters
turtle_speed = 9

# constants
AXIS_LENGTH = 500
AXIS_MARGIN = 20
AXIS_WIDTH = 3

LABELS = ["A", "B", "C", "D", "E", "F"]
COLORS = ["red", "blue", "green", "pink", "grey", "yellow"]


a_cnt = 0 
b_cnt = 0 
c_cnt = 0
d_cnt = 0 
e_cnt = 0 
f_cnt = 0 
for i in bar_arr:
    if i == 'A':
        a_cnt += 1
    elif i == 'B': 
        b_cnt += 1 
    elif i == 'C':
        c_cnt += 1
    elif i == 'D':
        d_cnt += 1 
    elif i == 'E':
        e_cnt += 1
    elif i == 'F':
        f_cnt += 1

# print(a_cnt, b_cnt, c_cnt, d_cnt, e_cnt, f_cnt)


a_arr = []
b_arr = [] 
c_arr = [] 
d_arr = [] 
e_arr = [] 
f_arr = []


for j in range(len(bar_arr)):
    if bar_arr[j] == "A":
        a_arr.append(bar_arr[j+1])
    elif bar_arr[j] == 'B':
        b_arr.append(bar_arr[j+1])
    elif bar_arr[j] == 'C':
        c_arr.append(bar_arr[j+1])
    elif bar_arr[j] == 'D':
        d_arr.append(bar_arr[j+1])
    elif bar_arr[j] == 'E':
        e_arr.append(bar_arr[j+1])
    elif bar_arr[j] == 'F':
        f_arr.append(bar_arr[j+1])


        




def axis():
    t.shape("turtle")
    t.speed(turtle_speed)
    t.width(AXIS_WIDTH)
    ####### Enter Your Code ########

    t.penup()
    t.setposition(-430,-350)
    t.pendown()
    t.fd(500)
    t.left(135)
    t.fd(20)
    t.backward(20)
    t.left(90)
    t.fd(20)
    t.right(180)
    t.fd(20)
    t.left(135)
    t.fd(500)
    t.right(90)
    t.fd(500)
    t.left(135)
    t.fd(20)
    t.backward(20)
    t.left(90)
    t.fd(20)
    t.backward(20)
    t.right(45)
    t.fd(500)
    t.right(180)

    ####### End of the Code ########



def bar_chart():
    PIXEL_PER_VAL = 2.5  
    ####### Enter Your Code ########
  
# label A

    t.begin_fill()
    t.fillcolor(COLORS[0])
    t.pencolor("#000000")
    t.fd(a_cnt*PIXEL_PER_VAL)
    t.right(90)
    t.fd(80)
    t.right(90)
    t.fd(a_cnt*PIXEL_PER_VAL)
    t.end_fill()
    t.left(180)


# label B 

    t.begin_fill()
    t.fillcolor(COLORS[1])
    t.pencolor("#000000")
    t.fd(b_cnt*PIXEL_PER_VAL)
    t.right(90)
    t.fd(80)
    t.right(90)
    t.fd(b_cnt*PIXEL_PER_VAL)
    t.end_fill()
    t.left(180)


# label C

    t.begin_fill()
    t.fillcolor(COLORS[2])
    t.pencolor("#000000")
    t.fd(c_cnt*PIXEL_PER_VAL)
    t.right(90)
    t.fd(80)
    t.right(90)
    t.fd(c_cnt*PIXEL_PER_VAL)
    t.end_fill()
    t.left(180)


# label D

    t.begin_fill()
    t.fillcolor(COLORS[3])
    t.pencolor("#000000")
    t.fd(d_cnt*PIXEL_PER_VAL)
    t.right(90)
    t.fd(80)
    t.right(90)
    t.fd(d_cnt*PIXEL_PER_VAL)
    t.end_fill()
    t.left(180)


# label E

    t.begin_fill()
    t.fillcolor(COLORS[4])
    t.pencolor("#000000")
    t.fd(e_cnt*PIXEL_PER_VAL)
    t.right(90)
    t.fd(80)
    t.right(90)
    t.fd(e_cnt*PIXEL_PER_VAL)
    t.end_fill()
    t.left(180)


# label F

    t.begin_fill()
    t.fillcolor(COLORS[5])
    t.pencolor("#000000")
    t.fd(f_cnt*PIXEL_PER_VAL)
    t.right(90)
    t.fd(80)
    t.right(90)
    t.fd(f_cnt*PIXEL_PER_VAL)
    t.end_fill()
    t.left(180)

    ####### End of the Code ########




def scatterplot():
    PIXEL_PER_VAL = 5
    ####### Enter Your Code ########
    for i in a_arr:
        t.penup()
        t.goto(-390,-350 + int(i)*PIXEL_PER_VAL)
        t.pendown()
        t.pencolor(COLORS[0])
        t.dot(PIXEL_PER_VAL)


    for i in b_arr:
        t.penup()
        t.goto(-310,-350 + int(i)*PIXEL_PER_VAL)
        t.pendown()
        t.pencolor(COLORS[1])
        t.dot(PIXEL_PER_VAL)            
        
    for i in c_arr:
        t.penup()
        t.goto(-230,-350 + int(i)*PIXEL_PER_VAL)
        t.pendown()
        t.pencolor(COLORS[2])
        t.dot(PIXEL_PER_VAL)   

    for i in d_arr:
        t.penup()
        t.goto(-150,-350 + int(i)*PIXEL_PER_VAL)
        t.pendown()
        t.pencolor(COLORS[3])
        t.dot(PIXEL_PER_VAL)   


    for i in e_arr:
        t.penup()
        t.goto(-70,-350 + int(i)*PIXEL_PER_VAL)
        t.pendown()
        t.pencolor(COLORS[4])
        t.dot(PIXEL_PER_VAL)   


    for i in f_arr:
        t.penup()
        t.goto( 10,-350 + int(i)*PIXEL_PER_VAL)
        t.pendown()
        t.pencolor(COLORS[5])
        t.dot(PIXEL_PER_VAL)   

    ####### End of the Code ########




def line_chart():
    PIXEL_PER_VAL = 2.5
    ####### Enter Your Code ########

# A
    t.penup()
    t.goto(-390, -350 + len(a_arr)*PIXEL_PER_VAL)
    t.pendown()
    t.begin_fill()
    t.color(COLORS[0])
    t.circle(5, 360)
    t.end_fill()
    t.pencolor('#000000')


#  B  
    t.goto(-310, -350+ len(b_arr)*PIXEL_PER_VAL)
    t.begin_fill()
    t.color(COLORS[1])
    t.circle(5, 360)
    t.end_fill()
    t.pencolor('#000000')

# C
    t.goto(-230, -350+ len(c_arr)*PIXEL_PER_VAL)
    t.begin_fill()
    t.color(COLORS[2])
    t.circle(5, 360)
    t.end_fill()
    t.pencolor('#000000')

# D
    t.goto(-150, -350 +len(d_arr)*PIXEL_PER_VAL)
    t.begin_fill()
    t.color(COLORS[3])
    t.circle(5, 360)
    t.end_fill()
    t.pencolor('#000000')

# E
    t.goto(-70, -350+ len(e_arr)*PIXEL_PER_VAL)
    t.begin_fill()
    t.color(COLORS[4])
    t.circle(5, 360)
    t.end_fill()
    t.pencolor('#000000')


# F
    t.goto( 10, -350+ len(f_arr)*PIXEL_PER_VAL)
    t.begin_fill()
    t.color(COLORS[5])
    t.circle(5, 360)
    t.end_fill()
    t.pencolor('#000000')
    ####### End of the Code ########


def free_turtle():
    t.reset()


axis()
bar_chart()
free_turtle()
axis()
scatterplot()
free_turtle()
axis()
line_chart()
t.exitonclick()



