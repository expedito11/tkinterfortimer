from tkinter import *
import time

def Main():
    global root
  ### frame for timer for bottons, display timer ,title  
    root = Tk()
    root.title("TIMER")
    width = 700
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 3) - (width / 3)
    y = (screen_height / 3) - (height / 3)
    ### used to set the position of main window
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=700)
    Top.pack(side=TOP)
    timer = Timer(root)
    timer.pack(side=TOP)
    Bottom = Frame(root, width=700)
    Bottom.pack(side=BOTTOM)
     ### buttons for start, stop, reset, exit, command is use to action the bottons
    Start = Button(Bottom, text='START',command=timer.Start, width=10, height=3, bg = "green")
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='STOP', command=timer.Stop, width=10, height=3, bg = "red")
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='RESET', command=timer.Reset, width=10, height=3, bg = "yellow")
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='EXIT', command=timer.Exit, width=10, height=3, bg = "blue")
    Exit.pack(side=LEFT)
    Title = Label(Top, text="TIMER", font=("times new roman", 20), fg="black", bg="sky blue",width = 18)
    Title.pack(fill=X)
    root.config(bg="white")
    root.mainloop()
  ## classes of timer   
class Timer(Frame):
    ### for timer base for the buttons
    def __init__(self, parent=None, **kw): ## **kw more widget option
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()
  #  # design for timer display
    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="sky blue", bg="white")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=3, padx=3)
 ##   # setup of timer when it start running
    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
        ### the time for every lap 
    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 60)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
        
        ### for start button to run the seconds
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
            ### "stop button to cancel the running seconds and stop it
    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
        ### reset the seconds and start again
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)
    ### exit buttons to exit in the running code
    def Exit(self):
        root.destroy()
        exit()          
          
if __name__ == '__main__': Main()

