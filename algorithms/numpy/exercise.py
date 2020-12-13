import numpy as np
import math
from timeit import default_timer as time


def func(N):

    start_time = time()

    s_0 = 97
    K = 103
    T = 1.5

    r = 0.05
    s = 0.2

    z = np.random.randn(N)

    c_one = s_0 * math.exp(( r - s ** 2 * 1/2 ) * T)
    c_two = s * T ** (1 / 2)
    b = math.exp(1) * np.ones(N)

    c = c_two * z
    s_t = c_one * (b ** c)

    g = s_t - K
    h_t = np.where(g > 0, g, 0)

    end_time = time()

    print(h_t)

    print(end_time - start_time)


print("first execution:")
func(1000)

print("----------------")

print("second execution:")
func(100000)

print("----------------")

print("third execution:")
func(10000000)