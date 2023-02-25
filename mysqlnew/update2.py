import pymysql
db = pymysql.connect(host='localhost',user='root',password='Salma@eshak$786',database='nov_test')
id =int(input("enter the id:"))
nm = input("enter the name:")
ag = int(input("enter the age:"))
mark = int(input("enter the marks:"))
c = db.cursor()
sql = "update t1 set Name = %s,Age=%s,Mark=%s where id=%s"
val = (nm,ag,mark,id)
c.execute(sql,val)
db.commit()
print("updated")

