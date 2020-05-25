import mysql.connector
from mysql.connector import Error


__all__ = ["conecatarNoBD"]
def conecatarNoBD():
    connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='M0dul4rinf1301',
                                            database='yathzee')
    if connection.is_connected():
        return connection
    return -1