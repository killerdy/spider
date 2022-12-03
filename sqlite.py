import sqlite3


def saveDataDB(datalist, dbpath):
    # init_db(dbpath)
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    print(len(datalist))
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
        sql = '''insert into movie(cname,ename,pic_link,rated)
        values(%s);''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        con.commit()
    con.close()


def init_db(dbpath):
    sql = '''
    create table movie(
        id integer primary key autoincrement,
        cname text,
        ename text,
        pic_link text,
        rated numeric
    );
    '''
    con = sqlite3.connect(dbpath)
    c = con.cursor()
    c.execute(sql)
    con.commit()
    con.close()


def main():
    init_db("test.db")
if __name__ == "__main__":
    main()
