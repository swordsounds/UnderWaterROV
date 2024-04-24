import customtkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import newGraph as graph

plt.style.use('fivethirtyeight')
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['r'])
plt.rcParams["toolbar"] = "None"


fig, axes = plt.subplots(figsize=(8, 4), nrows=2, ncols=3)

def switch_event():
    print(switch_var.get())

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    y3 = data['total_3']
    y4 = data['total_4']
    y5 = data['total_5']
    y6 = data['total_6']

    plt.cla()

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

    frame_canvas = customtkinter.CTkFrame(height=468, width=968, master=root)
    frame_canvas.grid(row=0, column=0, padx=20, pady=20)
    
    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.1, rely=0.075)
    
    ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

    tabview = customtkinter.CTkTabview(height=900, master=frame_tabview)
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