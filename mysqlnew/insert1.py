import pymysql
db = pymysql.connect(host='localhost',user='root',password='Salma@eshak$786',database='nov_test')
con = db.cursor()
sqlquery ='insert into t1 values(%s,%s,%s,%s)'
val = (14,'manu',25,100)
con.execute(sqlquery,val)
db.commit()
print('inserted')
