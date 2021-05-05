import pymysql

db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'jyhoon94',
    passwd = 'Zpflrjs94!',
    db = 'dan_db',
    charset='utf8'
)

sql = """
    create table dab_db (
        user_id int unsigned not null auto_increment,
        user_email varchar(100) not null,
        blog_id char(4)
        primary key(user_id)
    )
"""
dan_db = db_conn.cursor()
dan_db.execute('show tables;')

