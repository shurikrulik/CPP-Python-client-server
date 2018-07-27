import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import csv


fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0,70000)

data = np.random.rand(571)*10000
theta = np.linspace(0,3.31613, num=571)
l,  = ax.plot([],[])

def update(i):
    global data
    row = rows[i:i+1]

    # for i in range(571):
    #     if row[i] =="":
    #         row[i]=0
    # data += np.add( data, row, out=data, casting="unsafe")
    l.set_data(theta, row)
    print(i)
    return l,

with open('/home/aleksandr/Documents/lastmeasurement.csv', newline='') as File:
    reader = csv.reader(File)
    rows = list(reader)
ani = animation.FuncAnimation(fig, update, frames=3305, interval=100, blit=True)
plt.show()
