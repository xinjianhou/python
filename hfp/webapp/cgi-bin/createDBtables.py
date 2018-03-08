#! /usr/local/bin/python3
import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

cursor.execute("drop table if exists timing_data")
cursor.execute("drop table if exists athletes")

cursor.execute("""create table athletes(
	id integer primary key autoincrement unique not null,
	name text not null,
	dob date not null)""")

cursor.execute("""create table timing_data(
	athlete_id INTEGER NOT NULL,
	value TEXT NOT NULL,
	FOREIGN KEY (athlete_id) REFERENCES athletes)""")

connection.commit()
connection.close()
