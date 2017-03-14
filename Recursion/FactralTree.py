import turtle
"""
t = turtle.Turtle()
t_win = turtle.Screen()


def draw_tree(t,line_len):
    if line_len > 0:
        t.right(20)
        t.forward(line_len)
        draw_tree(t,line_len - 10)
        #t.backward(line_len)
        #t.left(40)
        #t.forward(line_len)
        #draw_tree(t,line_len - 10)

t.left(90)
t.forward(100)
draw_tree(t,100)
t_win.exitonclick()
"""

def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.color('red')
        t.circle(3)
        t.color('green')
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()
main()


"""
from turtle import *

color('white', 'blue')
begin_fill()
while True:
    forward(100)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""