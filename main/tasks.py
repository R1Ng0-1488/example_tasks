from example_tasks.celery import app

from .models import Task
from .utils import process


@app.task
def start_task(task_id: int):
	task = Task.get_task(id=task_id)
	if task:
		task.set_status(1)
		result = process(task.csv.file.path)
		task.set_result(result)
		task.set_status(2)
