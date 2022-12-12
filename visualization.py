import random
import csv
import matplotlib.pyplot as plt

fin = open('c:/FileIO/seoul.csv', 'r')
data = csv.reader(fin)
header = next(data)
print(header)

high = []
low = []


for row in data:
    tempH = row[-1]
    tempL= row[-2]
    if tempH == '' or tempL == '':
        continue


    month = int(row[0].split('-')[1])

    if(6<= month <=9):
        high.append(float(tempH))
    if (month == 11 or month == 12 or month == 1 or month == 2):
        low.append(float(tempL))

plt.hist(high, color='r', bins=100)
plt.hist(low, color='b', bins=100)
plt.show()