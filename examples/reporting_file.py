from memory_profiler import profile

f=open('hi.txt','w+')

@profile(stream=f)
def my_func():
    b = [2] * (2 * 10 ** 7)
    del b
    return [1] * (10 ** 6)

@profile(stream=f)
def my_func1():
    b = [3] * (2 * 10 ** 7)
    del b
    return [2] * (10 ** 6)

if __name__ == '__main__':
    my_func()
    my_func1()