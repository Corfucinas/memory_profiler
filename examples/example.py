from memory_profiler import profile
@profile
def my_func():
    b = [2] * (2 * 10 ** 7)
    del b
    return [1] * (10 ** 6)

if __name__ == '__main__':
    my_func()
