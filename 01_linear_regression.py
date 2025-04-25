import random
import pprint
# adicionar bias
"""
regressao linear
y = wx + b

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
DATA = [[i, a * i]
        for i in range(1, 5)]

w = random.random() * 10

def cost(w):
    result = 0
    for i in range(len(DATA)):
        x = DATA[i][0]
        y = DATA[i][1]
        _y = x * w
        
        result += (y - _y) ** 2

    result = result / len(DATA)
    return result

EPS = 1*10**(-2)
RATE = 1*10**(-2)

print("-" * 50)
print("DATA:")
pprint.pp(DATA)
print()
print(f"random initial weight: {w}")
print("-" * 50)

for epoch in range(20):
    dcost = (cost(w + EPS) - cost(w)) / EPS
    w -= RATE * dcost
    print(f"epoch: {epoch:2} | MSE: {cost(w):15.11f} | w: {w:.2f}")
    
print("-" * 50)
print(f"guessed weight: {w:.2f}")
print(f"true weight: {a:.2f}")
print(f"accuracy: {(10 - abs(a - w)) * 10:.2f}%")


