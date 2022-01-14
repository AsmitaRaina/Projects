import calendar 
from tkinter import *

def showCalendar():
    gui=Tk()
    gui.config(background = "black")
    gui.geometry("550x600")
    gui.title("Calendar of the year")
    year = int(year_field.get())
    gui_content = calendar.calendar(year)
    calYear = Label(gui, text = gui_content, font = "Consolas 10 bold")
    calYear.grid(row = 5, column = 1, padx = 20)
    gui.mainloop()

if __name__=="__main__":
    new=Tk()
    new.config(background = "grey")
    new.title("Calendar")
    new.geometry("100x100")
    cal = Label(new, text = "CALENDAR", bg = "yellow")
    year = Label(new, text = "ENTER YEAR", bg = "dark grey")
    year_field = Entry(new)
    button = Button(new, text = "SHOW CALENDAR", fg = "black", bg = "blue", \
                command = showCalendar)
    def Exit():
        new.destroy()
    button2 = Button(new, text = "Exit", command = Exit)
    button2.grid(row = 5, column = 1)
cal.grid(row = 1, column = 1)
year.grid(row = 2, column = 1)
year_field.grid(row = 3, column = 1)
button.grid(row = 4, column = 1)
new.mainloop()
