# import mysql.connector


# def connect():
#     mydb = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         passwd='')
#     # auth_plugin='mysql_native_password'
#     cursor = mydb.cursor()
#     return cursor, mydb


import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=''
        # auth_plugin='mysql_native_password'
    )
    cursor = mydb.cursor()
    return cursor, mydb

