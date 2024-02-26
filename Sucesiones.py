"""
Ejercicios de sucesion del 10 al 14 (se me paso la 13)
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

sus10()
sus11()
sus12()
sus14()
