import pymysql
con = pymysql.connect(host='localhost', user='root', password='1234', db='bibledb', charset='utf8')
cur = con.cursor()

fin = open('c:/Fileio/bible.txt', 'r')
full = ['창세기','출애굽기','레위기','민수기','신명기','여호수아','사사기','룻기','사무엘상','사무엘하','열왕기상','열왕기하','역대상','역대하','에스라','느헤미야','에스더','욥기','시편','잠언','전도서','아가','이사야','예레미야','예레미야애가','에스겔','다니엘','호세아','요엘','아모스','오바댜','요나','미가','나훔','하박국','스바냐','학개','스가랴','말라기','신약성경','성경책 이름','마태복음','마가복음','누가복음','요한복음','사도행전','로마서','고린도전서','고린도후서','갈라디아서','에베소서','빌립보서','골로새서','데살로니가전서','데살로니가후서','디모데전서','디모데후서','디도서','빌레몬서','히브리서','야고보서','베드로전서','베드로후서','요한1서','요한1서','요한2서','요한2서','요한3서','요한3서','유다서','요한계시록']
abbr = ['창','출','레','민','신','수','삿','룻','삼상','삼하','왕상','왕하','대상','대하','스','느','에','욥','시','잠','전','아','사','렘','애','겔','단','호','욜','암','옵','욘','미','나','합','습','학','슥','말','','','마','막','눅','요','행','롬','고전','고후','갈','엡','빌','골','살전','살후','딤전','딤후','딛','몬','히','약','벧전','벧후','요일','요1','요이','요2','요삼','요3','유','계']

lines = fin.readlines()

for line in lines:
    idxColon = line.index(':')
    idxSpace = line.index(' ')

    if line[1].isnumeric():
        book = line[0:1]
        chapter = line[1:idxColon]
    else:
        book = line[0:2]
        chapter = line[2:idxColon]

    verse = line[idxColon+1:idxSpace]
    content = line[idxSpace+1:]
    content = content.replace("\'","&#39;")
    index = abbr.index(book)


    sql = 'INSERT INTO bibletbl VALUES(null,"'+full[index]+'","'+chapter+'","'+verse+'","'+content+'")';
    print(sql)
    cur.execute(sql)
    con.commit()

fin.close()
con.close()

