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

```sh
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

