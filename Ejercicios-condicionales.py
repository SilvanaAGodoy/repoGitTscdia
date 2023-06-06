# -------Ejercicios Condicionales-----
# 1-Realice un programa que solicite 2 letras al usuario y verificque si son iguales o no mostranso un mensaje:

letra_1 = input("Por favor ingrese una letra: ")
letra_2 = input("Por favor ingrese otra letra: ")
if (letra_1 != letra_2):
   print("Las letras no son iguales")
else:
   print("Las letras son iguales")

# 2)-Hacer un programa que permita decidir si dos palabras son iguales o
# diferentes. Mostrar mensaje por pantalla.

palabra1 = input("Ingresar primera palabra: ")
palabra2 = input("ingresar segunda palabra: ")
if (palabra1 == palabra2):
   print("Las palabras son iguales")
else:
   print("Las palabras no son iguales")

#   3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota
#en mesa femenina o masculina.

sexo = input( "Ingresar F si es mujer ó M si es hombre: ") 
if (sexo == "F"):
   print("Usted vota en la mesa femenina")
else:
   print("Usted vota en la mesa masculina") 

#4. Realice un programa que lea dos números y diga cuál es el mayor.       

primer_nro = input("Ingrese un número: ")
print("El primer número elegido es: ", primer_nro)
segundo_nro = input("Ingrese el segundo número:")
print("El segundo número elegido es: ", segundo_nro)
if (primer_nro > segundo_nro):
   print("El número mayor es: ", primer_nro)
else:
   print("El número mayor es: ", segundo_nro)   

 
#5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
#el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
#de cambio quiere, si de dólares a pesos o viceversa.

transaccion = input("Ingrese el código de la transacción que desea realizar: \n"
               "1. Para cambiar dólares a pesos\n"
               "2. Para cambiar pesos a dólares\n")
monto = int(input("Ingrese el monto a cambiar: "))
tc_cpra = 487
tc_vta = 495
if transaccion == "1":
    print("Usted va a recibir el total de:", monto * tc_cpra, "pesos argentinos")
elif transaccion == "2":
    print("Usted va a recibir el total de: ", monto / tc_vta, "dólares estadounidenses")
else:
    print("Elija otra operación")


# 6. Realice un programa donde el usuario ingrese su edad. Si es mayor de
# 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad = input( "Por favor ingrese su edad, sólo en formato números: ")
edad_para_votar = int(edad)
if (edad_para_votar > 16):
    print("Puede votar")
else:
    print("No vota")

# ---------------------Ejercicios IF Anidados--------------------------#

# 1. Introducir los lados de un triángulo y visualizar por pantalla si dicho
# triángulo es equilátero, isósceles o escaleno.

a = input("Introduzca el valor del lado a del triángulo: ")
b = input("Introduzca el valor del lado b del trángulo: ")
c = input("Introduzca el valor del lado c del tríangulo: ")
if (a == b and b == c and a == c):
    print("Se trata de un triángulo es equilátero")
elif (a == b or b == c or a == c):
    print("Se trata de un triángulo isósceles")
else:
    print("Se trata de un triángulo escaleno")

# 2. Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.

monto = float(input("Por favor ingrese el monto a pagar: "))
forma_pago = input("Ingrese la forma de pago que desea: \n"
                   "1.Para pago de contado, obtendrá un 10% de descuento\n"
                   "2.Para pago con tarjeta, se le aplicará un 10% de interés\n"
                   "3.Para pago con débito, obtendrá un descuento del 5% de interés: ")
if forma_pago == "1":
    print("Usted debe abonar ", monto - (monto * 0.10), "pesos.")
elif forma_pago == "2":
    print("Usted debe abonar ", monto * 1.10, "pesos.")
elif forma_pago == "3":
    print("Usted abonará ", monto - (monto * 0.05), "pesos")
else:
    print("por favor ingrese una opción válida")

# 3. Realice un programa que lea tres números, muestre cuál es el mayor y
# determine si es par o impar.

nro_1 = int(input("Ingrese el primer número: "))
nro_2 = int(input("Ingrese el segundo número: "))
nro_3 = int(input("Ingrese el tercer número: "))

if (nro_1 > nro_2 and nro_1 > nro_3):
    if (nro_1 / 2 == 0):
        print("El número ", nro_1,
              "es el mayor de los tres números ingrasados y es par.")
    else:
        print("El número ", nro_1,
              "es el mayor de los tres números ingresados y es impar.")
elif (nro_2 > nro_1 and nro_2 > nro_3):
    if (nro_2 / 2 == 0):
        print("El número ", nro_2,
              "es el mayor de los tres números ingresados y es par.")
    else:
        print("El número ", nro_2,
              "es el mayor de los tres números ingresados y es impar.")
elif (nro_3 > nro_1 and nro_3 > nro_2):
    if (nro_3 / 2 == 0):
        print("El número ", nro_3,
              "es el mayor de los tres números ingresados y es par.")
    else:
        print("El número ", nro_3,
              "es el mayor de los tres números ingresados y es impar.")
else:
    print()


# 4. Confeccione un programa que pida un número del 1 al 7 y diga el día de
# la semana correspondiente.

numero = int(input("Por favor ingrese un número del 1 al 7: "))
if numero == 1:
    print("Es día Lunes")
elif numero == 2:
    print("Es día Martes")
elif numero == 3:
    print("Es día Miércoles")
elif numero == 4:
    print("Es día Jueves")
elif numero == 5:
    print("Es día Viernes")
elif numero == 6:
    print("Es día Sábado")
elif numero == 7:
    print("Es día Domingo")
else:
    print("Por favor ingrese una opción válida.")

#5)- Realice un programa que pida un número del 1 al 12 y diga el nombre
# del mes correspondiente.

numero = int(input("Por favor ingrese un número del 1 al 12: "))
if numero == 1:
    print("Es el mes de Enero")
elif numero == 2:
    print("Es el mes de Febrero")
elif numero == 3:
    print("Es el mes de Marzo")
elif numero == 4:
    print("Es el mes de Abril")
elif numero == 5:
    print("Es el mes de Mayo")
elif numero == 6:
    print("Es el mes de Junio")
elif numero == 7:
    print("Es el mes de Julio")
elif numero == 8:
    print("Es el mes de Agosto")
elif numero == 9:
    print("Es el mes de Septiembre")
elif numero == 10:
    print("Es el mes de Octubre")
elif numero == 11:
    print("Es el mes de Noviembre")
elif numero == 12:
    print("Es el mes de Diciembre")
else:
    print("Por favor ingrese un número dentro del rango indicado.")
