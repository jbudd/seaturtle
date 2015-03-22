import Tkinter as tk
from motor_functions import *

class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.forward = False
        self.back = False
        self.degree = 0
        self.direction = 1

    def keyPressed(self,event):
        if event.keysym == 'Escape':
            root.destroy()
        elif event.keysym == 'd':
            self.right = True
        elif event.keysym == 'a':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True
        elif event.keysym == 'Down':
            self.down = True
        elif event.keysym == 'w':
            self.forward = True
        elif event.keysym == 's':
            self.back = True

    def keyReleased(self,event):
        if event.keysym == 'd':
            self.right = False
        elif event.keysym == 'a':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
        elif event.keysym == 'Down':
            self.down = False
        elif event.keysym == 'w':
            self.forward = False
        elif event.keysym == 's':
            self.back = False

    def task(self):
        if self.right:
            print 'Right'
            turn_right(70)
        elif self.left:
            print 'Left'
            turn_left(70)
        elif self.up:
            print 'up'
            self.direction = 1
            if degree < 72:
                set_speed_gear(70)
        elif self.down:
            print 'Down'
        elif self.forward:
            print 'forward'
            move(70)
        elif self.back:
            print 'back'
            move(-70)
        root.after(20,self.task)
    
    def increment(channel):
        self.degree += 18*self.direction
    
    GPIO.add_event_detect(ENCODER, GPIO.FALLING, callback = increment, bouncetime = 200)



application = App()
root = tk.Tk()
print( "Press arrow key (Escape key to exit):" )

root.bind_all('<Key>', application.keyPressed)
root.bind_all('<KeyRelease>', application.keyReleased)
root.after(20,application.task)

root.mainloop()