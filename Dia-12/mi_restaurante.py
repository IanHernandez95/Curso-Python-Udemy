from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1320, 1650, 2310, 3220, 1220, 1990, 2050, 2650]
precios_bebida = [250, 990, 1210, 1540, 1080, 1100, 2000, 1580]
precios_postre = [1540, 1680, 1320, 1970, 2550, 2140, 1940, 1740]

# Funciones

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0 , END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_comida[x].get() == 0:
                cuadros_comida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postre[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 0)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 0)}')
    var_costo_postre.set(f'$ {round(sub_total_postres, 0)}')
    var_subtotal.set(f'$ {round(sub_total, 0)}')
    var_impuesto.set(f'$ {round(impuestos, 0)}')
    var_total.set(f'$ {round(total, 0)}')

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 42 + '\n' )
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 67 + '\n' )

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t\t$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1
    
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t\t$ {int(postre.get()) * precios_postre[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 67 + '\n' )
    texto_recibo.insert(END, f'Costo de la Comida:\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Bebida:\t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de la Postre:\t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 67 + '\n' )
    texto_recibo.insert(END, f'Costo de la Sub-Total:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Costo de la Impuesto:\t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Costo de la Total:\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 42 + '\n' )
    texto_recibo.insert(END, f'Lo esperamos Pronto' )

def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo a sido guardado')

def reset():
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
    
    for variable in variables_comida:
        variable.set(0)
    for variable in variables_bebida:
        variable.set(0)
    for variable in variables_postre:
        variable.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')



# Iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar Maximizar
aplicacion.resizable(0, 0)

# Titulo de la Ventana
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

# Color de Fondo de la ventana
aplicacion.config(bg='burlywood')


# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Calibri',55), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costo
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=25)
panel_costo.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas', font=('Calibri',19,'bold'), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Calibri',19,'bold'), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Calibri',19,'bold'), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comidas = ['Pollo','Cordero','Reineta','Merluza','Pizza','Kebab','Sushi','Hamburguesa']
lista_bebidas = ['Agua','Soda','Jugo','Cafe','Te','Cerveza','Vino','Cola-Cola']
lista_postres = ['Helado','Fruta','Torta','Galletas','Brownie','Mousse','Panqueque','Flan']

# Generar items Comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # CheckButtons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                        text=comida.title(), 
                        font=('Calibri',15,'bold'), 
                        onvalue=1, 
                        offvalue=0, 
                        variable=variables_comida[contador],
                        command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    # Crear cuadros de entrada}
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                    font=('calibri',15,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                column=1)

    contador += 1


# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:

    # Crear Checkbuttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, 
                        text=bebida.title(), 
                        font=('Calibri',15,'bold'), 
                        onvalue=1, 
                        offvalue=0, 
                        variable=variables_bebida[contador],
                        command=revisar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    
    # Crear cuadros de entrada}
    cuadros_bebida.append('')
    texto_bebida.append('')    
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                    font=('calibri',15,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                column=1)

    contador += 1

# Generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:

    # Crear Checkbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, 
                        text=postre.title(), 
                        font=('Calibri',15,'bold'), 
                        onvalue=1, 
                        offvalue=0, 
                        variable=variables_postre[contador],
                        command=revisar_check)
    postre.grid(row=contador, 
                column=0, 
                sticky=W)
    
    # Crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                    font=('calibri',15,'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                column=1)

    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costo,
                            text='Costo Comida',
                            font=('Calibri',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costo,
                        font=('Calibri',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costo,
                            text='Costo bebida',
                            font=('Calibri',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costo,
                        font=('Calibri',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postre = Label(panel_costo,
                            text='Costo postre',
                            font=('Calibri',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costo,
                        font=('Calibri',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)


etiqueta_subtotal = Label(panel_costo,
                            text='Subtotal',
                            font=('Calibri',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_subtotal.grid(row=0, column=2, padx=41)

texto_subtotal = Entry(panel_costo,
                        font=('Calibri',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuesto = Label(panel_costo,
                            text='Impuesto',
                            font=('Calibri',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costo,
                        font=('Calibri',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costo,
                            text='Total',
                            font=('Calibri',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costo,
                        font=('Calibri',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                        font=('Calibri', 14, 'bold'),
                        width=32,
                        bd=1)
visor_calculadora.grid(row=0,
                        column=0,
                        columnspan=4)

botones_calculadora = ['7','8','9','+',
                    '4','5','6','-',
                    '1','2','3','x',
                    'R','B','0','/']

botones_guadados = []

fila = 1
columna = 0
for btn in botones_calculadora:
    btn = Button(panel_calculadora,
                text=btn.title(),
                font=('calibri', 14, 'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=8)
    btn.grid(row=fila,
            column=columna)

    botones_guadados.append(btn)
    
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guadados[0].config(command=lambda : click_boton('7'))
botones_guadados[1].config(command=lambda : click_boton('8'))
botones_guadados[2].config(command=lambda : click_boton('9'))
botones_guadados[3].config(command=lambda : click_boton('+'))
botones_guadados[4].config(command=lambda : click_boton('4'))
botones_guadados[5].config(command=lambda : click_boton('5'))
botones_guadados[6].config(command=lambda : click_boton('6'))
botones_guadados[7].config(command=lambda : click_boton('-'))
botones_guadados[8].config(command=lambda : click_boton('1'))
botones_guadados[9].config(command=lambda : click_boton('2'))
botones_guadados[10].config(command=lambda : click_boton('3'))
botones_guadados[11].config(command=lambda : click_boton('*'))
botones_guadados[12].config(command=obtener_resultado)
botones_guadados[13].config(command=borrar)
botones_guadados[14].config(command=lambda : click_boton('0'))
botones_guadados[15].config(command=lambda : click_boton('/'))



# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=('calibri', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0, column=0)



#Botones
botones = ['Total','Recibo','Guardar','Reset']
botones_creados = []
columnas = 0
for btn in botones:
    btn = Button(panel_botones,
                text=btn.title(),
                font=('calibri', 14, 'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=9)
    
    botones_creados.append(btn)

    btn.grid(row=0, column=columnas)

    columnas += 1


botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)


# Evitar que la pantalla se cierre
aplicacion.mainloop()