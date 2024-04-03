from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

plt.rcParams["toolbar"] = "None"

x_len = 30
y_range = [0, 1.5]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = list(range(0, x_len))
ys= [0]* x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys)

plt.title("Current vs Time")
plt.xlabel("Time")
plt.ylabel("Current")

def animate(i, ys):
    try:
        f = open("DataCollector.txt", "r")
        current = float(f.read())
        ys.append(current)
    except Exception as e:
        print(e)
    ys = ys[-30:]
    line.set_ydata(ys)
    return line,

def main():
    ani = animation.FuncAnimation(fig, animate, 
                                  frames=range(1, 2), 
                                  fargs=(ys,), 
                                  cache_frame_data=False, interval=500, 
                                  blit=True)
    plt.show()
    

if __name__ == "__main__":
    main()
