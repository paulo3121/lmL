import random
import pprint
import mlutils

def main(order):
    len_order = order + 1
    def poly(coefs, x):
        return sum([coef * (x**i) for i, coef in enumerate(coefs)])

    t_coefs = [random.uniform(-1000, 1000) for i in range(len_order)]
    g_coefs = [random.uniform(-1000, 1000) for i in range(len_order)]
    DATA = [[i, poly(t_coefs, i)]
            for i in sorted([random.uniform(-2.5, 2.5) for i in range(100)])]

    def loss(coefs):
        cost = 0
        for i in range(len(DATA)):
            x = DATA[i][0]
            y = DATA[i][1]
            _y = poly(coefs, x)
            cost += (y - _y) ** 2

        cost = cost / len(DATA)
        return cost

    # funcionam bem até ordem 5
    EPS = 1e-5
    RATE = 5e-4

    def dy(alt_coefs, coefs):
        return (loss(alt_coefs) - loss(coefs)) / EPS

    for epoch in range(10000):
        alts_coefs = [[coef + EPS if j == i else coef # existe jeito melhor do que max?
                       for j, coef in enumerate(g_coefs)]
                       for i in range(len_order)]

        dcosts = [dy(alt_coef, g_coefs) for alt_coef in alts_coefs]
        for i in range(len_order):
            g_coefs[i] -= dcosts[i] * RATE
        # if epoch in [100, 1000, 5000, 9999]:
        #     print(epoch, mlutils.poly_acc(t_coefs, g_coefs))

    return mlutils.poly_acc(t_coefs, g_coefs)

print(main(3))
