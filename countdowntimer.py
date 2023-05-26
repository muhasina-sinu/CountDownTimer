from plyer import notification
from tkinter import messagebox
from tkinter import *
import time

window = Tk()
window.geometry("300x300")
window.title("CountDownTimer")



hours = IntVar()
minutes = IntVar()
seconds = IntVar()
times = 0




def countdowntimer():
    global times
    
    try:
        times = hours.get()*3600+ minutes.get()*60 + seconds.get()
        
        
    except:
        messagebox.showerror(message="Enter Valid Time")
        
    while times >= 0:
            
        if times >= 60:
            minute,second = divmod(times, 60)
            hour = 0
            
                
            if  minute >= 60:
                hour, minute = divmod(minute, 60)    
                     
        
            seconds.set(second)
            minutes.set(minute)
            hours.set(hour)
                
        else:
            seconds.set(times)
            minutes.set("0")   
            hours.set("0") 
                
       
        times = times-1
        window.update()
        time.sleep(1)  
        
        
def reset():
    global times 
    
    times = -1
    seconds.set("0")
    minutes.set("0")
    hours.set("0")
    



title = Label(window,text="Set the timer",font=("arial",16)).place(x=52, y=40)

hour_entry = Entry(window, textvariable=hours, justify='center', width=4).place(x=50, y=80, height=50)
minute_entry = Entry(window, textvariable=minutes, justify='center', width=4).place(x=120, y=80, height=50)
second_entry = Entry(window, textvariable=seconds, justify='center', width=4).place(x=190, y=80, height=50)


hour_label = Label(window,text="Hours").place(x=52, y=130)
minute_label = Label(window,text="Minutes").place(x=117, y=130)
second_label = Label(window,text="Seconds").place(x=186, y=130)



timer = Button(window, text= "START", width=8, fg="red", command=countdowntimer).place(x=30,y=180)
clear = Button(window, text= "RESET", width=8, command=reset).place(x=150,y=180)

window.mainloop()
