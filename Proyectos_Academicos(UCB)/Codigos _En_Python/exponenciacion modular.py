def exponenciacion_modular(a, b):
    q = 0
    r = abs(a)
    while r>=b:
        r -= b
        q += 1
    if a<0 and r<0:
        r = b-r
    return f"""El cociente de {a}div{b} es {q}
El residuo de {a}mod{b} es {r}"""

print(exponenciacion_modular(9,3))