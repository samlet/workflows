"""
$ python simple_c.py
"""
def invoke():
    import simple
    result = simple.add.delay(4, 4)
    rd=result.get(timeout=1)
    print(rd)

if __name__ == '__main__':
    invoke()
