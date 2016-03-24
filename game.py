#coding=utf-8
import Tkinter
import random
import threading
import sys
import tkMessageBox

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
window.title("贪吃蛇")
canvas = Tkinter.Canvas(window,bg="white",width=300,height=300)
canvas.pack()

class SnakeNode:
    coordX = 0
    coordY = 0
    direction = ""
    def __init__(self,coordX,coordY,direction,color="blue"):
        self.coordX = coordX
        self.coordY = coordY
        if coordX > 0 and coordY > 0:
            self.body = canvas.create_rectangle(coordX,coordY,coordX+20,coordY+20,fill=color)
        self.direction = direction
    def move(self):
        if self.direction != "":
            if self.direction == "Up":
                canvas.move(self.body,0,-20)
                self.coordY -= 20
            elif self.direction == "Down":
                canvas.move(self.body,0,20)
                self.coordY += 20
            elif self.direction == "Left":
                canvas.move(self.body,-20,0)
                self.coordX -= 20
            elif self.direction == "Right":
                canvas.move(self.body,20,0)
                self.coordX += 20

def add_food():
    global list
    global food
    intX = random.randint(0,col-1)*20
    intY = random.randint(0,row-1)*20
    intX if intX == 300 else 280
    intY if intY == 300 else 280
    list[intX/20][intY/20] = 1
    food = SnakeNode(intX,intY,"")
    #window.after(1000,add_food)

def change_direct(event):
    global direct
    global snake
    if direct.index(snake[0].direction) + direct.index(event.keysym) == 3:
        return
    snake[0].direction = event.keysym
    #snake[0].move()
    #move_snake()

def move_snake():
    global snake
    global food
    eat_food(snake[0],food)

    if snake[0].coordX>=280 or snake[0].coordY>=280 or snake[0].coordX<=0 or snake[0].coordY<=0:
        tkMessageBox.showinfo("提示", "Game over")
        #window.destroy()

    for i in range(1,len(snake)):
        if snake[i].coordX - snake[i-1].coordX < 0:
            snake[i].direction = "Right"
        elif snake[i].coordX - snake[i-1].coordX > 0:
            snake[i].direction = "Left"
        if snake[i].coordY - snake[i-1].coordY < 0:
            snake[i].direction = "Down"
        elif snake[i].coordY - snake[i-1].coordY > 0:
            snake[i].direction = "Up"
    for i in range(0,len(snake)):
        snake[i].move()
    window.after(1000,move_snake)

def eat_food(head,food):
    global snake
    x = 0
    y = 0
    if head.direction == "Up":
        y = -20
    elif head.direction == "Down":
        y = 20
    elif head.direction == "Left":
        x = -20
    elif head.direction == "Right":
        x = 20
    if (head.coordX+x) == food.coordX and (head.coordY+y)== food.coordY:
        food.direction = head.direction
        #food.move()
        snake.insert(0,food)
        add_food()


direct = ["Up","Left","Right","Down"]
#rand = random.randint(0,3)
rand = 3
head = SnakeNode(100,100,direct[rand])
second = SnakeNode(100,80,direct[rand])
snake = [head,second]
food = SnakeNode(0,0,"")

canvas.bind_all('<KeyPress-Up>',change_direct)
canvas.bind_all('<KeyPress-Down>',change_direct)
canvas.bind_all('<KeyPress-Left>',change_direct)
canvas.bind_all('<KeyPress-Right>',change_direct)

#canvas.move(snake,20,0)
add_food()
window.after(0,move_snake)
#window.after(0,add_food)
window.mainloop()