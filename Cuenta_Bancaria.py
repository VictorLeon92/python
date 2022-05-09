from random import randint

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente (Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Nombre:{self.nombre} {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}'

    def __del__(self):
        print('¡Hasta la próxima!')

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f'Has depositado {cantidad}.\nAhora tienes {self.balance} en tu cuenta.')

    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f'Has retirado {cantidad}.\nAhora tienes {self.balance} en tu cuenta.')
        else:
            print('Fondos insuficientes.')


# Función crear cliente: Pedir todos los datos y almacenarlos en una instancia de la clase

def crear_cliente():
    print('Bienvenido/a. Introduce tus datos.')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    cuenta = input('Número de cuenta: ')
    saldo = randint(10000,50000)
    nuevo_cliente = Cliente(nombre, apellido, cuenta, saldo)

    return nuevo_cliente

# función inicio y trámites: Realizar bucle de operaciones hasta que el cliente quiera salir y no permitir returar más dinero del que hay

def inicio():
    cliente = crear_cliente()
    print(f'''{cliente}
    ¿Qué quieres hacer?''')

    opcion = 0
    while opcion != 'S':
        print('''Elige una opción:
        [D] Depositar efectivo
        [R] Retirar saldo
        [S] Salir''')
        opcion = input()

        if opcion == 'D':
            importe_dep = int(input('¿Cuánto quieres ingresar?: '))
            cliente.depositar(importe_dep)
        elif opcion == 'R':
            importe_ret = int(input('¿Cuánto quieres retirar?: '))
            cliente.retirar(importe_ret)

        print(cliente)

    del cliente


inicio()
