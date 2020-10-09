#coding:utf-8
#!/usr/bin/env/python
from tkinter import *


def clique(nombre):
    global operation
    operation=operation+str(nombre)
    var_entry.set(operation)
def efface():
    global operation
    operation=""
    var_entry.set(operation)
def resultat():
    global operation
    sum=eval(operation)
    var_entry.set(sum)
    operation=""




#MENU

#cree une fenetre
fenetre = Tk()
#titre
fenetre.title("calculatrice")
operation = ""
#icon
#fenetre.iconbitmap("pepsi.ico")
#code principale


var_entry = StringVar()
entry = Entry(fenetre,font=('arial',20,'bold'),textvariable=var_entry,bd=16,insertwidth=4,
              bg='purple',justify='right').grid(columnspan=4)

button7 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="7",command=lambda:clique(7)).grid(row=1,column=0)

button8 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="8",command=lambda:clique(8)).grid(row=1,column=1)

button9 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="9",command=lambda:clique(9)).grid(row=1,column=2)

addition= Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="+",command=lambda:clique("+")).grid(row=1,column=3)

button4 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="4",command=lambda:clique(4)).grid(row=2,column=0)

button5 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="5",command=lambda:clique(5)).grid(row=2,column=1)

button6 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="6",command=lambda:clique(6)).grid(row=2,column=2)

soutraction= Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="-",command=lambda:clique("-")).grid(row=2,column=3)

button1 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="1",command=lambda:clique(1)).grid(row=3,column=0)

button2 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="2",command=lambda:clique(2)).grid(row=3,column=1)

button3 = Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),
                 text="3",command=lambda:clique(3)).grid(row=3,column=2)

division= Button(fenetre,padx=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="/",command=lambda:clique("/")).grid(row=3,column=3)
button0 = Button(fenetre,padx=18,pady=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="0",command=lambda:clique(0)).grid(row=4,column=0)

afface = Button(fenetre,padx=18,pady=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="<-",command=efface).grid(row=4,column=1)

egale= Button(fenetre,padx=18,pady=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="=",command=resultat).grid(row=4,column=2)

multiplication= Button(fenetre,padx=18,pady=18,bd=7,fg='black',font=('arial',20,'bold'),bg='orange',
                 text="*",command=lambda:clique("*")).grid(row=4,column=3)
#affiche la fenetre
fenetre.mainloop()
