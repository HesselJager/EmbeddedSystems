import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas import read_csv


plt.style.use('fivethirtyeight')


def animate(i):
    data = read_csv('test_data.csv')

    x = data['0']
    y1 = data['1']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()