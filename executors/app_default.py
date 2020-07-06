'''
$ celery -A executors.app_default worker -l info
'''
from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('default',
             broker='amqp://',
             backend='amqp://',
             include=['executors.simple'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

