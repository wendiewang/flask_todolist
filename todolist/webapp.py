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

@app.route("/edit/<int:task_id>", methods=["GET"])
def edit_task(task_id):
	task = Task.query.get(task_id) 
	return render_template("edit.html", task=task)

@app.route("/edit/<int:task_id>", methods=["POST"])
def update_task(task_id):
	task = Task.query.get(task_id)
	task.title = request.form['title']
	model.save_all()
	return redirect(url_for("home"))

@app.route("/complete/<int:task_id>", methods=["POST"])
def completed_task(task_id):
	#task = Task.query.get(task_id)
	task_id = Task.complete() 
	return redirect(url_for("home"))

# WENDY AND JAMIE, YOU ARE STUCK ON HOW TO MARK A TASK COMPLETE OR INCOMPLETE.
# learn something quick. PS, don't fret. you are still awesome!

# "{{ url_for('not_completed', task_id=task.id) }}" YOU MIGHT NEED THIS FOR INCOMPLETE