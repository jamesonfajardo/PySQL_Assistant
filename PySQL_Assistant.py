class MYSQL_DBH:
    def __init__(this, __SQL_Q=None, __SQL_QV=None, __SQL_DB=None):
        this.sql_q = __SQL_Q
        this.sql_qv = __SQL_QV
        this.sql_db = __SQL_DB

    def DB_Query(this):
        import mysql.connector
        import re
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            db=this.sql_db
        )
        dbc = mydb.cursor()
        if (re.search('^create database', this.sql_q, re.IGNORECASE)):
            dbc.execute(this.sql_q, this.sql_qv)
            queryNotif = 'Database Created'

        # CREATE TABLE
        elif (re.search('^create table', this.sql_q, re.IGNORECASE)):
                dbc.execute(this.sql_q, this.sql_qv)
                queryNotif = 'Table Created'

        # INSERT
        elif (re.search('^insert into', this.sql_q, re.IGNORECASE)):

            if (type(this.sql_qv) == tuple):
                dbc.execute(this.sql_q, this.sql_qv)
                queryNotif = '1 record inserted, ID: ' + str(dbc.lastrowid)

            elif (type(this.sql_qv) == list):
                dbc.executemany(this.sql_q, this.sql_qv)
                queryNotif = str(dbc.rowcount) + ' records inserted'

        # SELECT
        elif (re.search('^select', this.sql_q, re.IGNORECASE)):
            dbc.execute(this.sql_q, this.sql_qv)
            queryNotif = dbc.fetchall()

        # UPDATE QUERY
        elif (re.search('^update', this.sql_q, re.IGNORECASE)):
            dbc.execute(this.sql_q, this.sql_qv)
            queryNotif = str(dbc.rowcount) + ' record(s) updated'

        # DELETE
        elif (re.search('^delete from', this.sql_q, re.IGNORECASE)):
            dbc.execute(this.sql_q, this.sql_qv)
            queryNotif = str(dbc.rowcount) + ' record(s) deleted'

        # TRUNCATE
        elif (re.search('^truncate table', this.sql_q, re.IGNORECASE)):
            dbc.execute(this.sql_q, this.sql_qv)
            queryNotif = 'Table truncated'

        # DROP TABLE
        elif (re.search('^drop table', this.sql_q, re.IGNORECASE)):
                dbc.execute(this.sql_q, this.sql_qv)
                queryNotif = 'Table deleted'

        # DROP DATABASE
        elif (re.search('^drop database', this.sql_q, re.IGNORECASE)):
                dbc.execute(this.sql_q, this.sql_qv)
                queryNotif = 'Database deleted'

        # OTHERS NOT COVERED
        else:
            dbc.execute(this.sql_q, this.sql_qv, re.IGNORECASE)
            queryNotif = 'Query Success'

        mydb.commit()

        return queryNotif

# Some notes:
# -> Always use placeholders
# -> Use tuple when using placeholders(%s)
