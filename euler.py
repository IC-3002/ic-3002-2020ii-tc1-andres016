def e_cuadratica(n):
    # Implemente esta función   
    i = 0
    e = 0
    while i==e:
        while i < n:
            e = e + 1/factorial(i)
            i = i + 1
    return e


def e_lineal(n):
    # Implemente esta función
    i = 0
    e = 0

    while i < n:
        e = e + 1/factorial(i)
        i = i + 1
    return e
 
def factorial(numero):
    resultado=1
    for i in range(1, numero+1):
        resultado=resultado*i
    return resultado
