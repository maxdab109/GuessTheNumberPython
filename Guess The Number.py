from tkinter import*
import random
from tkinter import messagebox
gtn = Tk()
gtn.geometry('700x540')
tries = 0
randomnum = random.randint(1, 100)
def start(*args):
    global tries, gg, randomnum, txt1
    tries = tries+1
    if int(gg.get())<randomnum:
        lbl3.configure(text="Higher!",bg="orange")
    elif int(gg.get())>randomnum:
        lbl3.configure(text="Lower!",bg="blue")
    else:
        lbl3.configure(text="Correct!",bg="red")
        if tries >= 0:
            messagebox.showinfo("Congrats", "It took you " + str(tries) + " tries")
    gg.delete(0, "end")

def restart():
    global tries, randomnum
    randomnum = random.randint(1, 100)
    tries = 0
    gg.delete(0, "end")
    lbl3.configure(text = "")


lbl1=Label(gtn, text = "Guess The Number Game", font=('Arial', 25))
lbl1.grid(column=0, row=0, columnspan=2)
lbl2=Label(gtn, text="This game focuses on guessing your number,\n All you have to do is guess which number has been chosem from 0-100. \n Press 'Enter' to begin.", font=('Arial', 15))
lbl2.grid(column=0, row=1, padx=20, columnspan=2)
gg=Entry(gtn, text="please write a number from 0-100", font=('Arial', 20), width=10)
gg.grid(column=0, row=2)
lbl3=Label(gtn, text="", font=('Arial', 20))
lbl3.grid(column=1, row=2)
btn4=Button(gtn, text="Exit", font=("Arial", 25), command=gtn.destroy, bg="green")
btn4.grid(column=0, row=4, columnspan=2)
btn5=Button(gtn, text="Restart", font=('Arial', 25), command=restart, bg="yellow")
btn5.grid(column=0, row=5, columnspan=2)
Generator=StringVar
gtn.bind("<Return>",start)

gtn.mainloop()