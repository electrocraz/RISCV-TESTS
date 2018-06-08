#!/usr/bin/python


import sqlite3

connection  = sqlite3.connect('set.db')

cursor      = connection.cursor()

dropTableStatement = "DROP TABLE INST"

cursor.execute(dropTableStatement)

connection.close()
