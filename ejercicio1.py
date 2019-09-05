# Universidad del Valle de Guatemala
# Michelle Bloomfield, 16803
# Andrea Cordón, 16076
# ejercicio1.py

import numpy as np
import random
import math

def normal(mu = 900, sigma = 200):
    while True:
        y1 = -(1/1)*np.log(random.random())
        y2 = -(1/1)*np.log(random.random())
        if (y2 - ((y1 - 1)**2)/2) > 0:
            y = y2 - ((y1 - 1)**2)/2
            u = random.random()
            if(u <= 0.5):
                return mu + sigma*y
            else:
                return mu + sigma*y


def uniforme():
    j = np.random.uniform(0, 1)
    return j

def generador():
    v = 0
    u = random.random()
    valor_esperado = 0.1*normal() + 0.9*uniforme()
    return valor_esperado



def generador2(iter):
    gen_tot = 0
    for i in range(0, iter):
        gen = generador()
        gen_tot += gen
    return gen_tot/iter

valor_esperado = 0.1*normal() + 0.9*uniforme()
print("Valor con 100 iteraciones: " + str(generador2(100)) + " contra: " + str(valor_esperado))
print("Valor con 1000 iteraciones: " + str(generador2(1000)) + " contra: " + str(valor_esperado))
print("Valor con 10000 iteraciones: " + str(generador2(10000)) + " contra: " + str(valor_esperado))