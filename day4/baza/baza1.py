# baza danych - silnik baz danych. mechanizm przechowywania i przetwarzania baz danych
# sql
# mysql, oracle, postgres, mssql
# teradata

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_db.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłączona")
except sqlite3.Error as e:
    print("Bład podłaczenia bazy:", e)
finally:
    if sql_connection:
        sql_connection.close()
# Baza danych zostałą podłączona
