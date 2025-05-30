import random
import pprint
import mlutils

a = random.uniform(0, 1000)
b = random.uniform(0, 1000)

w = random.uniform(0, 10)
s = random.uniform(0, 10)

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

for epoch in range(200):
    dcost_w = (cost(w + EPS, s) - cost(w, s)) / EPS
    dcost_s = (cost(w, s + EPS) - cost(w, s)) / EPS
    w -= RATE * dcost_w
    s -= RATE * dcost_s
    if epoch % 25 == 0:
        print(f"i: {epoch:3} | {w=:2.3} | {s=:3.2} | {dcost_w=:.2} | {dcost_s=:.2}")

print("-" * 60)
print(f"true:  y = {a:.2f}x + {b:.2f}")
print(f"guess: y = {w:.2f}x + {s:.2f}")
print(mlutils.poly_acc([a, b], [w, s]))
