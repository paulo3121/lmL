import random
import numpy as np

import timeit

# np.random.seed(123)

order = 2
# true_p = np.random.uniform(0, 10, size=(order + 1))
# guess_p = np.random.uniform(0, 10, size=(order + 1))
true_p = np.array([1, 3, 2])
guess_p = np.array([1, 2, 2])
# guess_p = np.array([5, 8, 4])

np.random.seed(123)
DATA_xs = np.arange(-5, 5, 0.5)
DATA_ys = np.polyval(true_p, DATA_xs)
DATA = np.stack((DATA_xs, DATA_ys), axis=1)

print()
print(f"true_p:  {true_p}")
print(f"guess_p: {guess_p}")


EPS = 1e-2

I = np.identity(3)
a = I * EPS
R = guess_p + (I * EPS)


def batch_cost(): 
    powers = np.arange(R.shape[1])[::-1]
    X = DATA_xs[None, :] ** powers[:, None]
    Y_pred = R @ X
    # return ((Y_pred - DATA_ys) ** 2).mean(axis=1)
    return (Y_pred - DATA_ys) ** 2

def batch_cost2():
    return (np.array([np.polyval(r, DATA_xs) for r in R]) - DATA_ys) ** 2

def batch_cost3():
    print(np.vander([1,2,3], 3))

def batch_cost4():
    # return np.polyfit(guess_p, DATA_ys, 2)
    return np.polyfit(DATA_xs, DATA_ys, 2)
    
# def batch_cost4():
#     return (np.array([np.polynomial.polynomial.polyval(r, DATA_xs) for r in R]) - DATA_ys) ** 2


# print(timeit.timeit(batch_cost, number=10000))
# print(timeit.timeit(batch_cost2, number=10000))
# print(timeit.timeit(batch_cost2, number=10000))
# print(timeit.timeit(batch_cost4, number=10000))
# print(np.polynomial.polynomial.polyval([1,3,5], [1,5]))
# print(np.polyval([1,2,5], [1,5]))

print(batch_cost4())

# print(batch_cost())
# print()
# print(batch_cost2())
# batch_cost3()

# funcao cost(p) ((np.polyval(p, DATA_xs) - DATA_ys) ** 2).mean()
