import sqlite3

DATABASE = 'database.db'


def get_db():
    db = sqlite3.connect(DATABASE)
    return db


def execute_db(sql):
    db = get_db()
    try:
        db.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


if __name__ == "__main__":
    execute_db("create table users (id int primary key autoincrement, email varchar(20) NOT NULL UNIQUE, pwd varchar(10) NOT NULL, active int default 0,org int NOT NULL)")
    execute_db(
        "create table org (id int primary key autoincrement, name varchar(100) NOT NULL,create_user int")
    # execute_db("insert into users(email,pwd) values ('yuanfang','123456')")

    # for user in query_db('select * from users'):
    #     print('user id='+str(user[0])+' name='+user[1])
    # u=query_db("select * from users where email='jayden.zhang@maiscrm.com'")
    # print(u[0])
