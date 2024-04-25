import customtkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.transforms as mtransforms
import pandas as pd
import newGraph as graph

plt.style.use('fivethirtyeight')
plt.rcParams['axes.facecolor'] = '(0.34,0.34,0.34,1)'
plt.rcParams['axes.edgecolor'] = '(0.167,0.173,0.178,1)'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['lines.color'] = '(0, 0, 0.78, 1)'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams["toolbar"] = "None"


fig, axes = plt.subplots(figsize=(14, 8), nrows=2, ncols=3)
fig.set_facecolor((0.167,0.173,0.178,1))

def switch_event():
    print(switch_var.get())

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value'][-30:]
    y1 = data['total_1'][-30:]
    y2 = data['total_2'][-30:]
    y3 = data['total_3'][-30:]
    y4 = data['total_4'][-30:]
    y5 = data['total_5'][-30:]
    y6 = data['total_6'][-30:]

    plt.cla()

    axes[0,0].cla()
    axes[0,1].cla()
    axes[0,2].cla()
    # axes[0,3].cla()
    axes[1,0].cla()
    axes[1,1].cla()
    axes[1,2].cla()
    # axes[1,3].cla()
    
    axes[0,0].set_ylabel('Current (a)')
    axes[0,1].set_ylabel('Current (a)')
    axes[0,2].set_ylabel('Current (a)')
    # axes[0,3].set_ylabel('Temperature (C)')
    axes[1,0].set_ylabel('Current (a)')
    axes[1,1].set_ylabel('Current (a)')
    axes[1,2].set_ylabel('Current (a)')
    # axes[1,3].set_ylabel('Depth (M)')

    axes[0,0].set_xlabel('Time (s)')
    axes[0,1].set_xlabel('Time (s)')
    axes[0,2].set_xlabel('Time (s)')
    # axes[0,3].set_xlabel('Time (s)')
    axes[1,0].set_xlabel('Time (s)')
    axes[1,1].set_xlabel('Time (s)')
    axes[1,2].set_xlabel('Time (s)')
    # axes[1,3].set_xlabel('Time (s)')

    axes[0,2].set_xticks(x, fontsize=1)
    
    axes[0, 0].plot(x, y1, label='Motor 1')
    axes[0, 1].plot(x, y2, label='Motor 2')
    axes[0, 2].plot(x, y3, label='Motor 3')
    axes[1, 0].plot(x, y4, label='Motor 4')
    axes[1, 1].plot(x, y5, label='Motor 5')
    axes[1, 2].plot(x, y6, label='Motor 6')

    

    plt.tight_layout()
    
def main():
    
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.after(0, lambda:root.state('zoomed'))
    root.title("Testing File")
    root.geometry("1080x920")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    frame_tabview = customtkinter.CTkFrame(master=root)
    frame_tabview.pack(pady=20, padx=60, fill="both", expand=True)
    frame_tabview.grid(row=0, column=1, padx=20, pady=20)

    frame_canvas = customtkinter.CTkFrame(height=968, width=1870, master=root)
    frame_canvas.grid(row=0, column=0, padx=20, pady=20)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.025, rely=0.075)
    
    ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

    tabview = customtkinter.CTkTabview(height=968, master=frame_tabview)
    tabview.pack(padx=20, pady=20)

    tab_1 = tabview.add("tab 1")
    tab_2 = tabview.add("tab 2")

    switch_var = customtkinter.StringVar(value='on')
    switch = customtkinter.CTkSwitch(tab_1, text='placeholder', command='switch_event', 
                                    variable=switch_var, onvalue='off', offvalue='on')
    switch.pack(padx=20, pady=20)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()