import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

cursor.execute("SELECT * from timing_data ")
data = cursor.fetchone()
print(data)
