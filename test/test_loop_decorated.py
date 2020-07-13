# .. an example with a for loop ..

import time

@profile
def test_1():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    time.sleep(0.6)
    del b

    a = [1] * (10 ** 6)
    for _ in range(2):
        b = [2] * (2 * 10 ** 7)
        del b
    return a

@profile
def test_2():
    time.sleep(0.5)
    a = {i: i + 1 for i in range(10000)}
    time.sleep(0.6)
    return

if __name__ == '__main__':
    test_1()
    test_2()
