#1) Realiza una función que devuelva el área de un círculo a partir de un radio. La función se llamará area_circulo(). El radio se pedirá al usuario por teclado:
import math

def area_circulo():
  radio = float(input('Introduce el radio del circulo:')) #Variable radio para pedir el número
  area = math.pi*(radio)**2  #Operación que calcula el area
  return area # La función unicamente devolverá el valor del area
  

print('El area es ',(area_circulo())) #He decidico utilizar el método print fuera de la función para que estuviese menos determinada. En otras palabras, en el caso de que me interesase calcular el volumen de un cilindro, realizar una suma de areas, etc; utilizaría la función y el hecho de que el print estuviese dentro de ella sería molesto.