import random
import pprint

"""
regressao linear
original: y = ax + b
modelo:   y = wx + s

uso de somente um neuron para achar um
weight que aproxime uma funcao afim
dos dados de entrada

comeca com weight aleatorio

precisamos de uma funcao cost/loss para acompanhamos o erro
ela deve usar alguma metrica de regressao
usarei MSE, Mean Squared Error

solucao analitica: melhor weight sera o 0 da derivada da fn cost
solucao gradient descent (brute-force): durante algumas
iteracoes, usar a derivada no ponto (com um pqn fator de
aprendizagem arbitrario) como gradiente para aproximar weight
"""

a = random.random() * 10
b = random.random() * 10

w = random.random() * 10
s = random.random() * 10


DATA = [[i, a * i + b]
        for i in range(1, 5)]

def cost(w, s):
    result = 0
    for i in range(len(DATA)):
        x = DATA[i][0]
        y = DATA[i][1]
        _y = x * w + s

        result += (y - _y) ** 2

    result = result / len(DATA)
    return result

EPS = 5e-5
RATE = 75e-3

for epoch in range(50):
    dcost_w = (cost(w + EPS, s) - cost(w, s)) / EPS
    dcost_s = (cost(w, s + EPS) - cost(w, s)) / EPS
    w -= RATE * dcost_w
    s -= 3 * RATE * dcost_s
    print(f"epoch: {epoch:2} | MSE: {cost(w, s):15.11f} | y = : {w:.2f}x + {s:.2f}")

print("-" * 50)
print(f"true:  y = {a:.2f}x + {b:.2f}")
print(f"guess: y = {w:.2f}x + {s:.2f}")
