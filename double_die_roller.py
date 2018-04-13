from button import Button
from die_view import DieView
from graphics import *

def main():
    win = GraphWin("Double Die Roller", 400, 200)
    win.setBackground( 'dark green' )
    dieView1 = DieView( win, Point( 50, 60 ), 80 )
    dieView2 = DieView( win, Point( 150, 60 ), 80 )
    rollButton = Button( win, Point( 100, 160), 100, 40, "Roll!" )
    
    while True:
        mouseClick = win.getMouse()
        if rollButton.wasClickedIn( mouseClick ):
            dieView1.roll()
            dieView2.roll()
    
main()