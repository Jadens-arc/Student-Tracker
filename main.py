from tracker import Tracker
import tkinter as tk

root = tk.Tk()
root.geometry("350x550")

canvas = tk.Canvas(root, bg = '#4ae3b5')
canvas.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

root.mainloop()

