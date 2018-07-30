import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import csv


numberOfRays = 571
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0,60000)

data = np.random.rand(numberOfRays)*10000
theta = np.linspace(0,3.31613, num=571)
l,  = ax.plot([],[])

def update(i):
    global data
    row = rows[i:i+1]
    l.set_data(theta, row)
    print(i)
    return l,

with open('/home/aleksandr/Documents/firstmeasurement1.csv', newline='') as File:
    reader = csv.reader(File)
    rows = list(reader)
ani = animation.FuncAnimation(fig, update, frames=4015, interval=100, blit=True)
plt.show()