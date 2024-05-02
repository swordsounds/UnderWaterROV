import matplotlib.pyplot as plt
import pandas as pd
import csv
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S") 


data = {
  "time": [current_time, current_time, current_time],
  "mtr1": [420, 380, 390],
  "mtr2": [420, 380, 390],
  "mtr3": [420, 380, 390],
  
}

data['time'].append(current_time)
data['mtr1'].append(500)
data['mtr2'].append(500)
data['mtr3'].append(500)

myvar = pd.DataFrame(data)

myvar.to_csv('data.csv', encoding='utf-8', index=False)

df = pd.read_csv('data.csv')

print(df)
# df = df.reset_index(drop=True)
# myvar = pd.Series(calories, index = dict(list(calories.items())[:2]))
# print(myvar)
# print(myvar.loc['mtr1'])
# print(myvar['calories'])
# print(myvar.loc[0])
# print(myvar.loc[[0,1]])

# csv_writer.writerow(myvar.loc[0])
# myvar.plot(x='time', y='current')
fig, axes = plt.subplots()

axes.plot(df['time'][-30:], df['mtr1'][-30:])
# axes = myvar['mtr1'][-30:].plot(df['time'][-30:])
# axes.set_xticklabels(x_values)
plt.show()