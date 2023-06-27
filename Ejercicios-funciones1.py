# 1.Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), 
# ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. 

def saludo(nro_aula):
    print(f'Hola Aula {nro_aula}, cómo están?')

saludo(1)  
print( "Que hermoso día")  
saludo(1)
print("Me encantaría tomar una taza de café")
saludo(1)

# 2.A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo con al menos
# otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos
# argumentos.

def Saludo(nombre):
    print(f'Hola {nombre}, Que tal?')

Saludo("Andrea")
Saludo("Josefina")
Saludo("Martín")    

#3.	Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma.
# Mostrar el resultado dos veces.

def suma (n1, n2, n3):
    print(f'La suma es igual a: {n1 + n2 + n3}')
    print(f'La suma es igual a: {n1 + n2 + n3}')

suma(10, 5, 30)

# 4.Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un 
# mensaje que muestre TRUE. 

def comparativo(number1, number2):
    if number1 == number2:
        print("TRUE")

comparativo(10, 10)

# 5.Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables
# locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este 
# ejercicio sería dos.

def sumayresta(a, b):
    suma = a + b
    resta = a - b
    print(f'El resultado de la suma de a + b es: {suma}')
    print(f'El resultado de la resta de a - b es: {resta}')

sumayresta(10, 5)

#6. Realice un programa que contenga una función que se llame “conversion”, 
# que la misma contenga tres parámetros. Se pide convertir los segundos ingresados 
# en horas, minutos y segundos

def conversion(segundos):
   horas = segundos / 3600
   minutos = segundos / 60
   print (f'La cantidad de {segundos} segundos, corresponden a {horas} horas')
   print (f'La cantidad de {segundos} segundos, corresponden a {minutos} minutos') 
  
segundos = int(input( "Ingrese la cantidad de segundos: "))   
conversion(segundos)   

