import numpy as np
import scipy.signal


@profile
def create_data():
    return [np.random.randn(1, 70, 71, 72) for _ in range(70)]


@profile
def process_data(data):
    data = np.concatenate(data)
    return scipy.signal.detrend(data, axis=0)


if __name__ == "__main__":
    data1 = create_data()
    data2 = process_data(data1)
