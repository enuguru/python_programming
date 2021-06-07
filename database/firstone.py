
import sqlite3

conn = sqlite3.connect("training.db")

c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT," +
             "temperature REAL,date TEXT)")

conn.commit()
c.close()
conn.close()


