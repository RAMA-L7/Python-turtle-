import calendar

from tkinter import *

cal=calendar.calendar(2022)

root= Tk()

root.title("2022 calendar")

c=Label(root, text=cal, font='small 5',bg='sky blue')
c.pack()

root.mainloop()

