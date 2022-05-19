#creating a simple calulator
from email.mime import image
import math
from tkinter import Label
from tkinter import*
#using grid but also pack can
root= Tk()
root.title("simple calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def Button_add(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return
def clear():
    e.delete(0,END)
def Button_addition():
    first_number=e.get()
    global f_numb
    global math
    math="addition"
    f_numb=int(first_number)
    e.delete(0,END)
def Button_equals():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":# if statements to make it easy for the equal button take choice
        e.insert(0,f_numb+int(second_number))
    elif math=="subtraction":
        e.insert(0,f_numb-int(second_number))
    elif math=="multiplication":
        e.insert(0,f_numb*int(second_number))
    else:
        e.insert(0,f_numb/int(second_number))
#giving the buttons an arithmentic role
def Button_subtraction():
    first_number=e.get()
    global f_numb
    global math
    math="subtraction"
    f_numb=int(first_number)
    e.delete(0,END)
def Button_multiplication():
    first_number=e.get()
    global f_numb
    global math
    math="multiplication"
    f_numb=int(first_number)
    e.delete(0,END)
def Button_division():
    first_number=e.get()
    global f_numb
    global math
    math="division"
    f_numb=int(first_number)
    e.delete(0,END)
# creating the buttons of the the calculor
Button_1=Button(root,text="1",padx=40,pady=20,command=lambda: Button_add(1))
Button_2=Button(root,text="2",padx=40,pady=20,command=lambda: Button_add(2))
Button_3=Button(root,text="3",padx=40,pady=20,command=lambda: Button_add(3))
Button_4=Button(root,text="4",padx=40,pady=20,command=lambda: Button_add(4))
Button_5=Button(root,text="5",padx=40,pady=20,command=lambda: Button_add(5))
Button_6=Button(root,text="6",padx=40,pady=20,command=lambda: Button_add(6))
Button_7=Button(root,text="7",padx=40,pady=20,command=lambda: Button_add(7))
Button_8=Button(root,text="8",padx=40,pady=20,command=lambda: Button_add(8))
Button_9=Button(root,text="9",padx=40,pady=20,command=lambda: Button_add(9))
Button_0=Button(root,text="0",padx=40,pady=20,command=lambda: Button_add(0))
Buttonadd=Button(root,text="+",padx=39,pady=20,command=Button_addition)
Button_subtract=Button(root,text="-",padx=40,pady=20,command=Button_subtraction)
Button_multiply=Button(root,text="x",padx=40,pady=20,command=Button_multiplication)
Button_divid=Button(root,text="/",padx=40,pady=20,command=Button_division)
Button_equal=Button(root,text="=",padx=91,pady=20,command=Button_equals)
Button_clear=Button(root,text="clear",padx=79,pady=20,command=clear)
#putting the buttons on the screen
Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_0.grid(row=4,column=0)
Buttonadd.grid(row=5,column=0)
Button_clear.grid(row=4,column=1,columnspan=2)
Button_equal.grid(row=5,column=1,columnspan=2)
Button_subtract.grid(row=6,column=0)
Button_divid.grid(row=6,column=1)
Button_multiply.grid(row=6,column=2)


root.mainloop()