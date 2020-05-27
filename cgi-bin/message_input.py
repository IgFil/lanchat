#!/usr/bin/env python
import cgi
import sqlite3
from time import gmtime, strftime

time = strftime("%H:%M:%S", gmtime())
name = "host"
form = cgi.FieldStorage()
message = form.getfirst("message")
conn = sqlite3.connect("chat_database.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO chat (title, text_message, time) VALUES (?,?,?)", (name, message, time))
conn.commit()
print("Content-type: text/html\n")


