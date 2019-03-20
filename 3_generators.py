from time import time


def gen_filename():
    """Генерация уникального имени файла"""
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = t + 234
        print(sum)


g_file = gen_filename()


def gen_y():
    yield 1
    yield 2
    yield 3


g = gen_y()


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


"""
событийный цикл Round Robin
"""
g1 = gen1('Alexander')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
