from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)



app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["POST"])
def index():
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    if request.method == "GET":
        if session.get("notes") != None:
            session["notes"].pop();
    return render_template("index.html", notes=session["notes"])
