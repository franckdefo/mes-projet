#coding:utf-8

from tkinter import  *
import time

#cree une fenetre de feu de signalisation
fenetre = Tk()
#titre de la fenetre
fenetre.title("feu_signalisation")
canvas = Canvas(fenetre,width=300,height=550,bg='blue')
canvas.pack(side=TOP,padx=5,pady=5)
ligne=canvas.create_line(150,50,150,500,width=1)

def debut():
    canvas.create_oval(100,50,200,150,width=1,fill="black")
    canvas.create_oval(100,300,200,200,width=1,fill="black")
    canvas.create_oval(100,450,200,350,width=1,fill="black")

def rouge(a):
    for i in range(a):
        canvas.create_oval(100, 50, 200, 150, width=1, fill="red")
        fenetre.update()
        time.sleep(1)

def orange(a):
    for i in range(a):
        canvas.create_oval(100,300,200,200,width=1,fill="orange")
        fenetre.update()
        time.sleep(1)

def verte(a):
    for i in range(a):
        canvas.create_oval(100,450,200,350,width=1,fill="green")
        fenetre.update()
        time.sleep(1)

while True:
    debut()
    rouge(5)
    debut()
    verte(5)
    debut()
    orange(2)
    pass




