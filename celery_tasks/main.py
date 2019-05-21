from celery_tasks.tasks import add

result = add.delay(5, 4)
print(result.get())
