red="#e7305b"
pink="#e2979c"
green="#9bdeac"
yellow="#f7f5dd"
FONT_NAME="Courier"
WORK_MIN=1
SHORT_BREAK_MIN=1
LONG_BREAK_MIN=20
rep=0
timbu=None

import tkinter

import math

#python allows you to change the datatype of a variable just by assigning it a different type of value
#in python values have a type but variables dont have any type hence dynamic typic is possible which means 
#that a variable can be initialized with values of different datatype simultaneously 
#global keyword is also used when a global variable is supposed to be changed inside a function
# def uno():#this function is not making the page as responsive as it should
#     cnt=5
#     while cnt>0:
#         # pica.itemconfig(timer_text,text=f"{cnt}")
#         time.sleep(1)
#         print(f"{cnt}")
#         pica.itemconfig(timer_text,text=f"{cnt}")
#         cnt=cnt-1
# def coung(a):
#     print(a)
#     if a>0:
#         win.after(1000,coung,a-1)     
# def strt():
#     coug(5)
# def coug(c):
#     pica.itemconfig(timer_text,text=c)
#     if c>0:
#         win.after(1000,coug,c-1) 
# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()
# print("Python is " + x)
#"Python is fantastic" would be the output of the above and the global variable outside the
#function is accessed within the myfunc() and is then changed 

# print("Python is " + x)
#sequence of events
# 25 minute work-1
# 5 minute break-2
# 25 minute work-3
# 5 minute break-4
# 25 minute work-5
# 5 minute break-6
# 25 minute work-7
# 20 minute break-8
# def strt():
#     coug(5*60)
# def coug(c):
#     t_min=math.floor(c/60)
#     t_sec=c%60
#     if t_sec<10:
#         t_sec=f"0{t_sec}"
#     pica.itemconfig(timer_text,text=f"{t_min}:{t_sec}")
#     if c>0:
#         win.after(1000,coug,c-1)
# def strt():
#     global rep#global keyword is used to access 
#     while rep<=5:
#         rep+=1
#         print(rep)the variable rep within a function and then change it
def reset_lets():
    global rep#this is used to access a variable declared at the global level and is used often to change its value
    global timbu#this is used often to access a variable declared at the global level and is used often to change it but in this case it has just been invoked to be used and not to be changed
    rep=0#here rep is made zero so that if start button is clicked after the reset button,the timer starts from where it had started initially and not from where it was present before the reset
    win.after_cancel(timbu)#it is used to cancel the scheduling of a function 
    tbl.config(text="Timer")#this is used to change the text of the label tbl back to what it was
    pica.itemconfig(timer_text,text="00:00")#this is used to change the text attribute of the variable timer_text which has been initialized by invoking create_text method of pica object which is of canvas class of the tkinter module

def strt():
    global rep#global keyword is used to access a variable which has a global scope mostly to permanently change it
    rep+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if rep%8==0:#if rep divided by 8 gives 0 as remainder
        count(long_break_sec)#then count function is called and long_break_sec is passed as an argument
        tbl.config(text="Break",fg=red,font=('Courier',24,"bold"),bg=yellow)#when long_break_sec is passed as argument,the text argument is equated with "Break" word
    elif rep%2==0:#if rep divided by 2 gives 0 as remainder
        count(short_break_sec)#then count function is called which has short_break_sec as argument
        tbl.config(text="Break",fg=pink,font=('Courier',24,"bold"),bg=yellow)#the label tbl is now configured with Break as the value of tex,its color is made pink,font is adjusted and bg or background is given
    else:
        count(work_sec)#now count with argument work_sec in case above 2 conditions are not fullfilled
        tbl.config(text="Work",fg=green,font=('Courier',24,"bold"),bg=yellow)

def count(c):
    global rep#global keyword is used to access the variable having global scope,this variable can be changed with global keyword
    global timbu
    t_min=math.floor(c/60)#floor function of math module ensures that an integer less than equal to c/60 is chosen such that the minutes doesnot get rounded off and we get the exact minutes along with second
    t_sec=c%60#this is used to get seconds
    if t_sec<10:#if the counter is 6 minute 9 seconds,the timer displays 6:9 and not 6:09 hence to make it 6:09 we have to do the below operation
        t_sec=f"0{t_sec}"#now the variable is changed in accordance to dynamic typing in python which ensures that variables dont have a datatype in python,values do
    pica.itemconfig(timer_text,text=f"{t_min}:{t_sec}")#after this the item is configured as shown below
    if c>0:
        timbu=win.after(1000,count,c-1)#if c>0 then the count function is called with argument c-1 repeatedly after every 1000 ms or 1 second
    else:
        z=math.floor(rep/2)#else if c=0 then rep is divided by 2 and lowest integer value <=rep/2 is initialized to z
        o=""
        for _ in range(z):
            o+="✔"#and now for the entire range of z,"✔" keeps on getting appended to o
            check_mark.config(text=o)#lastly o is equated with text of check_mark label
        strt()#after doing all this strt() is called again for the next repetition of rep



win=tkinter.Tk()#win is an object of Tk class
win.title("Pomodoro")
win.config(padx=100,pady=100,bg=yellow)
# coung(5)

# def do_some(*yhing):
#     print(yhing)

# def do_some(a,b,c):
#     print(a)
#     print(b)
#     print(c)

# win.after(1000,do_some,3,4,5)

tbl=tkinter.Label(text="Timer",fg=green,font=('Courier',24,"bold"),bg=yellow)
tbl.grid(row=0,column=1)

pica=tkinter.Canvas(width=224,height=224,bg=yellow,highlightthickness=0)
img=tkinter.PhotoImage(file="D:\\tkinterudemytomato.png")
pica.create_image(112,112,image=img)
timer_text=pica.create_text(116,122,text="00:00",fill="white",font=('Courier',35,"bold"))
pica.grid(row=1,column=1)

start_but=tkinter.Button(text="Start",highlightthickness=0,command=strt)#highlitthickness=0 makes the line around invisible
start_but.grid(row=2,column=0)

reset_but=tkinter.Button(text="Reset",highlightthickness=0,command=reset_lets)
reset_but.grid(row=2,column=2)

check_mark=tkinter.Label(text="",fg=green,font=('Courier',10,"bold"),bg=yellow)
check_mark.grid(row=3,column=1)

win.mainloop()#this method will check for any button press movement on screen and it is the responsibilty of this to make the window more responsive1