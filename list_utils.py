

def find_one(list, aguja):
    """
    devuelve True si encuentra una o mas ocurrencias de aguja en list
    """
    #inicializamos el bool que representa la condicion de haber encontrado o no y el indice
    encontrar = False
    index = 0
    #mientras no se encuentre o se haya terminado con la list
    while not encontrar and index < len(list):
    #miramos a ver si esta en la posicion actual
        if aguja == list[index]:
            aguja = True
    #avanzamos al siguiente elemento
        index = index + 1
    #devolvemos si hemos encontrado o no
    return encontrar