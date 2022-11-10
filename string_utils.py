
def explode_string(una_cadena):
    """
    trasforma una cadena en una lista de caracteres
     "Han" => ["H", "a", "n"]
    """
#para hacer esto python tiene una funcion que te hace precisamente esto : list()

    return list(una_cadena)

def explode_list_of_strings(lista_de_unalista):
    """
    aplica explode_string a cada cadena de lista
    """
    result = []
    for cada_cadena in lista_de_unalista:
        result.append(explode_string(cada_cadena))
    return result

def replace_all_in_list(original, old, new):
    """
    cambia todas las ocurrencias de old por new
    """
    result = []
    for elemen in original:
        if elemen == old:
            result.append(new)
        else:
            result.append(elemen)
    return result

def replace_all_in_matrix(original, old, new):
    """
    aplica replace_all_in_list en todas las listas
    """
    result = []
    for cada_list in original:
        result.append(replace_all_in_list(cada_list, old, new))
    return result