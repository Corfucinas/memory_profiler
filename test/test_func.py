
@profile
def test_1(i):
    # .. will be called twice ..
    c = {i: 2 for i in range(i)}

if __name__ == '__main__':
    test_1(10)
    test_1(10000)
