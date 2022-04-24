def test(func):

    def process(*args, **kwargs):
        print('start')
        r = func(*args, **kwargs)
        print('end')
        return r
    return process

@test
def query(key):
    print('hello there ', key)

query('123')
