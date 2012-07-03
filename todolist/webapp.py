from flask import redirect, url_for, render_template, request
from model import app, Task
import model

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)


@app.route("/add", methods=["GET"])
def make_task():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def save_task():
	title = request.form['task_title']
	t = Task(title)
	model.add(t)
	model.save_all()
	return redirect(url_for("home"))

@app.route("/edit/<int:task_id>")
def edit_task(task_id):
	t = Task.query.get(task_id)
	t.complete()
	model.save_all()
	return "Task %d is now complete at %r" %(task_id, t.completed_at)