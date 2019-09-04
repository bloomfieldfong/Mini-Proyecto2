# Universidad del Valle de Guatemala
# Michelle Bloomfield, 16803
# Andrea Cordón, 16076
# ejercicio4.py
import random

costo_retorno = 0.5
costo_compra = 1.5
costo_venta = 2.5

def eleccion(cantidad, probabilidades, itera= 30):
    resultado = []
    respuesta = []
    for dato, prob in zip(cantidad,probabilidades):
        resultado += [dato] * int(prob * 100)
    for i in range(0,itera):
        respuesta.append(random.choice(resultado))
    return respuesta

def calculo(compra, venta):
    lista = []

    perdidas = 0
    devoluciones = 0
    ganancias = 0

    for i in range(0, len(venta)):
        lista.append(compra - venta[i])
        if (venta[i]<=compra):
            ganancias += venta[i]
        if(venta[i]> compra):
            ganancias += compra
    
    for i in range(0, len(lista)):
        if(lista[i]<0):
            perdidas += 1
        if (lista[i]>0):
            devoluciones += 1

    return perdidas, devoluciones, ganancias



def main():

    nueve_mes=  calculo(9,eleccion([9,10,11], [0.3, 0.4,0.3]))
    nueve_anio=  calculo(9,eleccion([9,10,11], [0.3, 0.4,0.3],365))
    nueve_diez=  calculo(9,eleccion([9,10,11], [0.3, 0.4,0.3],3650))

    print("Si se compra 9 periodicos: ")
    print(" ->  En un mes: ")
    print("Su ganancia sera de "+ str(nueve_mes[2]+nueve_mes[1]) + "$.  Perdio " + str(nueve_mes[0])+ " ventas. Devolvio un total de: "+ str(nueve_mes[1])+ " periodicos")

    print(" -> En un año: ")
    print("Su ganancia sera de "+ str(nueve_anio[2]+nueve_anio[1]) + "$.  Perdio " + str(nueve_anio[0])+ " ventas. Devolvio un total de: "+ str(nueve_anio[1])+ " periodicos")

    print(" -> En diez años: ")
    print("Su ganancia sera de "+ str(nueve_diez[2]+nueve_diez[1]) + "$.  Perdio " + str(nueve_diez[0])+ " ventas. Devolvio un total de: "+ str(nueve_diez[1])+ " periodicos")
    
    print("--------------------------------------------------------------------------------------------------------")

    diez_mes=  calculo(10,eleccion([9,10,11], [0.3, 0.4,0.3]))
    diez_anio=  calculo(10,eleccion([9,10,11], [0.3, 0.4,0.3],365))
    diez_diez=  calculo(10,eleccion([9,10,11], [0.3, 0.4,0.3],3650))
    
    print("Si se compra 10 periodicos: ")
    print(" -> En un mes: ")
    print("Su ganancia sera de "+ str(diez_mes[2]+diez_mes[1]) + "$.  Perdio " + str(diez_mes[0])+ " ventas. Devolvio un total de: "+ str(diez_mes[1])+ " periodicos")

    print(" -> En un año: ")
    print("Su ganancia sera de "+ str(diez_anio[2]+diez_anio[1]) + "$.  Perdio " + str(diez_anio[0])+ " ventas. Devolvio un total de: "+ str(diez_anio[1])+ " periodicos")

    print(" -> En diez años: ")
    print("Su ganancia sera de "+ str(diez_diez[2]+diez_diez[1]) + "$.  Perdio " + str(diez_diez[0])+ " ventas. Devolvio un total de: "+ str(diez_diez[1])+ " periodicos")
    
    print("--------------------------------------------------------------------------------------------------------")
    once_mes=  calculo(11,eleccion([9,10,11], [0.3, 0.4,0.3]))
    once_anio=  calculo(11,eleccion([9,10,11], [0.3, 0.4,0.3],365))
    once_diez=  calculo(11,eleccion([9,10,11], [0.3, 0.4,0.3],3650))
    
    print("Si se compra 11 periodicos: ")
    print(" -> En un mes: ")
    print("Su ganancia sera de "+ str(once_mes[2]+once_mes[1]) + "$.  Perdio " + str(once_mes[0])+ " ventas. Devolvio un total de: "+ str(once_mes[1])+ " periodicos")

    print(" -> En un año: ")
    print("Su ganancia sera de "+ str(once_anio[2]+once_anio[1]) + "$.  Perdio " + str(once_anio[0])+ " ventas. Devolvio un total de: "+ str(once_anio[1])+ " periodicos")

    print(" -> En diez años: ")
    print("Su ganancia sera de "+ str(once_diez[2]+once_diez[1]) + "$.  Perdio " + str(once_diez[0])+ " ventas. Devolvio un total de: "+ str(once_diez[1])+ " periodicos")

main()