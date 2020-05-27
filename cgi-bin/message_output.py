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
        #print("<p id="+str(message[0])+">"+str(message[1])+" {} "+str(message[2])+"</p>")
        print("<p id="+str(message[0])+">"+str(message[1])+" || " + message[2] + "</p>")



