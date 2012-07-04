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

def completed_task(task_id):
	# task = Task.query.get(task_id)
	# task.complete()

	#
	
	# if task.done == True:
	# 	task.complete()
	# if task.done == False:
	# 	pass
	return redirect(url_for("home"))