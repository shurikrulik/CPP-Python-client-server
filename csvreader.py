import csv
import math
import itertools
from matplotlib import pyplot as plt
from matplotlib import animation

def polarToDecart(f, r):
    decartCoordinates={"x":0, "y":0}
    decartCoordinates['x']=r*math.cos(f)
    decartCoordinates['y']=r*math.sin(f)
    return decartCoordinates


def init():
    line.set_data([], [])
    return line,

def animate(it):
    for row in rows[it-1:it]:
        for i in range(571):
            if row[i] =="":
                row[i]=0
            coordinates = polarToDecart(i/3, int(row[i]))
            x = coordinates['x']
            y = coordinates['y']
            line.set_data(x, y)
            print(x,y)
    return line,

with open('/home/aleksandr/Documents/lastmeasurement.csv', newline='') as File:
    reader = csv.reader(File)
    rows = list(reader)
    fig = plt.figure()
    ax = plt.axes(xlim=(-100000, 100000), ylim=(-100000, 100000))
    line, = ax.plot([], [], lw=2)
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=3796, interval=100)
    anim.save('basic_animation.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
    plt.show()
