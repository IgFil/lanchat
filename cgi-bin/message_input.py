#!/usr/bin/env python
import cgi
import cgitb
import sqlite3
from time import localtime, strftime
import os

cgitb.enable()

time = strftime("%H:%M:%S", localtime())

form = cgi.FieldStorage()
message = form.getfirst("message")
if message != None:
    name = form.getfirst("name")
    conn = sqlite3.connect("chat_database.db")
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat (title, text_message, time) VALUES (?,?,?)", (name, message, time))
    conn.commit()
    print("Content-type: text/html\n")


img = form.getfirst("file_img")
if img != None:
    with open(form['file_img'].filename, 'wb') as file:
        file.write(bytes(img))
        file.close
    nick = os.environ["HTTP_COOKIE"]

    name = "GlaDos"

    html = '<br><img src=../' + \
        form['file_img'].filename + ' width=300px" height="300px">'
    conn = sqlite3.connect("chat_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat (title, text_message, time) VALUES (?,?,?)", (nick, html, time))
    conn.commit()

    print("Content-type: text/html\n")
    print(nick)
