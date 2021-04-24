def exchanges(tipo_pesos, valor_dolar):
    pesos = input("¿Cúantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes  $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    exchanges("colombianos", 3875)
elif opcion == 2:
    exchanges("argentinos", 65)
elif opcion == 3:
    exchanges("MEXICANOS", 19.85)
else:
    print("Ingresa una opción correcta por favor")