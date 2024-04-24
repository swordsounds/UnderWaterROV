from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

plt.rcParams["toolbar"] = "None"
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3)
fig.supxlabel("Time")
fig.supylabel("Current")

# ax = fig.add_subplot(1,1,1)




x_len = 30
y_range = [0, 1.5]
xs = list(range(0, x_len))
ys= [0]* x_len

ax1.set_ylim(y_range)
ax2.set_ylim(y_range)
ax3.set_ylim(y_range)
ax4.set_ylim(y_range)
ax5.set_ylim(y_range)
ax6.set_ylim(y_range)

line, = ax1.plot(xs, ys)
line1, = ax2.plot(xs, ys)
line2, = ax3.plot(xs, ys)
line3, = ax4.plot(xs, ys)
line4, = ax5.plot(xs, ys)
line5, = ax6.plot(xs, ys)

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
                                  blit=False)
    plt.show()
    

if __name__ == "__main__":
    main()
