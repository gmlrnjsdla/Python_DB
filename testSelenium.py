from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time


# [CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.starbucks.co.kr/store/store_map.do"
    wd = webdriver.Chrome('./WebDriver/chromedriver.exe')

    for i in range(9460, 9484):  # 매장 수 만큼 반복
        wd.get(CoffeeBean_URL)
        time.sleep(1)  # 웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("getStoreDetail(%d)" % i)
            time.sleep(1)  # 스크립트 실행 할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            #print(soupCB.prettify())

            store_name_h2 = soupCB.select("header.titl > h6")
            store_name = store_name_h2[0].string
            print(store_name)  # 매장 이름 출력하기

            store_info = soupCB.select("div.shopArea_infoWrap > dl.shopArea_info > dd")
            store_address_list = list(store_info[0])
            store_address = store_address_list[0]
            print(store_address)
            store_phone = store_info[1].string
            result.append([i] + [store_name] + [store_address] + [store_phone])
        except:
            continue
    return


# [CODE 0]
def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)  # [CODE 1]
    print(result)

    CB_tbl = pd.DataFrame(result, columns=('num', 'store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='cp949', mode='w', index=True)


if __name__ == '__main__':
    main()