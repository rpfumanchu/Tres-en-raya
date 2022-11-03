
    #ASI LO HICE AL PRINCIPIO, no tiene sentido seguir recorriendo la lista si ya se encontro una ocurrencia
    #  , MAS RÁPIDO DE ESTA OTRA FORMA   IMPLEMENTANDO FIND_N

# def find_one(list, aguja):
#     """
#     devuelve True si encuentra una o mas ocurrencias de aguja en list
#     """
#     #inicializamos el bool que representa la condicion de haber encontrado o no y el indice
#     encontrar = False
#     indice = 0
#     #mientras no se encuentre o se haya terminado con la list
#     while not encontrar and indice < len(list):
#     #miramos a ver si esta en la posicion actual
#         if aguja == list[indice]:
#             encontrar = True
#     #avanzamos al siguiente elemento
#         indice = indice + 1
#     #devolvemos si hemos encontrado o no
#     return encontrar

def find_one(list, aguja):
    return find_n(list, aguja, 1)


def find_n(list, aguja, n):
    """
    devuelve True si en list hay n o más ocurrencias de aguja
    False si hay menos o si n< 0
    """
    #si n >= 0..
    if n >= 0:
        #inicializamos el indice y el contador
        indice = 0
        contador = 0

        #mientras no hayamos encontrado al elemento o no hayamos terminado la lista
        while contador < n and indice < len(list):
            #si lo encontramos actualizamos el contador
            if aguja == list[indice]:
                contador = contador + 1

            #avanzamos al siguiente elemento
            indice = indice + 1
        #devolvemos el resultado de comparar con n
        return contador >= n
    else:
        return False

def find_streak(list, aguja, n):
    """
    devuelve true si en list hay n o mas seguidos o más agujas segudos
    """
    #si n >= 0
    if n >= 0:
        #inicializo el indice,  el contador y el indicador de racha
        indice = 0
        contador = 0
        racha = False
        #mientras no haya encontrado n seguidos u la lista no se haya acabado
        while contador < n and indice < len(list):
            #si lo encuentro activo el indicador de racha y actualizo el contador
            if aguja == list[indice]:
                racha = True
                contador = contador + 1
            #si no lo encuentro, desactivo el indicador de racha y lo pongo a cero
            else:
                racha = False
                contador = 0
            #avanzo al siguiente elemneto
            indice = indice +1
        #devolvemos el resultado de comparar con n SIEMPRE Y CUANDO estemos en racha
        return n >= contador and racha
    else:
    #para valores de n < 0 no tiene sentido
        return False
    