⊕ [Using RabbitMQ — Celery 4.4.6 documentation](https://docs.celeryproject.org/en/stable/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq)
⊕ [How to Set Up a Task Queue with Celery and RabbitMQ | Linode](https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/)

```bash
# broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
$ rabbitmqctl add_user myuser mypassword
$ rabbitmqctl add_vhost myvhost
$ rabbitmqctl set_user_tags myuser mytag
$ rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

$ rabbitmqctl status
```

⊕ [First Steps with Celery — Celery 4.4.6 documentation](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html)

```python
app = Celery('tasks', backend='rpc://', broker='pyamqp://')
# Or if you want to use Redis as the result backend, but still use RabbitMQ as the message broker (a popular combination):
# app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')

>>> result = add.delay(4, 4)
# The ready() method returns whether the task has finished processing or not:
>>> result.ready()
False
# You can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:
>>> result.get(timeout=1)
8
# In case the task raised an exception, get() will re-raise the exception, but you can override this by specifying the propagate argument:
>>> result.get(propagate=False)
# If the task raised an exception, you can also gain access to the original traceback:
>>> result.traceback
```



