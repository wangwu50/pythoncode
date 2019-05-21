from celery import Celery

app = Celery('tasks', broker='redis://10.224.11.231/3', backend='redis://10.224.11.231/4')


@app.task(name='celery_tasks.tasks.add')
def add(x, y):
    return x + y
