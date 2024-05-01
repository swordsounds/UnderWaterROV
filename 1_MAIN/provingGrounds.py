import csv
from datetime import datetime
current=0

fieldnames = ['mtr_1']

def onCurrentChange0(self, current):
    with open('data.csv', 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            now = datetime.now()
            info = {
                "mtr_1": current 
            }
            csv_writer.writerow(info)


def main():
    onCurrentChange0(onCurrentChange0, 400)


if __name__ == '__main__':
    main()