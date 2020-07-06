# procs-celery-project.md
## start
```sh
$ sudo mkdir /var/run/celery
$ sudo mkdir /var/log/celery
$ sudo chown -R xiaofeiwu /var/log/celery/
$ sudo chown -R xiaofeiwu /var/run/celery/

# In the background
$ proj='executors.app_default'
$ celery multi start w1 -A $proj -l info

# $ celery  multi restart w1 -A proj -l info
# $ celery multi stop w1 -A proj -l info
# The stop command is asynchronous so it won’t wait for the worker to shutdown. You’ll probably want to use the stopwait command instead, which ensures that all currently executing tasks are completed before exiting:

$ celery multi stopwait w1 -A $proj -l info
# celery multi doesn’t store information about workers so you need to use the same command-line arguments when restarting. Only the same pidfile and logfile arguments must be used when stopping.

# 启动curses界面
$ celery -A $proj events
# 完成监视后，可以再次禁用事件：
$ celery -A $proj control disable_events
# workers
$ celery -A $proj status
```

