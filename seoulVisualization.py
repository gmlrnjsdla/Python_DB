import csv
import matplotlib.pyplot as plt

fin = open('c:/FileIO/seoul.csv', 'r')
data = csv.reader(fin)
header = next(data)
print(header)

high = []
low = []
years = []

for row in data:
    tempL = row[-2]
    tempH = row[-1]
    if tempL == '' or tempH == '':
        continue

    date = row[0].split('-')
    if(date[1] == '12' and date[2] == '12'):
        years.append(int(date[0]))
        high.append(float(tempH))
        low.append(float(tempL))

plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('12월 12일 기온')
plt.plot(years, high, 'r')
plt.plot(years, low, 'b')
plt.ylabel('온도(℃)')
plt.xlabel('연도')
plt.show()
fin.close()