#Dado un diccionario donde la clave es el nombre de cada amigo y el valor es una lista de los tiempos (en minutos) registrados para cada sala de escape en Capital, 
# escribir una función en Python que devuelva un diccionario. En este nuevo diccionario, las claves deben ser los nombres de los amigos y los valores deben ser tuplas 
# que indiquen la cantidad de salas de las que cada persona logró salir y el promedio de los tiempos de salida (solo considerando las salas de las que lograron salir)

#problema promedio_de_salidas (in registro: dict⟨String, seq⟨Z⟩⟩) : dict⟨String, ⟨Z x R⟩⟩ {
# requiere: {registro tiene por lo menos un integrante}
# requiere: {Todos los integrantes de registro tiene por lo menos un tiempo}
# requiere: {Todos los valores de registro tiene la misma longitud}
# requiere: {Todos los tiempos de los valores de registro están entre 0 y 61 inclusive}
# asegura: {res tiene las mismas claves que registro}
# asegura: {El primer elemento de la tupla de res para un integrante, es la cantidad de salas con tiempo mayor estricto a 0 y menor estricto a 61 que
# figuran en sus valores de registro}
# asegura: {El segundo elemento de la tupla de res para un integrante, si la cantidad de salas de las que salió es mayor a 0: es el promedio de salas con 
# tiempo mayor estricto a 0 y menor estricto a 61 que figuran en sus valores de registro; sino es 0.0}

def promedio_de_salidas (registro:dict) -> dict:
    dic_final:dict = {}
    for clave in registro.keys():
        cant_de_salas:int = 0
        cant_minutos_validos:int = 0
        for i in registro[clave]:
            if i > 0 and i < 61:
                cant_de_salas += 1
                cant_minutos_validos += i
        if cant_minutos_validos > 0:
            dic_final[clave] = (cant_de_salas, cant_minutos_validos/cant_de_salas)
        else:
            dic_final[clave] = (cant_de_salas, cant_minutos_validos)
    return dic_final


#Dada una lista con los tiempos (en minutos) registrados para cada sala de escape de Capital, escribir una función en Python que devuelva la
#posición (índice) en la cual se encuentra el tiempo más rápido, excluyendo las salas en las que no haya salido (0 o mayor a 60).

#problema tiempo_mas_rapido (in tiempos_salas: seq⟨Z⟩): Z {
# requiere: {Hay por lo menos un elemento en tiempos_salas entre 1 y 60 inclusive}
# requiere: {Todos los tiempos en tiempos_salas están entre 0 y 61 inclusive}
# asegura: {res es la posición de la sala en tiempos_salas de la que más rápido se salió (en caso que haya más de una, devolver la primera, osea la de menor índice)}

def tiempo_mas_rapido (tiempo_salas:list) -> int:
    minimo:int = 61
    for i in tiempo_salas:
        if i < minimo and i > 0 :
            minimo = i
    for x in range(len(tiempo_salas)):
        if tiempo_salas[x] == minimo:
            return x

#Dada una matriz donde las columnas representan a cada amigo y las filas representan las salas de escape, y los valores son los tiempos (en minutos) registrados para
#cada sala (0 si no fueron, 61 si no salieron, y un número entre 1 y 60 si salieron), escribir una función en Python que devuelva los índices de todas las filas (que representan las salas)
#en las cuales el primer, segundo y cuarto amigo no fueron (0), pero el tercero sí fue (independientemente de si salió o no).

#problema escape_en_solitario (in amigos_por_salas: seq⟨seq⟨Z⟩⟩): seq⟨Z⟩ {
# requiere: {Hay por lo menos una sala en amigos_por_salas}
# requiere: {Hay 4 amigos en amigos_por_salas}
# requiere: {Todos los tiempos en cada sala de amigos_por_salas están entre 0 y 61 inclusive}
# asegura: {La longitud de res es menor igual que la longitud de amigos_por_salas}}
# asegura: {Por cada sala en amigos_por_salas cuyo primer, segundo y cuarto valor sea 0, y el tercer valor sea distinto de 0, la posición de dicha sala en amigos_por_salas debe aparecer res}
# asegura: {Para todo i pertenciente a res se cumple que el primer, segundo y cuarto valor de amigos_por_salas[i] es 0, y el tercer valor es distinto de 0}

def escape_en_solitario (amigos_por_salas: list) -> list:
    res:list = []
    cantidad_de_salas:int = len(amigos_por_salas)
    for sala in range(cantidad_de_salas):
        if (amigos_por_salas[sala][0] == 0) and (amigos_por_salas[sala][1] == 0) and (amigos_por_salas[sala][3] == 0) and (amigos_por_salas[sala][2] != 0):
            res.append(sala)
    return res

