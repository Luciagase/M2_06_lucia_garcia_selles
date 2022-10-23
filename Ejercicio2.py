#2) Realiza una función llamada lee_numero() que solicite y lea por teclado un numero. Utilizar esta función para pedirle al usuario 3 números. Luego pasarle estos 3 números a una función que se llame mayor() que tenga 3 parámetros y que devuelva el número mayor de los 3:

def lee_numero():
  return int(input('Introduce un numero: '))
# Se crea una función que unicamente pida un número

def mayor(lee_numero): #compara los numeros utilizando una lista
  numero1=lee_numero()
  numero2=lee_numero()
  numero3=lee_numero()
  lista=[] #Lista Vacía
  lista.append(numero1)
  lista.append(numero2)   #introduce los numeros en la lista
  lista.append(numero3)
  return max(lista)  # Devuelve mayor número de la lista

print('El numero mas grande es',mayor(lee_numero))
