# Universidad del Valle de Guatemala
# Michelle Bloomfield, 16803
# Andrea Cordón, 16076
# ejercicio3.py

import random
import math
import numpy as np

def normal(mu, sigma):
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
    

def vpn(proy, iter):
    if(proy == 1):
        for i in range(0, iter):
            i0 = -800
            t1 = normal(-800, 50)
            t2 = normal(-800, 100)
            t3 = normal(-700, 150)
            t4 = normal(300, 200)
            t5 = normal(400, 200)
            t6 = normal(500, 200)
            uni = 
