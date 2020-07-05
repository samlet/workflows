# procs-scheduler.md
⊕ [Advanced Python Scheduler — APScheduler 3.6.3 documentation](https://apscheduler.readthedocs.io/en/stable/)
    调度程序的选择主要取决于您的编程环境以及APScheduler的用途。这是选择调度程序的快速指南：

    BlockingScheduler：当调度程序是您的流程中唯一运行的东西时使用
    BackgroundScheduler：在不使用以下任何框架且希望调度程序在应用程序内部的后台运行时使用
    AsyncIOScheduler：如果您的应用程序使用asyncio模块，则使用
    GeventScheduler：如果您的应用程序使用gevent，则使用
    TornadoScheduler：在构建Tornado应用程序时使用

    