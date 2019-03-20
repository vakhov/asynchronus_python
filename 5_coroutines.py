from inspect import getgeneratorstate


def subgen():
    """
    g = subgen()
    getgeneratorstate(g)  # 'GEN_CREATED'
    # next(g) equal g.send(None)
    g.send(None)
    getgeneratorstate(g)  # 'GEN_SUSPENDED'
    g.send('Ok')  # Subgen received: Ok
    :return:
    """
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass

@coroutine
def avarage():
    count = 0
    summ = 0
    avarage = None

    while True:
        try:
            x = yield avarage
        except StopIteration:
            print('Done')
        except BlaBlaException:
            print('.....................')
        else:
            count += 1
            summ += x
            avarage = round(summ / count, 2)
