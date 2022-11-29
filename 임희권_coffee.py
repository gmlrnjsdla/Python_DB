from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import pymysql



con = pymysql.connect(host='localhost', user='root', password='1234', db='iciDB', charset='utf8')
cur = con.cursor()

#[CODE 1]
def hollys_store():
    for page in range(1,54):
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        print(Hollys_url)
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_address = store_td[3].string
            store_phone = store_td[5].string

            sql = "INSERT INTO coffeetbl(name,address,phone) VALUES('{0}','{1}','{2}')".format(store_name,store_address,store_phone)
            cur.execute(sql)

    con.commit()
    con.close()
    return

#[CODE 0]
def main():
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store()   #[CODE 1] 호출

       
if __name__ == '__main__':
     main()
