# .. an example with a for loop ..

import time

def test_1():
    a = {i: i + 1 for i in range(10000)}
    return

@profile
def test_2():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b

    a = [1] * (10 ** 6)
    for _ in range(2):
        b = [2] * (2 * 10 ** 7)
        del b
    return a


if __name__ == '__main__':
    test_1()
    time.sleep(1)
    test_2()
    time.sleep(1)
