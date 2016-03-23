#coding=utf-8
import Tkinter
import random
import threading
import sys

#定义上下左右
up = lambda y : y+20
down = lambda y : y-20
left = lambda x : x-20
right = lambda x : x+20
#定义gameboard
col = 15
row = 15
list = [[0 for x in range(col)] for y in range(col)]   
#定义窗体
window = Tkinter.Tk()
canvas = Tkinter.Canvas(window,bg="white",width=300,height=300)
canvas.pack()


def add_food():
    intX = random.randint(0,col-1)*20
    intY = random.randint(0,row-1)*20
    intX if intX == 300 else 280
    intY if intY == 300 else 280
    food = canvas.create_rectangle(intX,intY,intX+20,intY+20,fill="blue")
    window.after(1000,add_food)

#def move():
#    canvas.move(snake,20,0)
#    window.after(1000,move)

def change_direct(event):
    global direct
    global d
    if d + direct.index(event.keysym) == 3:
        return
    #if [direct[d],event.keysym] == ["Up","Down"] or [direct[d],event.keysym] == ["Left","Right"]:
    #    return 
    d = direct.index(event.keysym)
    move(event.keysym)

def start_game():
    global direct
    global d
    move(direct[d])
    window.after(1000,start_game)

def move(direction):
    if direction == "Up":
        canvas.move(snake,0,-20)
    elif direction == "Down":
        canvas.move(snake,0,20)
    elif direction == "Left":
        canvas.move(snake,-20,0)
    elif direction == "Right":
        canvas.move(snake,20,0)

SnakeX = 100
SnakeY = 100
snake = canvas.create_rectangle(SnakeX,SnakeY,SnakeX+20,SnakeY+20,fill="red")

direct = ["Up","Left","Right","Down"]
d = random.randint(0,3)

canvas.bind_all('<KeyPress-Up>',change_direct)
canvas.bind_all('<KeyPress-Down>',change_direct)
canvas.bind_all('<KeyPress-Left>',change_direct)
canvas.bind_all('<KeyPress-Right>',change_direct)



#canvas.move(snake,20,0)
window.after(0,start_game)
#add_food()
#window.after(0,add_food)
window.mainloop()