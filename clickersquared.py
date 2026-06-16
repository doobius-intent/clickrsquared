import tkinter as tk

window1= tk.Tk()
window1.title("Clicker Squared")
window1.geometry('1000x600')
window1.configure(bg="lightblue")
lbl = tk.Label(window1, text="WELCOME TO CLICKER SQUARED")
lbl.pack()

counter1 = 20

clickboost = 1

def buttonclicked():
    global counter1
    counter1 += clickboost
    lbl.config(text=f"Clicks: {counter1}")

button1 = tk.Button(window1,
                    text=".      _____\n.   /    __     \ \n.  |    | O |    |\n.  \    \---/    /\n.   \           /\n.     \____/",
                    command=buttonclicked,
                    activebackground="blue",
                    activeforeground="lightgray",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="heart",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial",10),
                    height=5,
                    highlightbackground="black",
                    highlightcolor="blue",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

button1.pack(side=tk.LEFT)

def upgradeclicked():
    global clickboost
    clickboost *= 2
    global counter1
    counter1 -= int(clickboost)

button2 = tk.Button(window1,
                    text="upgrade... (exponential)",
                    command=upgradeclicked,
                    activebackground="blue",
                    activeforeground="lightgray",
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="heart",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial",10),
                    height=5,
                    highlightbackground="black",
                    highlightcolor="blue",
                    highlightthickness=2,
                    justify="left",
                    overrelief="raised",
                    padx=10,
                    pady=5,
                    width=15,
                    wraplength=100)

button2.pack(side=tk.RIGHT)

def quitApp():
    window1.destroy()

exit_button = tk.Button(window1,
                   text="Exit :(",
                   fg="red",
                   command=quitApp)

exit_button.pack(side=tk.BOTTOM)

window1.mainloop()
