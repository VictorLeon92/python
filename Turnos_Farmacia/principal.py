import numeros

def preguntar():
    print('Biemvemod@,')

    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica')
        try:
            mi_area = input('Elija el area que desea visitar: ').upper()
            ['P','F','C'].index(mi_area)
        except ValueError:
            print('Por favor, introduzca una opción válida')
        else:
            break

    numeros.decoracion(mi_area)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('¿Quieres sacar otro número?\n[S] - Si\n[N] - No\n').upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('Por favor, introduzca una opción válida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break

inicio()