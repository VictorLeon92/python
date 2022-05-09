def turno_perfumeria():
    for x in range(1, 9999):
        yield f"P - {x}"


def turno_farmacia():
    for x in range(1, 9999):
        yield f"F - {x}"


def turno_cosmetica():
    for x in range(1, 9999):
        yield f"C - {x}"

p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmetica()


def decoracion(area):

    print('Su turno es:')

    if area == 'P':
        print(next(p))
    elif area == 'F':
        print(next(f))
    else:
        print(next(c))

    print('Por favor, espere su turno')

