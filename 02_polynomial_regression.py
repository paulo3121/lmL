import random
import pprint

def main(order):
    def poly(coefs, x):
        return sum([coef * (x**i) for i, coef in enumerate(coefs)])

    t_coefs = [random.uniform(-100, 100) for i in range(order + 1)]
    g_coefs = [random.uniform(-100, 100) for i in range(order + 1)]
    DATA = [[i, poly(t_coefs, i)]
            for i in sorted([random.uniform(-4, 4) for i in range(20)])]
    # pprint.pprint(DATA)
    # print()

    # t_coefs = [1, 2, 5, 1]        # 1 + 2x + 5x2 + x3
    # g_coefs = [8, 3, 1, 7]        # 8 + 3x + 1x2 + 7x3
    
    # DATA = [[i, poly(t_coefs, i)]
    #         for i in [-3, -2, -1, 0, 1, 2, 3]]

    # pprint.pp(DATA)
    # print()

    def loss(coefs):
        cost = 0
        for i in range(len(DATA)):
            x = DATA[i][0]
            y = DATA[i][1]
            _y = poly(coefs, x)
            cost += (y - _y) ** 2

        cost = cost / len(DATA)
        return cost
        

    # EPS = 1e-3
    # RATE = 43e-4
    EPS = 1e-4
    RATE = 1e-3
    
    def dy(alt_coefs, coefs):
        return (loss(alt_coefs) - loss(coefs)) / EPS

    # print(t_coefs)
    # print(g_coefs)
    for epoch in range(10000):
        alts_coefs = [[coef + EPS if j == i else coef # existe jeito melhor do que max?
                       for j, coef in enumerate(g_coefs)]
                       for i in range(4)]

        dcosts = [dy(alt_coef, g_coefs) for alt_coef in alts_coefs]
        for i in range(4):
            g_coefs[i] -= dcosts[i] * RATE

        # pprint.pprint(alts_coefs, width=60)
        # pprint.pprint(dcosts, width=60)
    # print(g_coefs)

    teste = [(1 - abs(t_coefs[i] - g_coefs[i]) / max(abs(t_coefs[i]), abs(g_coefs[i]), 1)) for i in range(4)]
    similaridade = sum(teste) / 4
    print(round(similaridade * 100, 2))

    
main(3)
main(3)
main(3)
