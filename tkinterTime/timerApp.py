import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()
        self.startButton = tk.Button(self,text='Start',command=self.quit)
        self.startButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()