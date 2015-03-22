import curses
#init the curses screen
stdscr = curses.initscr()
#use cbreak to not require a return key press
curses.cbreak()
print "press q to quit"
quit=False
# loop
while quit !=True:
   c = stdscr.getch()
   print curses.keyname(c),
   if curses.keyname(c)=="q" :
      quit=True

curses.endwin()