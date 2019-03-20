from inspect import getgeneratorstate


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('.......', message)


@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except:
            pass
