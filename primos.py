"""
Numeros primos
Sarricolea Cortés Ethan Yahel
"""

def primos(numero):
    for i in range(2,numero,1):
        if (numero%i==0 and i!=numero):
            return False
    return True

def main():
    number = (primos(int(input("Coloca el numero: "))))
    print("Numero primo" if number else "Numero no primo")

if __name__=="__main__":
    main()