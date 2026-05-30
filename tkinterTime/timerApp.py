import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    # This isn't a real part of tkinter, just something for us to separate the things
    def createWidgets(self):
        # Starts the timer
        self.startButton = tk.Button(self,text='Start',command=self.startTimer, anchor='w')
        self.startButton.grid()
        # Pauses timer
        self.pauseButton = tk.Button(self,text='Pause',command=self.pauseTimer, anchor='center')
        self.pauseButton.grid()
        # Resets Timer
        self.resetButton = tk.Button(self,text='Reset',command=self.resetTimer, anchor='e')
        self.resetButton.grid()
        # Quits Application
        self.quitButton = tk.Button(self, text='Quit', command=self.quit, anchor='s')
        self.quitButton.grid()

    def startTimer(self):
        print("timer started!")
    
    def pauseTimer(self):
        print("timer paused ;-;")

    def resetTimer(self):
        print("timer reset")

app = Application()
app.master.title('Sample application')
app.mainloop()