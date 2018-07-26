import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0,100000)


theta = np.linspace(0,190, num=571)
l,  = ax.plot([],[])

def update(i):
    global data
    for row in rows[i-1:i]:
        l.set_data(theta, row )
    return l,

with open('/home/aleksandr/Documents/lastmeasurement.csv', newline='') as File:
    reader = csv.reader(File)
    rows = list(reader)
    for row in rows[1:2]:
        data = row
ani = animation.FuncAnimation(fig, update, frames=3796, interval=100, blit=True)
plt.show()
