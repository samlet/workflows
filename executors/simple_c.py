"""
$ python simple_c.py
"""
from executors import simple
class SimpleCli(object):
    def invoke(self):
        """
        $ python -m executors.simple_c invoke
        :return:
        """
        result = simple.add.delay(4, 4)
        rd=result.get(timeout=1)
        print(rd)

if __name__ == '__main__':
    import fire
    fire.Fire(SimpleCli)


