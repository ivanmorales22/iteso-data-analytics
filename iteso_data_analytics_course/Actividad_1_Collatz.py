## Actividad 1 05/02/2024 Programacion para analisis de Datos
## Activity: Collatz Sequence Length Finder
## Ivan Morales

def secuencia_collatz(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia

def encontrar_secuencia_collatz_mas_larga(a, b):
    longitud_maxima = 0
    numero_con_secuencia_mas_larga = 0

    for i in range(a, b + 1):
        longitud_actual = len(secuencia_collatz(i))
        if longitud_actual > longitud_maxima:
            longitud_maxima = longitud_actual
            numero_con_secuencia_mas_larga = i

    return numero_con_secuencia_mas_larga, longitud_maxima

# Ejemplo de uso
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

resultado = encontrar_secuencia_collatz_mas_larga(a, b)
print(f"El número con la secuencia más larga es {resultado[0]} con una longitud de {resultado[1]}")
