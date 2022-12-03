import sqlite3
con=sqlite3.connect('test.db')
print("打开成功")
c=con.cursor()
# sql='''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
sql='''
    insert into company(id,name,age,address,salary)
        values(2,'李四',22,"盐城",5000);
'''
c.execute(sql)
con.commit()
con.close()