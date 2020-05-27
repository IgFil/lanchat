#!/usr/bin/env python
import cgi
import sqlite3
from time import localtime, strftime

time = strftime("%H:%M:%S", localtime())
name = "host"
form = cgi.FieldStorage()
message = form.getfirst("message")
conn = sqlite3.connect("chat_database.db")
conn.text_factory = str
cursor = conn.cursor()
cursor.execute("INSERT INTO chat (title, text_message, time) VALUES (?,?,?)", (name, message, time))
conn.commit()
print("Content-type: text/html\n")


