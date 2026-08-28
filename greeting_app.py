import tkinter as tk
def greet():
    name= entry.get()
    if name =="":
        label.config(text="Please Enter your name")
    else:
        label.config(text=f"hello {name}")
window = tk.Tk()
window.title("Greeting app")
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Greet me", command=greet)
button.pack()
label = tk.Label(window, text="")
label.pack()
window.mainloop()