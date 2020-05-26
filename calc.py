
from tkinter import *

root = Tk()
root.title("Basic Calculator")


e = Entry(root, width=40, borderwidth=3, bg="#9f97c9")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# e.insert(0, "enter your name : ")
def butClick(num):
#     e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    
def butClear():
    e.delete(0, END)
    
def butAdd():
   n1 = e.get()
   global fnum 
   global math
   math = "addition"
   fnum = int(n1)
   e.delete(0, END)
   
def butEqual():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, fnum + int(n2))
        
    elif math == "subtraction":
        e.insert(0, fnum - int(n2))
        
    elif math == "multiplication":
        e.insert(0, fnum * int(n2))
        
    elif math == "division":
        e.insert(0, fnum / int(n2))
        
        
        

def butSub():
    n1 = e.get()
    global fnum 
    global math
    math = "subtraction"
    fnum = int(n1)
    e.delete(0, END)
   

def butMul():
    n1 = e.get()
    global fnum 
    global math
    math = "multiplication"
    fnum = int(n1)
    e.delete(0, END)
   

def butDiv():
    n1 = e.get()
    global fnum 
    global math
    math = "division"
    fnum = int(n1)
    e.delete(0, END)
       

but1 = Button(root, text="1", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(1))
but2 = Button(root, text="2", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(2))
but3 = Button(root, text="3", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(3))
but4 = Button(root, text="4", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(4))
but5 = Button(root, text="5", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(5))
but6 = Button(root, text="6", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(6))
but7 = Button(root, text="7", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(7))
but8 = Button(root, text="8", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(8))
but9 = Button(root, text="9", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(9))
but0 = Button(root, text="0", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=lambda: butClick(0))
butadd = Button(root, text="+", padx=39, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=butAdd)
butequal= Button(root, text="=", padx=87, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=butEqual)
butclear = Button(root, text="Clear", padx=76, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=butClear)
butsub = Button(root, text="-", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=butSub)
butmul = Button(root, text="*", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=butMul)
butdiv = Button(root, text="/", padx=40, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=butDiv)

exit = Button(root, text="Click here to QUIT !! ", padx=84, pady=20, activebackground="#ccbc9b", activeforeground="blue", command=root.quit)


#put buttons on screen
but1.grid(row=3, column=0)
but2.grid(row=3, column=1)
but3.grid(row=3, column=2)
but4.grid(row=2, column=0)
but5.grid(row=2, column=1)
but6.grid(row=2, column=2)
but7.grid(row=1, column=0)
but8.grid(row=1, column=1)
but9.grid(row=1, column=2)
but0.grid(row=4, column=0)
butsub.grid(row=5, column=0)
butdiv.grid(row=5, column=1)
butmul.grid(row=5, column=2)
butadd.grid(row=6, column=0)
butequal.grid(row=4, column=1, columnspan=2)
butclear.grid(row=6, column=1, columnspan=2)
exit.grid(row=7, column=0, columnspan=3)








root.mainloop()