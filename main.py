from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)


def miles_to_km():
    result = float(miles_entry.get())
    final_result = round(result * 1.609, 3)
    km_result.config(text=f"{final_result}")


miles_label = Label(text="Miles")
km_label = Label(text="Km")
equal_label = Label(text="is equal to")
km_result = Label(text="")
miles_label.grid(column=3, row=1)
km_label.grid(column=3, row=2)
equal_label.grid(column=1, row=2)
km_result.grid(column=2, row=2)

miles_entry = Entry(width=10)
miles_entry.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)

window.mainloop()
