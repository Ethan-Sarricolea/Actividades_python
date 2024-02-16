# -*- coding: utf-8 -*-
"""

Sarricolea Cortés Ethan Yahel

Algoritmo de euclides

"""

def MCD(num1,num2):
    mayor = num1 if num1>num2 else num2
    menor = num2 if mayor==num1 else num1
    if mayor%menor>0:
        MCD(menor,(mayor%menor))
    elif (mayor==0 or menor==0):
        if mayor==0:
            return menor
        else:
            return mayor
    
numero = []
    
for i in range(0,2,1):
    numero.append(int(input(f"Coloca el numero {i+1}:")))
    
print("El maximo comun divisor es: ")
dato = MCD(numero[0],numero[1])
print(dato)
