from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox



# Listados de precios
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

# Variable que guarda la vista de los botones pulsados de la calculadora
operador = ''

# Funcion de marcacion de botones de la calculadora
def click_boton(numero):
    global operador
    operador = operador + numero
    pantalla_calculadora.delete(0, END)
    pantalla_calculadora.insert(END,operador)

# Borrar calculadora
def borrar():
    global operador
    operador = ''
    pantalla_calculadora.delete(0, END)

# Calcular y obtener resultado
def obtener_resultado():
    global operador
    resultado = str( eval(operador))
    pantalla_calculadora.delete(0, END)
    pantalla_calculadora.insert(0, resultado)
    operador = ''

# Comprobar el check de las secciones comida, bebida y postre
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for b in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for p in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get() == '0':
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

# Calcular el total de la factura
def total():
    subtotal_comida = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comida = subtotal_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    subtotal_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    subtotal_postre = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postre = subtotal_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1

    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    var_precio_comida.set(f'{round(subtotal_comida, 2)} €')
    var_precio_bebida.set(f'{round(subtotal_bebida, 2)} €')
    var_precio_postre.set(f'{round(subtotal_postre, 2)} €')
    var_subtotal.set(f'{round(subtotal, 2)} €')
    var_impuesto.set(f'{round(impuestos, 2)} €')
    var_total.set(f'{round(total, 2)} €')

def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Factura:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, f'Productos\t\tCant.\tPrecio Productos\n')
    texto_recibo.insert(END, f'-' * 69 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t{int(comida.get()) * precios_comida[x]} €\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t{int(bebida.get()) * precios_bebida[x]} €\n')
        x += 1

    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t{int(postre.get()) * precios_postres[x]} €\n')
        x += 1

    texto_recibo.insert(END, f'-' * 69 + '\n')
    texto_recibo.insert(END, f'Precio Comida: \t\t\t{var_precio_comida.get()}\n')
    texto_recibo.insert(END, f'Precio Bebida: \t\t\t{var_precio_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio Postre: \t\t\t{var_precio_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 69 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 57 + '\n')
    texto_recibo.insert(END, '¡Gracias por su visita!')

# Guardar recibo como archivo
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'La factura se ha guardado correctamente.')

# Resetear la aplicacion
def resetear():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)

    var_precio_comida.set('')
    var_precio_bebida.set('')
    var_precio_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1160x630+0+0')

# Evitar maximizar la pantalla
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title('Mi Restaurante - Sistema de Facturación')

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4', font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de precios
panel_precios = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_precios.pack(side=BOTTOM)

# Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebida', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel de postres
panel_postres = LabelFrame(panel_izquierdo, text='Postre', font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comidas = ['Pollo', 'Pavo', 'Salmón', 'Atún', 'Arroz', 'Pasta', 'Garbanzos', 'Ensalada']
lista_bebidas = ['Agua', 'Café', 'Refresco', 'zumo', 'Cerveza', 'Vino', 'Infusión', 'Alcoholes']
lista_postres = ['Tarta', 'Galleta', 'Bollería', 'Helado', 'Yogurt', 'Fruta', 'Flan', 'Natillas']


# Variables comida
variables_comida = []
cuadros_comida = []
texto_comida = []

# Variable contador
contador = 0

# Bucles para generar check-buttons
for comida in lista_comidas:

    #crear checkbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)

    comida.grid(row=contador,
                column=0,
                sticky='w')

    # Crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Variables bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

# Variable contador
contador = 0

# Bucles para generar check-buttons
for bebida in lista_bebidas:

    # Crear checkbuttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)

    bebida.grid(row=contador,
                column=0,
                sticky='w')

    # Crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Variables postre
variables_postre = []
cuadros_postre = []
texto_postre = []

# Variable contador
contador = 0

# Bucles para generar check-buttons
for postre in lista_postres:

    # Crear checkbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)

    postre.grid(row=contador,
                column=0,
                sticky='w')

    # Crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Variable
var_precio_comida = StringVar()
var_precio_bebida = StringVar()
var_precio_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de precio y campos de entrada - Comida
etiqueta_precio_comida = Label(panel_precios,
                               text='Precio comida',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_comida.grid(row=0, column=0)

texto_precio_comida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_comida)
texto_precio_comida.grid(row=0,column=1, padx=41)


# Etiquetas de precio y campos de entrada - Bebida
etiqueta_precio_bebida = Label(panel_precios,
                               text='Precio bebida',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_bebida.grid(row=1, column=0)

texto_precio_bebida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_bebida)
texto_precio_bebida.grid(row=1,column=1, padx=41)

# Etiquetas de precio y campos de entrada - Postre
etiqueta_precio_postre = Label(panel_precios,
                               text='Precio postre',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_precio_postre.grid(row=2, column=0)

texto_precio_postre = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_postre)
texto_precio_postre.grid(row=2,column=1, padx=41)

# Etiquetas de precio y campos de entrada - Subtotal
etiqueta_subtotal = Label(panel_precios,
                               text='Subtotal',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)

# Etiquetas de precio y campos de entrada - Impuesto
etiqueta_impuesto = Label(panel_precios,
                               text='Impuesto',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3, padx=41)

# Etiquetas de precio y campos de entrada - Total
etiqueta_total = Label(panel_precios,
                               text='Total',
                               font=('Dosis',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)


# Botones
botones = ['total', 'recibo', 'giardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)

# Calculadora
pantalla_calculadora = Entry(panel_calculadora,
                             font=('Dosis', 16, 'bold'),
                             width=32,
                             bd=1)
pantalla_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','X','=','C','0','/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_guardados.append(boton)
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))





# Evitar que la pantalla se cierre
aplicacion.mainloop()

