# procs-celery-group.md
⊕ [画布：设计工作流程— Celery 4.4.6文档](https://docs.celeryproject.org/en/stable/userguide/canvas.html#canvas-group)

```python
# 您可以轻松创建一组任务以并行执行：
>>> from celery import group
>>> res = group(add.s(i, i) for i in range(10))()
>>> res.get(timeout=1)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 简单的链，执行第一个任务并将其返回值传递给链中的下一个任务，依此类推。
>>> from celery import chain

>>> # 2 + 2 + 4 + 8
>>> res = chain(add.s(2, 2), add.s(4), add.s(8))()
>>> res.get()
16

# 也可以使用管道来编写：
>>> (add.s(2, 2) | add.s(4) | add.s(8))().get()
16

# 如果您不希望链中上一个任务的结果。可以创建一系列独立的任务：
>>> res = (add.si(2, 2) | add.si(4, 4) | add.si(8, 8))()
>>> res.get()
16
>>> res.parent.get()
8
>>> res.parent.parent.get()
4

# 和弦原语使我们能够添加当组中的所有任务完成执行时要调用的回调。
>>> from celery import chord
>>> res = chord((add.s(i, i) for i in range(10)), xsum.s())()
>>> res.get()
90
# 上面的示例创建了10个任务，这些任务全部并行启动，当所有任务完成时，返回值组合到一个列表中并发送给该xsum任务。

# 将组与另一个任务链接在一起将自动将其升级为和弦：
>>> c3 = (group(add.s(i, i) for i in range(10)) | xsum.s())
>>> res = c3()
>>> res.get()
90

# 组和弦也接受部分参数，因此在链中，前一个任务的返回值将转发到组中的所有任务：

>>> new_user_workflow = (create_user.s() | group(
...                      import_contacts.s(),
...                      send_welcome_email.s()))
... new_user_workflow.delay(username='artv',
...                         first='Art',
...                         last='Vandelay',
...                         email='art@vandelay.com')

# 如果您不想将参数转发给组，则可以使组中的签名不可变：

>>> res = (add.s(4, 4) | group(add.si(i, i) for i in range(10)))()
>>> res.get()
<GroupResult: de44df8c-821d-4c84-9a6a-44769c738f98 [
    bc01831b-9486-4e51-b046-480d7c9b78de,
    2650a1b8-32bf-4771-a645-b0a35dcc791b,
    dcbee2a5-e92d-4b03-b6eb-7aec60fd30cf,
    59f92e0a-23ea-41ce-9fad-8645a0e7759c,
    26e1e707-eccf-4bf4-bbd8-1e1729c3cce3,
    2d10a5f4-37f0-41b2-96ac-a973b1df024d,
    e13d3bdb-7ae3-4101-81a4-6f17ee21df2d,
    104b2be0-7b75-44eb-ac8e-f9220bdfa140,
    c5c551a5-0386-4973-aa37-b65cbeb2624b,
    83f72d71-4b71-428e-b604-6f16599a9f37]>

>>> res.parent.get()
8
```


