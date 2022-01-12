import tkinter as tk 

window = tk.Tk()
lbl = tk.Label(master = window, text = "Your name:")
lbl.grid(row = 0, column = 0, sticky = "e")
name = tk.Entry()
name.grid(row = 0, column = 1, sticky = "w")
lbl2 = tk.Label(master = window)
lbl2.grid(row = 1, column = 0, columnspan = 2, sticky = "w")
def update_label():
	lbl2["text"] = "Hello {}".format(name.get())
btn = tk.Button(master = window, text = "update", command = update_label)
btn.grid(row = 2, column = 0, columnspan = 2, sticky = "w")
window.mainloop()