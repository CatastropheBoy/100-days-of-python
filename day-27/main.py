from tkinter import *

def button_clicked():
    my_label.config(text=new_input.get())

window = Tk()
window.title("First GUI")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a label", font=("Arial", 24))
# my_label.pack()
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New text")


# Button 


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


# New Button
new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)






# Entry 

new_input = Entry(width=10)
new_input.grid(column=3, row=2)
# new_input.pack()
new_input.get()







window.mainloop()