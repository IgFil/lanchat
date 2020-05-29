#!/usr/bin/env python

import cgi
import sqlite3
form = cgi.FieldStorage()
id = form.getfirst("id")
conn = sqlite3.connect("chat_database.db")
cursor = conn.cursor()
messages = cursor.execute("SELECT * FROM chat")
conn.commit()
print("Content-type: text/html\n")
if messages != "":
    for message in messages:
        print('<p class = "message" id='+str(message[0])+'>'+message[1]+' || ' + message[2] + ' || ' + message[3] + '</p>')



