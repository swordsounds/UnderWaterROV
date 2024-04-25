import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
plt.rcParams['axes.facecolor'] = '(0.34,0.34,0.34,1)'
plt.rcParams['axes.edgecolor'] = '(0.167,0.173,0.178,1)'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['lines.color'] = '(0, 0, 0.78, 1)'
plt.rcParams["toolbar"] = "None"


fig, axes = plt.subplots(figsize=(8, 4), nrows=2, ncols=4)
fig.set_facecolor((0.167,0.173,0.178,1))

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value'][-30:]
    y1 = data['total_1'][-30:]
    y2 = data['total_2'][-30:]
    y3 = data['total_3'][-30:]
    y4 = data['total_4'][-30:]
    y5 = data['total_5'][-30:]
    y6 = data['total_6'][-30:]
    y7 = data['total_7'][-30:]
    y8 = data['total_8'][-30:]
    # plt.cla()
    axes[0,0].cla()
    axes[0,1].cla()
    axes[0,2].cla()
    axes[0,3].cla()
    axes[1,0].cla()
    axes[1,1].cla()
    axes[1,2].cla()
    axes[1,3].cla()
    
    axes[0, 0].plot(x, y1, label='Motor 1')
    axes[0, 1].plot(x, y2, label='Motor 2')
    axes[0, 2].plot(x, y3, label='Motor 3')

    axes[1, 0].plot(x, y4, label='Motor 4')
    axes[1, 1].plot(x, y5, label='Motor 5')
    axes[1, 2].plot(x, y6, label='Motor 6')

    axes[0, 3].plot(x, y7, label='Depth of VPF')
    axes[1, 3].plot(x, y8, label='Temp. Of Inner')
    
    plt.tight_layout()

def main():
    ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()