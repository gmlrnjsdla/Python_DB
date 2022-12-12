import csv

fin = open('c:/FileIO/incheon.csv', 'r')
data = csv.reader(fin)
header = next(data)
print(header)

high = -999
low = 999
dayR = -999
dayHigh = ''
dayLow = ''
tempR = 0

for row in data:
    tempH = row[4]
    tempL = row[3]
    if(tempH==''):
        continue

    if (tempL == ''):
        continue

    tempH = float(tempH)
    tempL = float(tempL)
    tempR = tempH - tempL

    if(tempR > dayR): # 일교차
        dayR = tempR
        day = row[0]

    if(high < tempH): # 최고 기온
        high = tempH
        dayHigh = row[0]

    if (low > tempL): # 최저기온
        low = tempL
        dayLow = row[0]

print('최고기온', high, '도 입니다.(%s)'%dayHigh) #최고기온
print('최저기온', low, '도 입니다.(%s)'%dayLow) #최고기온
print('최대 일교차는', dayR, '도 입니다.(%s)'%day) #최고기온

fin.close()