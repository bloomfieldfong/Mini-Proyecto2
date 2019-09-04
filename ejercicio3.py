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


def uniform(mu2, sigma2):
    rango = sigma2 - mu2
    selection = np.random.uniform(0, 1)
    return mu2 + (rango*selection)
    

def vpn(proy, iter):
    if(proy == 1):
        #vpn_list = []
        vpn_net = 0
        for i in range(0, iter):
            i0 = -800
            t1 = normal(-800, 50)
            t2 = normal(-800, 100)
            t3 = normal(-700, 150)
            t4 = normal(300, 200)
            t5 = normal(400, 200)
            t6 = normal(500, 200)
            uni = uniform(200, 8440)
            vpn = i0 + (t1/(1 + 0.1)**1) + (t2/(1 + 0.1)**2) + (t3/(1 + 0.1)**3) + (t4/(1 + 0.1)**4) + (t5/(1 + 0.1)**5) + (t6/(1 + 0.1)**6) + (uni/(1 + 0.1)**7)
            vpn_net += vpn
        return vpn_net/iter
    if(proy == 2):
        #vpn_list = []
        vpn_net = 0
        for i in range(0, iter):
            i0 = -900
            t1 = normal(-600, 50)
            t2 = normal(-200, 50)
            t3 = normal(-600, 100)
            t4 = normal(250, 150)
            t5 = normal(350, 150)
            t6 = normal(400, 150)
            uni = uniform(1600, 6000)
            vpn = i0 + (t1/(1 + 0.1)**1) + (t2/(1 + 0.1)**2) + (t3/(1 + 0.1)**3) + (t4/(1 + 0.1)**4) + (t5/(1 + 0.1)**5) + (t6/(1 + 0.1)**6) + (uni/(1 + 0.1)**7)
            vpn_net += vpn
        return vpn_net/iter

print("---------------- HOTEL ----------------")
print("Con 100 iteraciones:" + "\n" + "\tVPN = " + str(vpn(1, 100)))
print("Con 1000 iteraciones:" + "\n" + "\tVPN = " + str(vpn(1, 100)))
print("Con 10000 iteraciones:" + "\n" + "\tVPN = " + str(vpn(1, 100)))


print("\n------------------ CC ------------------")
print("Con 100 iteraciones:" + "\n" + "\tVPN = " + str(vpn(2, 100)))
print("Con 1000 iteraciones:" + "\n" + "\tVPN = " + str(vpn(2, 100)))
print("Con 10000 iteraciones:" + "\n" + "\tVPN = " + str(vpn(2, 100)))
