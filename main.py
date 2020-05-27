from http.server import HTTPServer, CGIHTTPRequestHandler
import sqlite3
try:
    conn = sqlite3.connect("chat_database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE chat (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title text, text_message text, time)")
except:
    SERVER_ADDRES = ("", 5555)
    httpd = HTTPServer(SERVER_ADDRES, CGIHTTPRequestHandler)
    httpd.serve_forever()
