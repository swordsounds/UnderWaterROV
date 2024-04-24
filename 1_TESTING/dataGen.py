import csv
import random
import time

x_value = 0
total_1 = 1000
total_2 = 1000
total_3 = 1000
total_4 = 1000
total_5 = 1000
total_6 = 1000
total_7 = 1000
total_8 = 1000

fieldnames = ['x_value', 'total_1', 'total_2', 'total_3', 'total_4', 'total_5', 'total_6', 'total_7', 'total_8']

with open('data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    

def main():

    global x_value, total_1, total_2, total_3, total_4, total_5, total_6, total_7, total_8

    while True:

        with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "x_value": x_value,
                "total_1": total_1,
                "total_2": total_2,
                "total_3": total_3,
                "total_4": total_4,
                "total_5": total_5,
                "total_6": total_6,
                "total_7": total_7,
                "total_8": total_8
            }

            csv_writer.writerow(info)

            x_value += 1
            total_1 = total_2 + random.randint(-6, 8)
            total_2 = total_1 + random.randint(-5, 6)
            total_3 = total_4 + random.randint(-6, 8)
            total_4 = total_3 + random.randint(-5, 6)
            total_5 = total_6 + random.randint(-6, 8)
            total_6 = total_5 + random.randint(-5, 6)
            total_7 = total_8 + random.randint(-6, 8)
            total_8 = total_7 + random.randint(-5, 6)

        time.sleep(0.25)
    
if __name__ == '__main__':
    main()