# ----------------EJERCICIOS-------------------------#

# 1.Realice una función para calcular el costo total recaudado en entradas de un recital.

def total_recaudado(cantidad_entradas_vendidas, precio_entrada):
    costo_total = cantidad_entradas_vendidas * precio_entrada
    return costo_total


cantidad_entradas_vendidas = 25000
precio_entrada = 11500

costo_total = total_recaudado(cantidad_entradas_vendidas, precio_entrada)

print(f'El costo total recaudado es de: {costo_total} pesos.')

# Alternativa 2 de resolución:


def total_recaudado(cantidad_entradas_vendidas, precio_entrada):
    costo_total = cantidad_entradas_vendidas * precio_entrada
    return print(f'El costo total recaudado es de: {costo_total} pesos.')


total_recaudado(25000, 11500)


# 2.Función para comprobar si una canción está en la lista de reproducción de un recital.

def comprobar_cancion(lista_reproduccion, cancion):
    if cancion in lista_reproduccion:
        return True
    else:
        return False


lista_reproduccion = ["Love Again", "Flowers",
                      "We are the Champions", "Bohemian Rapsody", "The Best"]
cancion = "The Best"

if comprobar_cancion(lista_reproduccion, cancion):
    print("La canción está en la lista de reproducción.")
else:
    print("La canción no está en la lista de reproducción.")


# 3.	Función para calcular el tiempo total de duración de un recital,
# considerando la duración de x cantidad de canciones.

def duracion_recital(cantidad_canciones, duracion_cancion):
    duracion_total = (cantidad_canciones * duracion_cancion)
    return duracion_total


cantidad_canciones = 20
duracion_cancion = 3.5  # en minutos

duracion_total = duracion_recital(cantidad_canciones, duracion_cancion)
print("La duración total del recital es de: ", duracion_total, "minutos")

# 4.Crear una función que calcule la velocidad promedio de un auto,
# dada la distancia recorrida y el tiempo empleado.


def velocidad_promedio_auto(distancia, tiempo):
    velocidad_promedio = distancia / tiempo
    return velocidad_promedio


distancia = 500  # kilometros
tiempo = 6.5  # horas

velocidad_promedio = velocidad_promedio_auto(distancia, tiempo)
print("La velocidad promedio de este auto es de: ",
      velocidad_promedio, "km por hora.")


# 5 Crear una función que determine si un auto está en marcha o detenido, dada su velocidad.

def estado_auto(velocidad):
    if velocidad > 0:
        estado = "en marcha"
    else:
        estado = "detenido"
    return estado


velocidad = 70  # km por hora

estado = estado_auto(velocidad)
print(f'El auto se encuentra {estado}')

# 6.	Crear una función que convierta kilómetros por hora a millas por hora.


def conversion_kmph_a_millasph(kmph):  # 1 km equivale a 0.621371 millas
    kmph_a_millasph = kmph * 0.621371
    return kmph_a_millasph


kmph = 1200

kmph_a_millasph = conversion_kmph_a_millasph(kmph)
print(f'{kmph} kilómetros por hora equivalen a {kmph_a_millasph} millas')

# 7.Crear una función que calcule el consumo de combustible de un auto por kilómetro,
# dada la distancia recorrida y la cantidad de combustible utilizada.


def consumo_combustible(distancia_recorrida, litros):
    consumo = litros / distancia_recorrida
    return consumo


distancia_recorrida = 3400  # kilometros
litros = 340

consumo = consumo_combustible(distancia_recorrida, litros)
print(
    f'El consumo de combustible del auto es de {consumo} litros por kilómetro.')

# 8)-Crear una función que determine el costo de un viaje en auto, dada la distancia recorrida,
# el consumo de combustible y el precio del combustible.


def costo_viaje_auto(distancia_recorrida, consumo_combustible, precio_combustible):
    costo = distancia_recorrida * consumo_combustible * precio_combustible
    return costo


distancia_recorrida = 500  # kilometros
consumo_combustible = 0.10  # litros por km
precio_combustible = 250  # precio por litro

costo = costo_viaje_auto(
    distancia_recorrida, consumo_combustible, precio_combustible)
print(f'El costo del viaje será de {costo} pesos.')
