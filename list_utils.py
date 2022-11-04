
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
        #devolvemos el resultadoado de comparar con n
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
        #devolvemos el resultadoado de comparar con n SIEMPRE Y CUANDO estemos en racha
        return contador >= n and racha
    else:
        #para valores de n < 0 no tiene sentido
        return False
    
# una matriz es una lista de listas de igual tamaño
def firts_elements(lista_de_listas):
    """
    drecibe una lista de listas y devuelve una lista con los primeros elementos de la original"""
    return nth_elements(lista_de_listas, 0)

def nth_elements(lista_de_listas, n):
    """
    Recibe una lista de listas y devuelve una lista
    con los enésimos elementos de la original
    """
    resultado = []
    for lista in lista_de_listas:
        resultado.append(lista[n])
    return resultado

def transpose(matriz):
    """
    recibe una matriz y devuelve su traspuesta
    """
    #creo una matriz vacia y la llamo trasp
    transp = []
    #ahora hay que recorrer desde 0 hasta último indice de todas las columnas de la matriz original
    for n in range(len(matriz[0])):
        #extraemos los elementos enésimos y los ponemos en transp 
        transp.append(nth_elements(matriz, n))
    return transp

def displace(l, distance, relleno=None):
    if distance == 0:
        return l
    elif distance > 0:
        rellenar = [relleno]  * distance
        res = rellenar + l
        #a las posicones finales :-
        res = res[:-distance]
        return res
    else:
        #con abs le decimos el valor absoluto y con : para el principio
        rellenar = [relleno] * abs(distance)
        res = l + rellenar
        res = res[abs(distance):]
        return res

def displace_matriz(m, relleno=None):
    #creamos una matriz vacia
    matriz = []
    #por cada colimna de la matriz original la desplazamos su índice -1
    for i in range(len(m)):
        #añadimos la columna desplazada a m
        matriz.append(displace(m[i], i - 1, relleno))
    #devolvemos matriz
    return matriz

def reverse_list(l):
    # ya usamos lisst ante para que nos devuelva una lista y para que nos devuelva es lista al reves usaremos la función de python reversed
    return list(reversed(l))

def reverse_matriz(matriz):
    revm = []
    for colum in matriz:
        revm.append(reverse_list(colum))
    return revm
