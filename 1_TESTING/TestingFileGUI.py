import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import matplotlib.animation as animation

plt.rcParams["toolbar"] = "None"
plt.rcParams["figure.figsize"] = [5, 4]
plt.style.use("ggplot")

x_len = 30
y_range = [0, 1.2]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = list(range(0, x_len))
ys= [0]* x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys)

plt.title("Current Over Time")
plt.xlabel("Seconds")
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

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Testing File")
        self.geometry("1080x540")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        frame = customtkinter.CTkFrame(height=420, width=500, master=self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        frame.grid(row=0, column=0, padx=20, pady=20)
        
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0)
        
        ani = animation.FuncAnimation(fig, animate, 
                                    frames=range(1, 2), 
                                    fargs=(ys,), 
                                    cache_frame_data=False, interval=500, 
                                    blit=True)

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()