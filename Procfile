minio: ./startup.run minio
downloader: celery -A executors.downloader worker --loglevel=debug
flower: celery -A executors.downloader flower --port=5555
