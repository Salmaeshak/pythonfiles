import pymysql
id = int(input("enter the id:"))
db = pymysql.connect(host='localhost',user='root',password='Salma@eshak$786',database='nov_test')
cr = db.cursor()
sql = 'delete from t1 where id = %d'%id
cr.execute(sql)
db.commit()
print('delete successfully')