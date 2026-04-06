import tkinter as tk

root = tk.Tk()

root.title("Testing GUI")
root.configure(background = 'pink')
root.minsize(250,250)
root.maxsize(1500,1500)
root.geometry("300x300+100+100")

start = tk.Label(root, text = "This is my first GUI program!", font=("Times New Roman", 30, 'bold'))
start.grid(row=0, column=0)
start.config(fg="blue", background="pink")

root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count)

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)


btn = tk.Button(root, text = "ADD", command=add)
btn.grid(row=4, column=0)
btn2 = tk.Button(root, text = "SUBTRACT", command=sub)
btn2.grid(row=4, column=1)

lbl = tk.Label(root, text = '0')
lbl.grid(row=5, column=0, columnspan=2)

close = tk.Button(root, text = "Bye", command=root.destroy)
close.grid(row=6, column=0)

root.mainloop()