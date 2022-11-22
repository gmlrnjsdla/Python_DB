from bs4 import BeautifulSoup

html = '<h1 id="title">한빛</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'
soup = BeautifulSoup(html,'html.parser')
print(soup.prettify())
a_tags = soup.find_all("a")

for a_tag in a_tags:
    print(a_tag.attrs['href']," : ", a_tag.string)

title = soup.find(id="title")
print(title.string)

li_list = soup.select("#title")
print(li_list)