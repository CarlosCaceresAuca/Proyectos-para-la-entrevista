def cambio_de_base(numero, base):
    lista = []
    q = numero
    while q != 0:
        lista.append(str(q % 8))
        q = (q//8)
    lista.reverse()
    return "".join(lista)

print(cambio_de_base(10,7))