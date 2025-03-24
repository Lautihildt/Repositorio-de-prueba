from queue import Queue
from queue import LifoQueue

urgentes1 = Queue()
urgentes1.put(1)
urgentes1.put(3)
urgentes1.put(5)

postergables1 = Queue()
postergables1.put(2)
postergables1.put(4)
postergables1.put(6)

#requiere: {no hay elementos repetidos en urgentes}
#requiere: {no hay elementos repetidos en postergables}
#requiere: {la intersección entre postergables y urgentes es vacía}
#requiere: {|postergables| = |urgentes|}
#asegura: {no hay repetidos en res }
#asegura: {res es permutación de la concatenación de urgentes y postergables}
#asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
#asegura: {En res no hay dos seguidos de urgentes}
#asegura: {En res no hay dos seguidos de postergables}
#asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
#asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}


#1)
def orden_de_atencion (urgentes:Queue(int), postergables:Queue(int)) -> Queue(int):
    cola_final = Queue()
    cola_urgentes_aux = Queue()
    cola_postergables_aux = Queue()
    if urgentes.empty():
        return urgentes
    else:
        while (not urgentes.empty()) and (not postergables.empty()):
            primer_urgente = urgentes.get()
            primer_postergable = postergables.get()
            cola_final.put(primer_urgente)
            cola_urgentes_aux.put(primer_urgente)
            cola_final.put(primer_postergable)
            cola_postergables_aux.put(primer_postergable)
        while (not cola_urgentes_aux.empty()) and (not cola_postergables_aux.empty()):
            urgentes.put(cola_urgentes_aux.get())
            postergables.put(cola_postergables_aux.get())
        return cola_final
    

#2)
#problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
#requiere: {0 < umbral < 1}
#asegura: {claves de res pertenecen a infecciosas}
#asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
#asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}

def pertenece (elemento:str,lista:list) -> bool:
    for i in lista:
        if elemento == i:
            return True
    return False

def alarma_epidemiologica (registros: list, infecciosas: list, umbral: float) -> dict:
    diccionario_final:dict[str,float] = {}
    infecciosas_registradas:list[str] = []
    cantidad_de_registro:int = 0
    for enfermedad in registros:
        cantidad_de_registro +=1
        if pertenece(enfermedad[1],infecciosas) and not pertenece(enfermedad[1],infecciosas_registradas):
            infecciosas_registradas.append(enfermedad[1])
    for enfermedad in infecciosas_registradas:
        cantidad_enfermedad:int = 0
        for i in registros:
            if i[1] == enfermedad:
                cantidad_enfermedad +=1
        porcentaje = (cantidad_enfermedad/cantidad_de_registro)
        if porcentaje >= umbral:
            diccionario_final[enfermedad] = porcentaje
    return diccionario_final

registro_1 = [(321321312,"malaria"),(321321312,"cancer"),(321321312,"malaria"),(321321312,"malaria"),(321321312,"dengue"),(321321312,"malaria"),(321321312,"malaria"),(321321312,"covid"),(321321312,"malaria"),(213213,"dengue")]

enfermedades_infecciosas=["dengue","malaria"]

#problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
#requiere: {No hay valores en horas que sean listas vacías}
#asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
#asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
#asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}

def empleados_del_mes(horas:dict) -> list:
    maximo:float = 0
    lista:list = []
    for i in horas.keys():
        if sumatoria(horas[i]) > maximo:
            maximo = sumatoria(horas[i])
    for i in horas.keys():
        if sumatoria(horas[i]) == maximo:
            lista.append(i)
    return lista

def sumatoria (horas:list) -> float:
    sum:float = 0
    for i in horas:
        sum += i
    return sum

#problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
# requiere: {Todos los pisos tienen la misma cantidad de camas.}
# requiere: {Hay por lo menos 1 piso en el hospital.}
# requiere: {Hay por lo menos una cama por piso.}
# asegura: {|res| = |camas_por_piso|}
# asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}

def nivel_de_ocupacion(camas_por_piso:list) -> list:
    porcentaje_x_piso:list = []
    cant_camas_x_piso = len(camas_por_piso[0])
    for piso in camas_por_piso:
        camas_ocupadas: int = 0
        for cama in piso:
            if cama == True:
                camas_ocupadas += 1
        porcentaje_x_piso.append(camas_ocupadas/cant_camas_x_piso)
    return porcentaje_x_piso

