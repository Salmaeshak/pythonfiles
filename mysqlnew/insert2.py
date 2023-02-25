import pymysql
id = int(input('enter the Id:'))
na = input('enter the name:')
ag = int(input('enter the age:'))
mark = int(input('enter the mark:'))
db = pymysql.connect(host='localhost',user='root',password='Salma@eshak$786',database='nov_test')
mycursor = db.cursor()
sql = 'insert into t1 values(%s,%s,%s,%s)'
val = (id,na,ag,mark)
mycursor.execute(sql,val)
db.commit()
print('inserted')

