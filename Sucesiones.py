"""
Ejercicios de sucesion del 10 al 14
Autor: Ethan Yahel Sarricolea Cortés
"""

def sus10():
    for i in range(1,(int(input("Coloca el largo: ")))+1):
        print(f"{(-1)**i}")

def sus11():
    for i in range(1,(int(input("Coloca el largo: ")))+1):
        print(f"{(i-1)*(-1)**i}")

def sus12():
    for i in range(1,(int(input("Coloca el largo: ")))+1):
        print(f"{i}/{(i+1)**2}")
        
def sus14():
    for i in range(1,(int(input("Coloca el largo: ")))+1):
        print(f"{i**2}/{3**i}")

def sus15():
    for i in range(1,(int(input("Coloca el largo: ")))+1):
        print("0" if i==1 else f"{(i-1)*((-1)**(i+1))}/{i}")

sus10()
sus11()
sus12()
sus14()
sus15()
