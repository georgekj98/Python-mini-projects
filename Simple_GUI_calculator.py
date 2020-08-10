from tkinter import *

root = Tk()
root.title("GUI calculator")
root.iconbitmap("Calculator.ico")

#Defining the entry box
e = Entry(root, width = 50 ,borderwidth = 5)
e.grid(row = 0, column = 0,columnspan = 4, padx = 10, pady = 10)

# Defining a memory variable
mem_var = NONE
prev_operator =''


def click_clear():
    global prev_operator
    global mem_var
    mem_var = NONE
    prev_operator =''
    e.delete(0, END)


def mem_change():
    if e.get() == "":
        return (NONE, False)
    else:
        num = float(e.get())
    e.delete(0, END)
    global mem_var
    global prev_operator
    if mem_var == NONE:
        mem_var = num
        return (num, False)
    else:
        return (num, True)

def click_add():
    num, flag = mem_change()
    if flag:
        global mem_var
        mem_var += float(num)
    global prev_operator
    prev_operator = '+'

def click_sub():
    if e.get() == "":
        e.insert(0,'-')
    else:
        num, flag = mem_change()
    if flag:
        global mem_var
        mem_var -= float(num)
    global prev_operator
    prev_operator = '-'

def click_mul():
    num, flag = mem_change()
    if flag:
        global mem_var
        mem_var *= float(num)
    global prev_operator
    prev_operator = '*'

def click_div():
    num, flag = mem_change()
    if flag:
        global mem_var
        mem_var /= float(num)
    global prev_operator
    prev_operator = '/'

def click_equals():
    global prev_operator
    global mem_var

    if prev_operator == '+':
        click_add()
    if prev_operator == '-':
        click_sub()
    if prev_operator == '*':
        click_mul()
    if prev_operator == '/':
        click_div()

    e.delete(0, END)
    e.insert(0,mem_var)
    mem_var = NONE
    # prev_operator = '='




def click_func(inp):
    text = e.get()
    e.delete(0,END)
    e.insert(0, text + str(inp))

#Defining the buttons
but_1 = Button(text="1",padx = 40, pady = 20,  command = lambda: click_func(1))
but_2 = Button(text="2",padx = 40, pady = 20,  command = lambda: click_func(2))
but_3 = Button(text="3",padx = 40, pady = 20,  command = lambda: click_func(3))
but_4 = Button(text="4",padx = 40, pady = 20,  command = lambda: click_func(4))
but_5 = Button(text="5",padx = 40, pady = 20,  command = lambda: click_func(5))
but_6 = Button(text="6",padx = 40, pady = 20,  command = lambda: click_func(6))
but_7 = Button(text="7",padx = 40, pady = 20,  command = lambda: click_func(7))
but_8 = Button(text="8",padx = 40, pady = 20,  command = lambda: click_func(8))
but_9 = Button(text="9",padx = 40, pady = 20,  command = lambda: click_func(9))
but_0 = Button(text="0",padx = 40, pady = 20,  command = lambda: click_func(0))
but_plus = Button(text="+",padx = 39, pady = 20,  command = click_add )
but_sub = Button(text="-",padx = 39, pady = 20,  command = click_sub )
but_mul = Button(text="*",padx = 39, pady = 20,  command = click_mul )
but_div = Button(text="/",padx = 39, pady = 20,  command = click_div )
button_equal = Button(text = "=",padx = 39, pady =20,  command = click_equals)
button_clear = Button(text = "AC",padx = 35, pady =20,  command = click_clear)


but_1.grid(row = 3, column = 0)
but_2.grid(row = 3, column = 1)
but_3.grid(row = 3, column = 2)
but_4.grid(row = 2, column = 0)
but_5.grid(row = 2, column = 1)
but_6.grid(row = 2, column = 2)
but_7.grid(row = 1, column = 0)
but_8.grid(row = 1, column = 1)
but_9.grid(row = 1, column = 2)

but_plus.grid(row = 1, column = 3)
but_sub.grid(row = 2, column = 3)
but_mul.grid(row = 3, column = 3)

but_div.grid(row = 4, column = 3)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row = 4, column = 1)
but_0.grid(row = 4, column = 0)

root.mainloop()
