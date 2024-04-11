print("Semana 12: Ejercicio 1")
def es_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero

numero = int(input("Ingrese un número para verificar si es perfecto: "))

if es_perfecto(numero):
    print(numero, "es un número perfecto.")
else:
    print(numero, "no es un número perfecto.")

    print("Semana 12: Ejercicio 2")
    def calcular_pagos():
         cuota = 10.0  # Cuota inicial
    total_pagado = 0.0

    print("Proyección de pagos mensuales durante 12 meses:")
    for mes in range(1, 13):
        total_pagado += cuota # type: ignore
        print("Mes", mes, "- Cuota a pagar:", cuota) # type: ignore
    cuota*= 2  # type: ignore # Duplicar la cuota cada mes

    print("Total pagado después de 12 meses:", total_pagado)

calcular_pagos()

print("Semana 12: Ejercicio 3")
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")

print("Semana 12: Ejercicio 4")

def calcular_ahorro_semanal():
    ahorro_semanal = 0
    print("Día\tDepósito\tAhorro acumulado")
    for dia in range(1, 8):
        deposito = float(input(f"Ingrese la cantidad depositada el día {dia}: "))
        ahorro_semanal += deposito
        print(f"{dia}\t${deposito:.2f}\t\t${ahorro_semanal:.2f}")

calcular_ahorro_semanal()