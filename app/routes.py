from flask import (
    Flask,
    render_template,
    request,
    redirect
    )
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database.tasks import Task
from mk_task import create_task


TLIST = []
tasks = Task.query.all()

@app.get("/")
def index():
    return render_template("home.html", task_list=tasks)

@app.get("/about")
def about_me():
    me = {
        "first_name": "Jimmy",
        "last_name": "Newtron",
        "bio": "Thinker"
    }
    return render_template("about.html", user=me) 

@app.get("/tasks/create")
def get_form():
    return render_template("create_tasks.html")

@app.post("/tasks")
def create_tasks():
    task_data = request.form
    task_dict = {
        "name": task_data.get("name"),
        "body": task_data.get("body"),
        "priority": task_data.get("priority")
    }
    task_name = str(task_dict["name"])
    task_body = str(task_dict["body"])
    task_priority = str(task_dict["priority"])
    create_task(task_name, task_body, task_priority)
    return redirect("/")


