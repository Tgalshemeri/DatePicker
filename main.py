import datetime
from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.title("PyReminder")
root.config(background="white")
root.geometry("250x250")
currentDay = datetime.date.today().day
currentMonth = datetime.date.today().month
currentYear = datetime.date.today().year
cal = Calendar(root, font='Arial 10 bold',
               selectmode='day', year=currentYear,
               month=currentMonth, day=currentDay, showweeknumbers=False)

cal.pack(fill='both', expand=True)


def print_sel(e):
    print(cal.selection_get())


cal.bind("<<CalendarSelected>>", print_sel)
root.resizable(False, False)
root.mainloop()
