# Universidad del Valle de Guatemala
# Michelle Bloomfield, 16803
# Andrea Cordón, 16076
# ejercicio1.py

import numpy as np
import random

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


print(generador([0.1,0.9], ["norm", "uniforme"]))