# ---------------EJERCICIOS----------------------------#

# # 1.Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares
# # y devuelva la sumatoria de los pares.

pares = []
impares = []
sumar_pares = 0

for i in range(4):
    num = int(input("Ingrese un numero: "))

    if num % 2 == 0:
        pares.append(num)
        sumar_pares += num

    else:
        impares.append(num)


print(f'Los numeros pares son: {pares}')
print(f'Los numeros impares son: {impares}')
print(f'La suma de los pares es: {sumar_pares} ')

# # 2.	Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100,
# # cuál es el número máximo y cuál es el número mínimo.


nros_mayores = []
nros_menores = []

for i in range(10):
    number = int(input("Ingrese un número: "))
    if number >= 100:
        nros_mayores.append(number)
    else:
        nros_menores.append(number)
print(
    f"La cantidad de números mayores a 100 (este incluído) es de: {len(nros_mayores)}")
print(f"La cantidad de números menores a 100 es de: {len(nros_menores)}")
print(f"El número máximo es: {max(nros_mayores)}")
print(f"El número mínimo es: {min(nros_menores)}")


# # 3-Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres,
# # cuántos varones, cuántos mayores de edad y cuántos menores de edad.


print("Mujeres = Para indicar su sexo, por favor ingres: femenino, fem o f")
print("varones = Para ingresar su sexo, por favor ingrese: masculino, masc o m")
print("Al ingresar su edad utilice sólo números")

mujeres = []
varones = []
mayores_de_edad = []
menores_de_edad = []

for i in range(15):
    sexo = input("Por favor ingrese su sexo: ")
    if sexo == "femenino" or sexo == "fem" or sexo == "f":
        mujeres.append(sexo)
    elif sexo == "masculino" or sexo == "masc" or sexo == "m":
        varones.append(sexo)
    else:
        print("Ingrese unna opción válida")
    edad = int(input("Ingrese su edad:"))
    if edad >= 18:
        mayores_de_edad.append(edad)
    elif edad < 18:
        menores_de_edad.append(edad)
    else:
        print("Ingrese una opción válida")
print(f'El grupo bajo estudio cuenta con {len(mujeres)} mujeres')
print(f'El grupo bajo estudio cuenta con {len(varones)} varones')
print(
    f'El grupo bajo estudio cuenta con {len(mayores_de_edad)} mayores de edad')
print(
    f'El grupo bajo estudio cuenta con {len(menores_de_edad)} menores de edad')

# 4.	Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

positivos = []
negativos = []
sumatoria = 0

for i in range(10):
    number = int(input("Ingrese un número:"))
    if number > 0:
        positivos.append(number)
        sumatoria += number
    else:
        negativos.append(number)
print(f'Los números positivos son {positivos}')
print(f'la suma de los números positivos ingresados es {sumatoria}')

# 5.	Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

positivos = []

for i in range(15):
    nro = int(input("Ingresar un número negativo: "))
    nro = abs(nro)
    positivos.append(nro)
print(f"Los números positivos son {positivos}.")
