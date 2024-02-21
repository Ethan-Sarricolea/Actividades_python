"""
Escribe un programa en python que indique si dos números dados son amigos

Numeros amigos: Si la suma de los divisores dan como resultado el numero amigo

"""

def factores(n):
  numeros = []
  for i in range(1,n+1):
    if n%i==0:
        True if (i==n) else numeros.append(i)   # Quitamos el factor si es el mismo numero
  return numeros            # Obtenemos la lista de factores

def amigos():
    suma1=0
    suma2=0
    for i in lista:
       suma1+=i
    for i in lista2:
       suma2+=i
    return True if (suma1==n2 and suma2==n) else False

n = int(input("Coloca el primer numero: "))
n2= int(input("Coloca el segundo numero: "))
lista = factores(n)
lista2 = factores(n2)

print(f"Los numeros son amigos" if amigos() else f"Los numeros no son amigos")
