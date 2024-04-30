import customtkinter
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np

plt.style.use('fivethirtyeight')

params = {
         'lines.color': '(0, 0, 0.78, 1)',
         'ytick.color': 'white',
         'xtick.color': 'white',
         'axes.labelcolor': 'white',
         'axes.edgecolor': '(0.167,0.173,0.178,1)',
         'axes.facecolor': '(0.34,0.34,0.34,1)',
         'lines.linewidth': '2',
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'4',
         'ytick.labelsize':'4',
         'toolbar':  'None'
         }
plt.rcParams.update(params)

fig, axes = plt.subplots(figsize=(14, 7), nrows=2, ncols=4)
fig.set_facecolor((0.167,0.173,0.178,1))
    

def animate(i):
    data = pd.read_csv('data.csv')
    x_ticks = np.arange(0, 2, 10) #data['x_value'][-2:]
    x_special = data['x_value']
    x = data['x_value'][-10:]
    y1 = data['total_1'][-10:]
    y2 = data['total_2'][-10:]
    y3 = data['total_3'][-10:]
    y4 = data['total_4'][-10:]
    y5 = data['total_5'][-10:]
    y6 = data['total_6'][-10:]

    y7 = data['total_7']
    y8 = data['total_8']

    plt.cla()

    axes[0,0].cla()
    axes[0,1].cla()
    axes[0,2].cla()
    axes[0,3].cla()
    axes[1,0].cla()
    axes[1,1].cla()
    axes[1,2].cla()
    axes[1,3].cla()
    

    axes[0,3].set_xticks(x_ticks)
    axes[1,3].set_xticks(x_ticks)

    axes[0,0].set_ylabel('Current (a)')
    axes[0,1].set_ylabel('Current (a)')
    axes[0,2].set_ylabel('Current (a)')
    axes[0,3].set_ylabel('Temperature (C)')
    axes[1,0].set_ylabel('Current (a)')
    axes[1,1].set_ylabel('Current (a)')
    axes[1,2].set_ylabel('Current (a)')
    axes[1,3].set_ylabel('Depth (M)')

    axes[0,0].set_xlabel('Time (s)')
    axes[0,1].set_xlabel('Time (s)')
    axes[0,2].set_xlabel('Time (s)')
    axes[0,3].set_xlabel('Time (s)')
    axes[1,0].set_xlabel('Time (s)')
    axes[1,1].set_xlabel('Time (s)')
    axes[1,2].set_xlabel('Time (s)')
    axes[1,3].set_xlabel('Time (s)')
    
    axes[0, 0].plot(x, y1, label='Motor 1')
    axes[0, 1].plot(x, y2, label='Motor 2')
    axes[0, 2].plot(x, y3, label='Motor 3')
    axes[0, 3].plot(x_special, y8, label='Temperature')
    axes[1, 0].plot(x, y4, label='Motor 4')
    axes[1, 1].plot(x, y5, label='Motor 5')
    axes[1, 2].plot(x, y6, label='Motor 6')
    axes[1, 3].plot(x_special, y7, label='Depth')

    plt.xticks(rotation=45)
    plt.tight_layout()
def thr_main(value):
    sldr_mn_lbl.configure(text=value)
def thr_one(value):
    sldr_1_lbl.configure(text=value)
def thr_two(value):
    sldr_2_lbl.configure(text=value)
def thr_three(value):
    sldr_3_lbl.configure(text=value)
def thr_four(value):
    sldr_4_lbl.configure(text=value)
def thr_five(value):
    sldr_5_lbl.configure(text=value)
def thr_six(value):
    sldr_6_lbl.configure(text=value)
def main():
    global sldr_mn_lbl, sldr_1_lbl, sldr_2_lbl, sldr_3_lbl, sldr_4_lbl, sldr_5_lbl, sldr_6_lbl
    global sldr_mn_thr, sldr_1_thr, sldr_2_thr, sldr_3_thr, sldr_4_thr, sldr_5_thr, sldr_6_thr
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.after(0, lambda:root.state('zoomed'))
    root.title("Testing File")
    root.geometry("1080x920")
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    tabview = customtkinter.CTkTabview(height=968, width=1870, master=root)
    tabview.pack(padx=20, pady=20)

    tab_1 = tabview.add("Live Graphs")
    tab_2 = tabview.add("Options")

    frame_tabview = customtkinter.CTkFrame(master=tab_2)
    frame_tabview.pack(pady=20, padx=20)
    frame_tabview.grid_rowconfigure(0, weight=1)
    frame_tabview.grid_columnconfigure(0, weight=1)
    
    sldr_mn_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_main)
    sldr_mn_thr.configure(number_of_steps=25)
    sldr_mn_thr.grid(row=0, column=0, padx=40, pady=20)
    sldr_mn_thr.set(0)

    sldr_mn_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_mn_lbl.grid(row=1, column=0, padx=40, pady=20)
    sldr_mn_lbl.configure(text='No Value')

    sldr_1_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_one)
    sldr_1_thr.configure(number_of_steps=25)
    sldr_1_thr.grid(row=0, column=1, padx=40, pady=20)
    sldr_1_thr.set(0)

    sldr_1_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_1_lbl.grid(row=1, column=1, padx=40, pady=20)
    sldr_1_lbl.configure(text='No Value')
    
    sldr_2_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_two)
    sldr_2_thr.configure(number_of_steps=25)
    sldr_2_thr.grid(row=0, column=2, padx=40, pady=20)
    sldr_2_thr.set(0)

    sldr_2_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_2_lbl.grid(row=1, column=2, padx=40, pady=20)
    sldr_2_lbl.configure(text='No Value')

    sldr_3_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_three)
    sldr_3_thr.configure(number_of_steps=25)
    sldr_3_thr.grid(row=0, column=3, padx=40, pady=20)
    sldr_3_thr.set(0)

    sldr_3_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_3_lbl.grid(row=1, column=3, padx=40, pady=20)
    sldr_3_lbl.configure(text='No Value')

    sldr_4_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_four)
    sldr_4_thr.configure(number_of_steps=25)
    sldr_4_thr.grid(row=0, column=4, padx=40, pady=20)
    sldr_4_thr.set(0)

    sldr_4_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_4_lbl.grid(row=1, column=4, padx=40, pady=20)
    sldr_4_lbl.configure(text='No Value')

    sldr_5_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_five)
    sldr_5_thr.configure(number_of_steps=25)
    sldr_5_thr.grid(row=0, column=5, padx=40, pady=20)
    sldr_5_thr.set(0)

    sldr_5_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_5_lbl.grid(row=1, column=5, padx=40, pady=20)
    sldr_5_lbl.configure(text='No Value')

    sldr_6_thr = customtkinter.CTkSlider(frame_tabview, orientation="vertical", from_=0, to= 100, command=thr_six)
    sldr_6_thr.configure(number_of_steps=25)
    sldr_6_thr.grid(row=0, column=6, padx=40, pady=20)
    sldr_6_thr.set(0)

    sldr_6_lbl = customtkinter.CTkLabel(frame_tabview, text='', font=('Helvetica', 18))
    sldr_6_lbl.grid(row=1, column=6, padx=40, pady=20)
    sldr_6_lbl.configure(text='No Value')

    canvas = FigureCanvasTkAgg(fig, master=tab_1)
    ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.025, rely=0.025)

    
    root.mainloop()
    
if __name__ == "__main__":
    main()

