'''
$ celery -A downloader worker --loglevel=debug
$ celery -A downloader status
$ celery -A downloader inspect stats
'''
from celery import Celery
import urllib.request
import os
import pathlib
# Where the downloaded files will be stored
# BASEDIR="/home/celery/downloadedFiles"
BASEDIR=pathlib.Path.home()/'downloads'/'tmp'

# Create the app and set the broker location (RabbitMQ)
app = Celery('downloaderApp',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')

@app.task
def download(url, filename):
    """
    Download a page and save it to the BASEDIR directory
      url: the url to download
      filename: the filename used to save the url in BASEDIR
    """
    response = urllib.request.urlopen(url)
    data = response.read()
    with open(BASEDIR/filename,'wb') as file:
        file.write(data)
    file.close()

@app.task
def list():
    """ Return an array of all downloaded files """
    return os.listdir(BASEDIR)

