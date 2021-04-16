from tkinter import *

def calculate():
    input = miles_input.get()
    output = float(input) * 1.609
    output_label.config(text=output)


window = Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()