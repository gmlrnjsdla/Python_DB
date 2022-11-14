import pymysql



con = pymysql.connect(host='localhost', user='root', password='1234', db='sqldb', charset='utf8')
cur = con.cursor()
sql = "DELETE FROM threetbl"

cur.execute(sql)
con.commit()
con.close()



# while(True):
#     row = cur.fetchone()
#     if row == None:
#         break
#     id = row[0]
#     name = row[1]
#     email = row[2]
#     birthYear = row[3]
#     print('%s %s %s %s'%(id,name,email,birthYear))

# con.close()

# sql = 'CREATE TABLE if not exists threeTbl(id char(), ' \
#       'userName char(15), email char(20), birthYear int)'
# cur.execute(sql)

# sql = 'INSERT INTO threetbl(id, userName,email,birthYear) VALUES("tige","홍길동","abc@gmail.com","19970811")'
#
# cur.execute(sql)
# con.commit()
# con.close()