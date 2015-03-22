import Tkinter as tk

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.w = False

    def keyPressed(self,event):
        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True
        elif event.keysym == 'Down':
            self.down = True
        elif event.keysym == 'w':
            self.w = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysym == 'Down':
            self.down = False
        elif event.keysym == 'w':
            self.w = False

    def task(self):
        if self.right:
            print 'Right'
        elif self.left:
            print 'Left'
        elif self.up:
            print 'Forward'
        elif self.down:
            print 'Down'
        elif self.w:
            print 'W'
        root.after(20,self.task)

application = App()
root = tk.Tk()
print( "Press arrow key (Escape key to exit):" )

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(20,application.task)

root.mainloop()