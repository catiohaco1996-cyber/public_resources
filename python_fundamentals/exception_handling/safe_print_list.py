#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    """
    Imprime los primeros x elementos de una lista de forma segura y
    retorna el número real de elementos que se lograron imprimir.
    """
    contador = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            contador += 1
        except IndexError:
            break
    print("")  # Imprime la nueva línea requerida al final
    return contador
