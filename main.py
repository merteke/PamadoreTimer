from tkinter import *
import time



#Constants
COLORS=['ffe6e6','e1afd1','ad88c6','7469b6']
COLOR1='#ffe6e6'
COLOR2='#e1afd1'
COLOR3='#ad88c6'
COLOR4='#7469b6'
FONT_NAME="Courier"
WORK_MIN=25
SHORT_REST_MIN=5
LONG_REST_MIN=20
CHECK_MARK=[]
REPS=0
timer=None
#FUCNTIONS
def start_timer():
    global REPS,CHECK_MARK
    work_sec=WORK_MIN*60
    short_break_seconds=SHORT_REST_MIN*60
    long_break_seconds=LONG_REST_MIN*60
    REPS+=1
    if REPS%8==0:
        timer_label.config(text="Long Rest",fg=COLOR4)
        CHECK_MARK.append("✓")
        check_label.config(text=f"{len(CHECK_MARK)*"✓"}")
        count_down(long_break_seconds)
    elif REPS%2==0:
        timer_label.config(text="Short Rest",fg=COLOR4)
        CHECK_MARK.append("✓")
        check_label.config(text=f"{len(CHECK_MARK)*"✓"}")
        count_down(short_break_seconds)
    else:
        timer_label.config(text="Study",fg="green")
        count_down(work_sec)
    
    

    
    
    
    

    
    
      
def reset():
    global CHECK_MARK,REPS
    window.after_cancel(timer)
    REPS=0
    CHECK_MARK=[]
    canvas.itemconfig(timer_text,text=f"00:00")
    timer_label.config(text="Timer",bg=COLOR1,fg=COLOR4,font=(FONT_NAME,32,"bold"))
    
    
            
def count_down(count):
    canvas.itemconfig(timer_text,fill=COLOR4)
    mins=count/60
    canvas.itemconfig(timer_text,text=f"{"{:02d}".format(int(mins))}:{"{:02d}".format(count%60)}")
    if count>0:
        global timer
        if count<10:
            canvas.itemconfig(timer_text,fill="red")
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
    
            
    
    

#UI SETUP
window=Tk()
window.minsize(height=600,width=600)
window.config(bg=COLOR1)
window.title("Pamadora")

img=PhotoImage(file="circle2.png")
canvas=Canvas(window,width=300,height=300,bg=COLOR1,highlightthickness=0)
canvas.create_image(150,150,image=img)
timer_text=canvas.create_text(150,150,text="00:00",fill=COLOR4,font=(FONT_NAME,32,"bold"))



canvas.place(x=300,y=100,anchor="n")

#timer label
timer_label=Label(text="Timer",bg=COLOR1,fg=COLOR4,font=(FONT_NAME,32,"bold"))
timer_label.place(x=300,y=50,anchor="n")

#Button start-reset
button_start=Button(text="Start",bg=COLOR4,font=(FONT_NAME,12,"bold"),command=start_timer)
button_start.place(x=150,y=400,anchor="n")

button_reset=Button(text="Reset",bg=COLOR4,font=(FONT_NAME,12,"bold"),command=reset)
button_reset.place(x=450,y=400,anchor="n")

#Checkmark label
check_label=Label(bg=COLOR1,fg=COLOR4,font=(FONT_NAME,20,"bold"))
check_label.place(x=300,y=400,anchor="n")



































window.mainloop()