from time import sleep
from itertools import cycle
from tkinter import *

root = Tk()
root.title('TrafficLight')
can1 = Canvas(root, width=250, height=320, bg='white')
can1.pack()
oval_red = can1.create_oval(10, 10, 110, 110, fill='white')
oval_yellow = can1.create_oval(10, 110, 110, 210, fill='white')
oval_green = can1.create_oval(10, 210, 110, 310, fill='white')


class TrafficLight:
    __color = None

    def running(self, __color):
        if __color == 'red':
            can1.itemconfig(oval_red, fill='red')
            can1.itemconfig(oval_yellow, fill='white')
            can1.itemconfig(oval_green, fill='white')
        elif __color == 'yellow':
            can1.itemconfig(oval_red, fill='white')
            can1.itemconfig(oval_yellow, fill='yellow')
            can1.itemconfig(oval_green, fill='white')
        elif __color == 'green':
            can1.itemconfig(oval_red, fill='white')
            can1.itemconfig(oval_yellow, fill='white')
            can1.itemconfig(oval_green, fill='green')


TrafficLight_1 = TrafficLight()
colors = ['red', 'yellow', 'green', 'yellow']
for _ in cycle(colors):
    TrafficLight_1._TrafficLight__color = _
    TrafficLight_1.running(_)
    root.update()
    if _ == 'red' or _ == 'green':
        sleep(7)
    elif _ == 'yellow':
        sleep(2)
