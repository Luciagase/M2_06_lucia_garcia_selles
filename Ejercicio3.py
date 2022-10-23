#3) Realizar una función llamada imc(). Esta función nos proporcionará el estado nutricional de una persona. Esto es; la clasificación de su índice de masa corporal (IMC), según la tabla proporcionada. La función recibirá el peso (en kilos) y la talla de una persona (en metros con dos decimales), datos a partir de los cuales se puede calcular el IMC cómo:

def imc():
  peso = round(float(input('Introduce peso en kg: ')),2)
  altura = round(float(input('Introduce altura en m: ')),2)
  IMC = round(float(peso/(altura*altura)),1)
  return IMC

def clasificacion(imc):
  global IMC #Necesito hacer la variable IMC global porque si no el ultimo print no la encuentra ya que está dentro de la función
  IMC=imc()
  if IMC < 18.5:
    return 'Bajo peso'
  elif 18.5 <= IMC < 25:
    return 'Normal'
  elif 25 <= IMC < 30:
    return 'sobrepeso'
  else:
    return 'Obesidad'

print('Tu indice de masa corporal es',clasificacion(imc),'pues es de',IMC)