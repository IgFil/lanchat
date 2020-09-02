from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
from time import localtime, strftime
import sqlite3
import os

UPLOAD_FOLDER = "/"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    text_message = db.Column(db.String(400), nullable=False)
    time = db.Column(db.String(100), nullable=False)


@ app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        data = request.form.to_dict()
        try:
            print(request.files)
            name = request.cookies.get('name')
            time = strftime("%H:%M:%S", localtime())
            upload_file_path = os.path.join(
                'static', os.path.basename(request.files['file_img'].filename))
            with open(upload_file_path, 'wb') as file:
                file.write(bytes(request.files['file_img'].read()))
                file.close
            message = '<br><img src=static/' + \
                request.files['file_img'].filename + \
                ' width=300px" height="300px">'
            img = Chat(title=name, text_message=message, time=time)
            db.session.add(img)
            db.session.commit()
            return("ok", 200)
        except:
            print("no img")
        message = data["message"]
        if message != None:
            name = data["name"]
            time = strftime("%H:%M:%S", localtime())
            chat = Chat(title=name, text_message=message, time=time)
            db.session.add(chat)
            db.session.commit()
        return ("ok", 200)

    else:
        return render_template("index.html")


@app.route('/output_message.html', methods=['POST'])
def output_message():
    messages = Chat.query.all()
    l = []
    for message in messages:
        l.append('<p class = "message" id='+str(message.id)+'>'+message.title +
                 ' || ' + message.text_message + ' || ' + message.time + '</p> ')
    html_response = ""
    html_response = html_response.join(l)
    return(html_response, 200)


if __name__ == "__main__":
    try:
        conn = sqlite3.connect("chat_database.db")
        cursor = conn.cursor()
        cursor.execute("DROP TABLE chat")
        conn.commit()
    finally:
        db.create_all()
        conn = sqlite3.connect("chat_database.db")
        cursor = conn.cursor()
        name = "GlaDos"
        message = "ЧАТ ПУСТ"
        time = "229"
        cursor.execute(
            "INSERT INTO chat (title, text_message, time) VALUES (?,?,?)", (name, message, time))
        conn.commit()
        app.run(debug=True)
