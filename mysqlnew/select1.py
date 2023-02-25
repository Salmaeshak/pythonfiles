import pymysql
id = int(input("enter the id:"))
db = pymysql.connect(host='localhost',user='root',password='Salma@eshak$786',database='nov_test')
con = db.cursor()
sql = 'select * from t1 where id =%d'%id
con.execute(sql)
i = con.fetchone()
id = i[0]
na = i[1]
ag = i[2]
print(f'id = {id},name={na},age = {ag}')


# import pymysql
# db = pymysql.connect(host='localhost',user='root',password='Salma@eshak$786',database='nov_test')
# con = db.cursor()
# sql = 'select * from t1 '
# con.execute(sql)
# data = con.fetchall()
# #print(data)
# for i in data:
#    id = i[0]
#    na = i[1]
#    ag = i[2]
#    print(f'id = {id},name={na},age = {ag}')
