import pymysql.cursors

def main():
    conn = pymysql.connect(
        user    ='root',
        passwd  ='root',
        host    ='localhost',
        port    = 3306,
        db      ='kabu_db',
    )
    c = conn.cursor()

    # テーブルの作成
    sql = 'select * from polls_question;'
    c.execute(sql)
    print('* polls_questionテーブルの一覧を表示\n')
    for row in c.fetchall():
        print('No:', row[0], 'Content:', row[1])
main()