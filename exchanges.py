menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cúantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cúantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cúantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 19.85
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")
else:
    print("Ingresa una opción correcta por favor")