from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 200, height = 200)

strCalculus = ''
result = ''
var = StringVar()
label = Label( tk, textvariable=var, relief=RAISED )
label.place(x=20,y=20)

def btn0():    
    global strCalculus
    strCalculus = strCalculus + "0"

    var.set(strCalculus)
    #label.pack()
    print(strCalculus)

def btn1():    
    global strCalculus
    strCalculus = strCalculus + "1"

    #canvas.create_text(10,100,text=strCalculus)
    var.set(strCalculus)
    print(strCalculus)

def btn2():
    global strCalculus
    strCalculus = strCalculus + "2"

    var.set(strCalculus)
    print(strCalculus)

def btn3():
    global strCalculus
    strCalculus = strCalculus + "3"

    var.set(strCalculus)
    print(strCalculus)

def btn4():
    global strCalculus
    strCalculus = strCalculus + "4"

    var.set(strCalculus)
    print(strCalculus)

def btn5():
    global strCalculus
    strCalculus = strCalculus + "5"

    var.set(strCalculus)
    print(strCalculus)

def btn6():
    global strCalculus
    strCalculus = strCalculus + "6"

    var.set(strCalculus)
    print(strCalculus)

def btn7():
    global strCalculus
    strCalculus = strCalculus + "7"

    var.set(strCalculus)
    print(strCalculus)

def btn8():
    global strCalculus
    strCalculus = strCalculus + "8"

    var.set(strCalculus)
    print(strCalculus)

def btn9():
    global strCalculus
    strCalculus = strCalculus + "9"

    var.set(strCalculus)
    print(strCalculus)
    
def btnPlus():
    global strCalculus
    strCalculus = strCalculus + "+"

    var.set(strCalculus)
    print(strCalculus)

def btnMinus():
    global strCalculus
    strCalculus = strCalculus + "-"

    var.set(strCalculus)
    print(strCalculus)

def btnMul():
    global strCalculus
    strCalculus = strCalculus + "*"

    var.set(strCalculus)
    print(strCalculus)

def btnDiv():
    global strCalculus
    strCalculus = strCalculus + "/"

    var.set(strCalculus)
    print(strCalculus)

def btnEqual():
    canvas.create_text(10,100,text='')
    
    global strCalculus
    global result

    try:
        result = str(eval(strCalculus))
    except ZeroDivisionError:
        print("division by zero!")
        result = "division by zero!"
    
    #result = str(eval(strCalculus))

    var.set(result)
    print(result)

    strCalculus = ''
    strCalculus = result
    print("strCalculus : %s" %strCalculus)

def btnClear():
    global strCalculus
    strCalculus = ""

    var.set(strCalculus)
    print("clear %s" %strCalculus)    

#btn1
btn1 = Button(tk, text="1", command=btn1)
#btn1.pack(side="left")
btn1.place(x=15, y=43)

#btn2
btn2 = Button(tk, text="2", command=btn2)
btn2.place(x=50, y=43)

#btn3
btn3 = Button(tk, text="3", command=btn3)
btn3.place(x=85, y=43)

#btn4
btn3 = Button(tk, text="4", command=btn4)
btn3.place(x=15, y=68)

#btn5
btn3 = Button(tk, text="5", command=btn5)
btn3.place(x=50, y=68)

#btn6
btn3 = Button(tk, text="6", command=btn6)
btn3.place(x=85, y=68)

#btn7
btn3 = Button(tk, text="7", command=btn7)
btn3.place(x=15, y=93)

#btn8
btn3 = Button(tk, text="8", command=btn8)
btn3.place(x=50, y=93)

#btn9
btn3 = Button(tk, text="9", command=btn9)
btn3.place(x=85, y=93)

#btn0
btn0 = Button(tk, text="0", command=btn0)
btn0.place(x=15, y=118)

#btnPlus
btnPlus = Button(tk, text="+", command=btnPlus)
btnPlus.place(x=120, y=43)

#btnMinus
btnMinus = Button(tk, text="-", command=btnMinus)
btnMinus.place(x=120, y=68)

#btnMul
btnMinus = Button(tk, text="*", command=btnMul)
btnMinus.place(x=120, y=93)

#btnDiv
btnMinus = Button(tk, text="/", command=btnDiv)
btnMinus.place(x=123, y=118)

#btnEqual
btnPlus = Button(tk, text="=", command=btnEqual)
btnPlus.place(x=85, y=118)

#btnClear
btnClear = Button(tk, text="C", command=btnClear)
btnClear.place(x=50, y=118)

canvas.pack() 
    
