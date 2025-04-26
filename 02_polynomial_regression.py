import random
import pprint

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
        
    EPS = 1e-3
    RATE = 1e-3
    
    def dy(alt_coefs, coefs):
        return (loss(alt_coefs) - loss(coefs)) / EPS

    # print(t_coefs)
    # print(g_coefs)
    for epoch in range(10000):
        alts_coefs = [[coef + EPS if j == i else coef # existe jeito melhor do que max?
                       for j, coef in enumerate(g_coefs)]
                       for i in range(len_order)]

        dcosts = [dy(alt_coef, g_coefs) for alt_coef in alts_coefs]
        for i in range(len_order):
            g_coefs[i] -= dcosts[i] * RATE

        # pprint.pprint(alts_coefs, width=60)
        # pprint.pprint(dcosts, width=60)
    # print(g_coefs)

    teste = [(1 - abs(t_coefs[i] - g_coefs[i]) / max(abs(t_coefs[i]), abs(g_coefs[i]), 1)) for i in range(len_order)]
    similaridade = sum(teste) / len_order
    print(round(similaridade * 100, 2))

    
main(1)
main(2)
main(3)
main(4)
main(5)
main(6)
main(7)
main(8)
