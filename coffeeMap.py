import pandas as pd

CB = pd.read_csv('c:/Fileio/CoffeeBean.csv', encoding='cp949', index_col=0, header=0, engine='python')
addr = []
print(CB.head(1))
for address in CB.address:
    addr.append(str(address).split())
print(addr)

addr2 = []
for i in range(len(addr)):
    if addr[i][0] == '서울':
        addr[i][0]='서울특별시'
    elif addr[i][0] == '서울시':
        addr[i][0]='서울특별시'
    elif addr[i][0] == '부산시':
        addr[i][0] = '부산광역시'
    elif addr[i][0] == '대전시':
        addr[i][0] = '대전광역시'
    elif addr[i][0] == '경남':
        addr[i][0] = '경상남도'
    elif addr[i][0] == '충북':
        addr[i][0] = '충청북도'
    elif addr[i][0] == '경기':
        addr[i][0] = '경기도'

    addr2.append(' '.join(addr[i]))
print(addr2)

addr2 = pd.DataFrame(addr2,columns=['addr2'])
CB2 = pd.concat([CB, addr2], axis=1)
print(CB2.head(5))
CB2.to_csv('c:/Fileio/CoffeeBean2.csv', encoding='cp949', index=False)