⊕ [Installation — Airflow Documentation](https://airflow.apache.org/docs/stable/installation.html)
⊕ [Tutorial — Airflow Documentation](https://airflow.apache.org/docs/stable/tutorial.html)
⊕ [A really quick on-boarding for Apache airflow.](https://gist.github.com/mmziyad/e8905e0719c957a15e15362e95b97944)

## setup
```sh
pip install apache-airflow
airflow initdb
```

## start
```sh
$ python tutorial_2.py list_tasks
$ python tutorial_2.py test print_date 2015-06-01
$ python tutorial_2.py test templated 2015-06-01
```

+ use airflow cli

```bash
# 查看dags位置, 默认是: dags_folder = /Users/xiaofeiwu/airflow/dags
$ subl ~/airflow/airflow.cfg 
$ cp tutorial_2.py ~/airflow/dags/

# print the list of active DAGs
$ airflow list_dags

# prints the list of tasks the "tutorial" dag_id
$ airflow list_tasks tutorial

# prints the hierarchy of tasks in the tutorial DAG
$ airflow list_tasks tutorial --tree
$ airflow test tutorial_2 print_date 2015-06-01
```

## cluster
⊕ [How to Set Up a Task Queue with Celery and RabbitMQ | Linode](https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/#monitor-a-celery-cluster-with-flower)
⊕ [How Apache Airflow Distributes Jobs on Celery workers](https://medium.com/sicara/using-airflow-with-celery-workers-54cb5212d405)

## pipedream
⊕ [RequestBin.com — A modern request bin to collect, inspect and debug HTTP requests and webhooks](https://requestbin.com/)
    + https://pipedream.com/sources/dc_L3ubRw
    + https://pipedream.com/workflows
    + https://twitter.com/pipedream
    ⊕ [PipedreamHQ/pipedream: Serverless integration and compute platform. Free for developers.](https://github.com/PipedreamHQ/pipedream)

## products
⊕ [zapier ifttt 有何区别？ - 知乎](https://www.zhihu.com/question/40183758/answer/175709375)
⊕ [使用 IFTTT Marker 和 GitHub 打造个人阅读追踪系统 - 少数派](https://sspai.com/post/40000)
⊕ [手把手教你使用 Power Automate 建立一个 Rss 邮件订阅服务 - 少数派](https://sspai.com/post/60006)
⊕ [微软将Flow重新命名为Power Automate 添加了RPA功能和虚拟代理_创视网](https://chuangyi.chuangyetv.com/net/20191105/110519461.html)
⊕ [创建流程_简单流程_快速入门_Serverless 工作流-阿里云](https://help.aliyun.com/document_detail/122477.html?spm=a2c4g.11186623.2.22.3f72656f8TO6l7)

## opensources
⊕ [huginn/huginn: Create agents that monitor and act on your behalf. Your agents are standing by!](https://github.com/huginn/huginn)
⊕ [Huginn安装教程—建立你自己的IFTTT - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1405470)


