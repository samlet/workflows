# procs-celery-flower.md
⊕ [How to Set Up a Task Queue with Celery and RabbitMQ | Linode](https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/#monitor-a-celery-cluster-with-flower)
⊕ [mher/flower: Real-time monitor and web admin for Celery distributed task queue](https://github.com/mher/flower)
⊕ [How Apache Airflow Distributes Jobs on Celery workers](https://www.sicara.ai/blog/2019-04-08-apache-airflow-celery-workers)

## start
```sh
$ pip install wheel flower

$ celery -A downloader worker --loglevel=debug
$ celery -A downloader flower --port=5555

$ open http://localhost:5555/

# 执行任务时, ui监控会实时更新
$ python downloader_c.py download 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png' 'python-logo.png'

# use curl to practice interacting how to use the Flower API
curl -X POST -d '{"args":["http://www.celeryproject.org/static/img/logo.png","celery-logo.png"]}' 'http://localhost:5555/api/task/async-apply/downloader.download?refresh=True'
# 失败的任务会在ui面板上显示详细的错误信息
```


