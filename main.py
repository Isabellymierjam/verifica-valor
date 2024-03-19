def verificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

numero = 10
resultado = verificar_numero(numero)

print(" O número", numero, "é", resultado + ".")