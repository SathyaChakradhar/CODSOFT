from tkinter import * #type: ignore
from tkinter.font import BOLD #type: ignore
ex= "" 
def press(num):
    global ex
    ex = ex + str(num)
    equation.set(ex)
def equalpress():
    try:
        global ex
        total = str(eval(ex))
        equation.set(total)
        ex= ""
    except:
        equation.set(" error ") 
        ex= "" 
def clear():
    global ex
    ex= "" 
    equation.set("")
def sclear():
    global ex
    ex=ex[:len(ex)-1]
    equation.set(ex)
win = Tk()
win.title("Simple Calculator")
equation = StringVar()
head=Label(win,text="CALCULATOR",font=('Times New Roman',20,BOLD))
head.place(x=500,y=90)
expression_field = Entry(win, textvariable=equation,width=32) 
expression_field.place(x=500,y=140)
b1=Button(win,text='1',command=lambda:press(1),height=1,width=5)
b1.place(x=500,y=200)
b2=Button(win,text='2',command=lambda:press(2),height=1,width=5)
b2.place(x=550,y=200)
b3=Button(win,text='3',command=lambda:press(3),height=1,width=5)
b3.place(x=600,y=200)
b4=Button(win,text='4',command=lambda:press(4),height=1,width=5)
b4.place(x=500,y=230)
b5=Button(win,text='5',command=lambda:press(5),height=1,width=5)
b5.place(x=550,y=230)
b6=Button(win,text='6',command=lambda:press(6),height=1,width=5)
b6.place(x=600,y=230)
b7=Button(win,text='7',command=lambda:press(7),height=1,width=5)
b7.place(x=500,y=260)
b8=Button(win,text='8',command=lambda:press(8),height=1,width=5)
b8.place(x=550,y=260)
b9=Button(win,text='9',command=lambda:press(9),height=1,width=5)
b9.place(x=600,y=260)
b0=Button(win,text='0',command=lambda:press(0),height=1,width=5)
b0.place(x=550,y=290)
dot=Button(win,text='.',command=lambda:press('.'),height=1,width=5)
dot.place(x=500,y=290)
plus=Button(win,text='+',command=lambda:press('+'),height=1,width=5)
plus.place(x=650,y=200)
minu=Button(win,text='-',command=lambda:press('-'),height=1,width=5)
minu.place(x=650,y=230)
pro=Button(win,text='*',command=lambda:press('*'),height=1,width=5)
pro.place(x=650,y=260)
div=Button(win,text='/',command=lambda:press('/'),height=1,width=5)
div.place(x=650,y=170)
equ=Button(win,text='=',command=equalpress,height=1,width=5)
equ.place(x=650,y=290)
per=Button(win,text='POW',command=lambda:press('**'),height=1,width=5)
per.place(x=600,y=170)
d0=Button(win,text='00',command=lambda:press('00'),height=1,width=5)
d0.place(x=600,y=290)
clr=Button(win,text='AC',command=clear,height=1,width=5)
clr.place(x=500,y=170)
sc=Button(win,text='C',command=sclear,height=1,width=5)
sc.place(x=550,y=170)
win.mainloop()