from executors.downloader import download, list
class DownloaderCli(object):
    def download(self, url, target, wait=False):
        """
        $ python downloader_c.py download 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png' 'python-logo.png'
        :return:
        """
        r = download.delay(url, target)
        # r.ready()
        # wait until done
        if wait:
            r.get(timeout=10)

    def list(self):
        """
        $ python downloader_c.py list
        $ python -m executors.downloader_c list
        :return:
        """
        r = list.delay()
        r.ready()
        print(r.get(timeout=1))

if __name__ == '__main__':
    import fire
    fire.Fire(DownloaderCli)



