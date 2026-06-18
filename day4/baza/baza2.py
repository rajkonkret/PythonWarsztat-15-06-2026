# with open('tekst.txt', "w") as f:
#     f.write("Dane\n")
# # context manager
import sqlite3


# __enter__, __exit__
class SqliteCM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    # wykona się zawsze
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()
