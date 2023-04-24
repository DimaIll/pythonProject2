from flask import Flask
import utils
app = Flask(__name__)

@app.route("/")
def page_index():
    return "Я главная страничка"

@app.route("/profile/")
def page_profile():
    return "Имя пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/message/")
def page_message():
    return "Сообщения пользователя"

@app.route("/users/<int:uid>")
def profile(uid):
    print(uid)
    print(type(uid))
    return ""

app.run()
