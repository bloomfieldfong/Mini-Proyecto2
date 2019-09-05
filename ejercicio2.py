# Universidad del Valle de Guatemala
# Michelle Bloomfield, 16803
# Andrea Cordón, 16076
# ejercicio2.py

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


def generador(pi, x):
    v = 0
    for i in range(0, len(x)):
        if(x[i] == "norm"):
            v += pi[i]*normal()

        if(x[i]=="uniforme"):
            v += pi[i]*np.random.uniform(0, 1)
    return v



def generador2(iter):
    gen_tot = 0
    for i in range(0, iter):
        gen = generador([0.1,0.9], ["norm", "uniforme"])
        gen_tot += gen
        return gen_tot

valor_esperado = str(generador([0.1,0.9], ["norm", "uniforme"]))
print("Valor con 100 iteraciones: " + str(generador2(100)) + " contra: " + valor_esperado)
print("Valor con 1000 iteraciones: " + str(generador2(1000)) + " contra: " + valor_esperado)
print("Valor con 10000 iteraciones: " + str(generador2(10000)) + " contra: " + valor_esperado)