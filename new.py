#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('set.db')
print "Opened database successfully";

def view_all_by_CompID(data):        
    with sqlite3.connect("set.db") as db:
        conn = db.conn()
        cursor.execute("""SELECT  NEW.id, NEW.name, NEW.freq
                       FROM NEW
                       INNER JOIN INST """)
        ViewData = conn.fetchall()
        DataTableCompAndClient([ViewData])
    db.commit()
conn.close()
