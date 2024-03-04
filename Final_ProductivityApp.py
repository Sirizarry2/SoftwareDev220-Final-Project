import tkinter as Tk
from tkinter import *
import time
from tkinter import messagebox

##Main window of Productivity App setup
window = Tk()
window.title("Productivity App")
window.geometry("500x500")


#Creating label widgets
appTitle = Label(window, text = "Productivity App")
appTitle.place(x= 220, y= 50, anchor= CENTER)


#Function for TO DO LIST button on main window
def switch(): 
    toDoList = Label(window)
    toDoList.place()
    
#Function for TIMER button on main window
def timer():
    timer_main = Label(window)
    timer_main.place()
    
 #Timer window setup
    clockwindow = Tk()
    clockwindow.title("Timer Countdown")
    clockwindow.geometry("500x500")

    #Creating label widgets
    timerTitle = Label(clockwindow, text = "Timer")
    timerTitle.place(x= 220, y= 100, anchor= CENTER)

    #Variables that show the time
    hour = StringVar()
    minute = StringVar()
    second = StringVar()

    #Setting default values for time variables
    hour.set("00")
    minute.set("00")
    second.set("00")

    #Take user input
    hourEntry = Entry(clockwindow, width=3, textvariable=hour)
    hourEntry.place(x= 170, y= 180, anchor= CENTER)

    minuteEntry = Entry(clockwindow, width=3, textvariable=minute)
    minuteEntry.place(x= 220, y= 180, anchor= CENTER)

    secondEntry = Entry(clockwindow, width=3, textvariable=second)
    secondEntry.place(x= 270, y= 180, anchor= CENTER)
        
    

    #Function of Timer button
    def myClick(): #Command for inputted data for the Timer
        try:  ##Converting time entered
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            messagebox.showerror("Error", "Enter a valid integer")
            return
        
        while temp >-1:
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins > 60:
                hours, mins = divmod(mins, 60)
            
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
        
            #Updating the time
            clockwindow.update()
            time.sleep(1)
        
            #MessageBox for the "Timer Stopped"
            if (temp == 0):
                messagebox.showinfo("", "Timer Stopped")
            temp -= 1
        
        
    #Button to enter time on Timer window
    timer = Button(clockwindow, text= "Enter", command= myClick)
    timer.place(x= 220, y= 220, anchor= CENTER)

    #Button to switch to the To DO List from Timer window
    toDoList = Button(clockwindow, text= "To Do List", command= switch)
    toDoList.place(x= 0, y= 0 )
    

#Button on Main window for TO DO LIST
toDoList = Button(window, text= "To Do List", command= switch)
toDoList.place(x= 220, y= 180, anchor= CENTER)

#Button on main window for TIMER
timer_main = Button(window, text= "Timer", command=timer)
timer_main.place(x=220, y= 220, anchor= CENTER )



window.mainloop()
