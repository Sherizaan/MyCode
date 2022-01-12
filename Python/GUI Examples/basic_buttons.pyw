import tkinter as tk
import datetime

window = tk.Tk()
message = tk.Label(text = "Hello world")
message.pack()
timeMessage = tk.Label()
timeMessage.pack()
def update_message():
	timeMessage["text"] = datetime.datetime.now()
btnimg = tk.PhotoImage(file = "ClickMe.png")
btn = tk.Button(image = btnimg, border = 0, command = update_message)
btn.pack()
window.mainloop()