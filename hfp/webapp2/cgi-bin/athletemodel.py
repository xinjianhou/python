#!/usr/local/bin/python3

import sqlite3

db_name = 'coachdata.sqlite'

from athletelist import AthleteList


def get_names_from_store():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor();

    results = cursor.execute("""select name from athletes""")

    response = [row[0] for row in results.fetchall()]

    connection.close()

    return(response)

def get_athlete_from_id(athlete_id):

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    results = cursor.execute("""select name, dob from athletes where id=?""",(athlete_id,))
    (name,dob) = results.fetchone()

    results = cursor.execute("""select value from timing_data where athlete_id=? order by value asc""",(athlete_id,))

    data = [row[0] for row in results.fetchall()]

    response = {    'Name':name,
                    'DOB':dob,
                    'Data':data,
                    'Top3':data[0:3]}
    connection.close()

    return(response)

def get_namesID_from_store():

    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    results = cursor.execute("""select name,id from athletes""")
    response = results.fetchall()

    connection.close()

    return(response)



