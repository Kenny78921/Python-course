from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox
#$ Iniciar aplicacion
aplicacion = Tk()

#$ Ajustar tamaño
aplicacion.geometry("1020x630+500+200")

#$ Evitar reescalamiento
aplicacion.resizable(0,0)

#$ Personalizar pantalla
aplicacion.title("App")
aplicacion.config(bg="pink")

#$ Contenido
panel_titulo = Frame(aplicacion, bd=1, relief=FLAT)
panel_titulo.pack(side=TOP)
etiqueta_titulo = Label(panel_titulo, text="Prueba", fg="azure4", font=("Victor_Mono", 50), bg="burlywood", width=21)
etiqueta_titulo.grid(row=0, column=0)

#! costos
def total():
    subtotal_comidas = 0
    p = 0
    for cantidad in texto_comida:
        subtotal_comidas = subtotal_comidas + (float(cantidad.get()) * precios_comidas[p])
        p +=1
    subtotal_bebidas = 0
    p = 0
    for cantidad in texto_bebida:
        subtotal_bebidas = subtotal_bebidas + (float(cantidad.get()) * precios_bebidas[p])
        p +=1
    subtotal_postres = 0
    p = 0
    for cantidad in texto_postre:
        subtotal_postres = subtotal_postres + (float(cantidad.get()) * precios_postres[p])
        p +=1

    subtotal = subtotal_comidas + subtotal_bebidas + subtotal_postres
    impuestos = subtotal * 1.16
    total = subtotal + impuestos

    var_costo_comidas.set(f"$ {round(subtotal_comidas,2)}")
    var_costo_bebidas.set(f"$ {round(subtotal_bebidas,2)}")
    var_costo_postres.set(f"$ {round(subtotal_postres,2)}")
    var_costo_subtotal.set(f"$ {round(subtotal,2)}")
    var_costo_impuestos.set(f"$ {round(impuestos,2)}")
    var_costo_total.set(f"$ {round(total,2)}")

def recibo():
    texto_recibo.delete(1.0,END)
    num_recibo = f"N# - {random.randint(1000,9999)}"
    fecha = datetime.datetime.now()
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha}\n")
    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t"
                                f"${round((int(comida.get()) * precios_comidas[x]),2)}\n")
        x+=1
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t"
                                f"${round((int(bebida.get()) * precios_bebidas[x]),2)}\n")
        x+=1
    x = 0
    for postre in texto_postre:
        if postre.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postre.get()}\t"
                                f"${round((int(postre.get()) * precios_postres[x]),2)}\n")
        x+=1

#!
def guardar():
    infor_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(infor_recibo)
    archivo.close()
    messagebox.showinfo("Recibo guardado")

def resetear():
    texto_recibo.delete(0.1,END)
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postre:
        texto.set("0")

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
    
    var_costo_comidas.set("")
    var_costo_bebidas.set("")
    var_costo_postres.set("")
    var_costo_subtotal.set("")
    var_costo_impuestos.set("")
    var_costo_total.set("")


#° Calculadora
operador = ""
def click_boton(numeros):
    global operador
    operador = operador + numeros
    pantalla_calculadora.delete(0, END)
    pantalla_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    pantalla_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    pantalla_calculadora.delete(0, END)
    pantalla_calculadora.insert(0, resultado)
    operador = ""

#! Etriqueta menu
#% Panel de menu
panel_menu = Frame(aplicacion, bd=1, relief=FLAT)
panel_menu.place(x=10, rely=0.8, anchor='sw')

panel_comidas = LabelFrame(panel_menu, text = "Comidas", font=("Victor_Mono", 25), bd=1 ,relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_menu, text = "Bebidas", font=("Victor_Mono", 25), bd=1 ,relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_menu, text = "Postres", font=("Victor_Mono", 25), bd=1 ,relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

#% Panel de menu

panel_costos = Frame(aplicacion, bd=1, relief=FLAT, bg = "azure4", padx=45)
panel_costos.place(x=10, rely=0.98, anchor='sw')

panel_calculadora = Frame(aplicacion, bd=1, relief=FLAT)
panel_calculadora.place(x=738, rely=0.48, anchor='sw')

panel_recibo = Frame(aplicacion, bd=1, relief=FLAT)
panel_recibo.place(x=750, rely=0.88, anchor='sw')

panel_botones = Frame(aplicacion, bd=1, relief=FLAT)
panel_botones.place(x=750, rely=0.98, anchor='sw')

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x+=1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get == "0":
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x+=1
    x = 0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            cuadros_postre[x].config(state=NORMAL)
            if cuadros_postre[x].get == "0":
                cuadros_postre[x].delete(0, END)
            cuadros_postre[x].focus()
        else:
            cuadros_postre[x].config(state=DISABLED)
            texto_postre[x].set("0")
        x+=1
        

#% Listas de variables
lista_comidas = ["Pizza_1","Pizza_2","Pizza_3","Pizza_4","Pizza_5","Pizza_6","Pizza_7","Pizza_8"]
variables_comida = []
cuadros_comida = []
texto_comida = []

lista_bebidas = ["Agua_1","Agua_2","Agua_3","Agua_4","Agua_5","Agua_6","Agua_7","Agua_8"]
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

lista_postres = ["Pay_1","Pay_2","Pay_3","Pay_4","Pay_5","Pay_6","Pay_7","Pay_8"]
variables_postre = []
cuadros_postre = []
texto_postre = []

lista_vacia_espacios = [" "," "," "," "," "," "," "," "]

precios_comidas = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebidas = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

#° Checkbuttons y labels
contador = 0
for comida in lista_comidas:
    #% Checkbuttons comidas
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=("Victor_Mono", 15), onvalue=1, offvalue=0, variable = variables_comida[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)

    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set(0)

    cuadros_comida[contador] = Entry(panel_comidas, font=("Victor_Mono", 15), width=6, state=DISABLED, textvariable=texto_comida[contador] )
    cuadros_comida[contador].grid(row=contador, column=1, sticky=W)

    lista_vacia_espacios[contador]= Label(panel_comidas, width=2)
    lista_vacia_espacios[contador].grid(row=contador, column=2, sticky=W)


    contador +=1

contador = 0
for bebida in lista_bebidas:
    #% Checkbuttons bebidas
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Victor_Mono", 15), onvalue=1, offvalue=0, variable = variables_bebida[contador], command=revisar_check)
    bebida.grid(row=contador, column=3, sticky=W)

    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set(0)

    cuadros_bebida[contador] = Entry(panel_bebidas, font=("Victor_Mono", 15), width=6, state=DISABLED, textvariable=texto_bebida[contador] )
    cuadros_bebida[contador].grid(row=contador, column=4, sticky=W)

    lista_vacia_espacios[contador]= Label(panel_bebidas, width=2)
    lista_vacia_espacios[contador].grid(row=contador, column=5, sticky=W)
    contador +=1

contador = 0
for postre in lista_postres:
    #% Checkbuttons postres
    variables_postre.append("")
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=("Victor_Mono", 15), onvalue=1, offvalue=0, variable = variables_postre[contador], command=revisar_check)
    postre.grid(row=contador, column=6, sticky=W)

    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set(0)

    cuadros_postre[contador] = Entry(panel_postres, font=("Victor_Mono", 15), width=6, state=DISABLED, textvariable= texto_postre[contador] )
    cuadros_postre[contador].grid(row=contador, column=7, sticky=W)

    lista_vacia_espacios[contador]= Label(panel_postres, width=2)
    lista_vacia_espacios[contador].grid(row=contador, column=8, sticky=W)
    contador +=1

#° Etiquetas de costo y campos de entrada
#% Costos comida
etiqueta_costo_comida = Label(panel_costos, text="  Costo comida  ", font=("Victor_Mono", 15), bg = "azure4",fg="white")
etiqueta_costo_comida.grid(row=0,column=0, padx=20)



#% Costos bebidas
etiqueta_costo_bebida = Label(panel_costos, text="  Costo bebida  ", font=("Victor_Mono", 15), bg = "azure4",fg="white")
etiqueta_costo_bebida.grid(row=1,column=0, padx=20)


#% Costos postre
etiqueta_costo_postre = Label(panel_costos, text="  Costo postre  ", font=("Victor_Mono", 15), bg = "azure4",fg="white")
etiqueta_costo_postre.grid(row=2,column=0, padx=20)



#% subtotal
etiqueta_costo_subtotal = Label(panel_costos, text="  Subtotal  ", font=("Victor_Mono", 15), bg = "azure4",fg="white")
etiqueta_costo_subtotal.grid(row=0,column=3, padx=20)


#% impuestos
etiqueta_costo_impuestos = Label(panel_costos, text="  Impuestos  ", font=("Victor_Mono", 15), bg = "azure4",fg="white")
etiqueta_costo_impuestos.grid(row=1,column=3, padx=20)


#% total
etiqueta_costo_total = Label(panel_costos, text="  Total  ", font=("Victor_Mono", 15), bg = "azure4",fg="white")
etiqueta_costo_total.grid(row=2,column=3, padx=20)


#° Botones
botones = ["total","recibo", "guardar", "resetear"]
boton_creado = []
columnas = 0
filas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("Victor_Mono", 15), bg = "azure4", fg = "white", width = 10, height=1)
    boton.grid(row=filas,column=columnas, padx=0)
    columnas +=1
    if columnas == 2:
        filas = 1
        columnas = 0
    boton_creado.append(boton)

boton_creado[0].config(command=total)
boton_creado[1].config(command=recibo)
boton_creado[2].config(command=guardar)
boton_creado[3].config(command=resetear)

#° Recibo
texto_recibo = Text(panel_recibo, bd = 2, width = 29, height=15)
texto_recibo.grid(row=0, column=0)

#° Calculadora
calculadora = ["7","8","9","+","4","5","6","-","1","2","3","x","=","B","0","/"]
botones_guardados = []
filas = 1
columnas = 0
pantalla_calculadora = Entry(panel_calculadora, font=("Victor_Mono", 15), width=20)
pantalla_calculadora.grid(row=0,column=0, columnspan=4)

for botones_calculadora in calculadora:
    botones_calculadora = Button(panel_calculadora, text=botones_calculadora.title(), font=("Victor_Mono", 15), bg = "azure4", fg = "white", width = 4)
    botones_calculadora.grid(row=filas,column=columnas, padx=0)
    columnas += 1
    if columnas == 4:
        columnas = 0
        filas += 1
    botones_guardados.append(botones_calculadora)

botones_guardados[0].config(command=lambda: click_boton("7"))
botones_guardados[1].config(command=lambda: click_boton("8"))
botones_guardados[2].config(command=lambda: click_boton("9"))
botones_guardados[3].config(command=lambda: click_boton("+"))
botones_guardados[4].config(command=lambda: click_boton("4"))
botones_guardados[5].config(command=lambda: click_boton("5"))
botones_guardados[6].config(command=lambda: click_boton("6"))
botones_guardados[7].config(command=lambda: click_boton("-"))
botones_guardados[8].config(command=lambda: click_boton("1"))
botones_guardados[9].config(command=lambda: click_boton("2"))
botones_guardados[10].config(command=lambda: click_boton("3"))
botones_guardados[11].config(command=lambda: click_boton("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[15].config(command=lambda: click_boton("0"))
botones_guardados[15].config(command=lambda: click_boton("/"))

var_costo_comidas = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuestos = StringVar()
var_costo_total = StringVar()

#% Costos

texto_costo_comida = Entry(panel_costos, font=("Victor_Mono", 15), bd=1, width=10,state="readonly", textvariable=var_costo_comidas)
texto_costo_comida.grid(row = 0, column=2)

texto_costo_bebidas = Entry(panel_costos, font=("Victor_Mono", 15), bd=1, width=10,state="readonly", textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row = 1, column=2)

texto_costo_postre = Entry(panel_costos, font=("Victor_Mono", 15), bd=1, width=10,state="readonly", textvariable=var_costo_postres)
texto_costo_postre.grid(row = 2, column=2)

texto_costo_subtotal = Entry(panel_costos, font=("Victor_Mono", 15), bd=1, width=10,state="readonly", textvariable=var_costo_subtotal)
texto_costo_subtotal.grid(row = 0, column=4)

texto_costo_impuestos = Entry(panel_costos, font=("Victor_Mono", 15), bd=1, width=10,state="readonly", textvariable=var_costo_impuestos)
texto_costo_impuestos.grid(row = 1, column=4)

texto_costo_total = Entry(panel_costos, font=("Victor_Mono", 15), bd=1, width=10,state="readonly", textvariable=var_costo_total)
texto_costo_total.grid(row = 2, column=4)

#$ Evitar que se cierre
aplicacion.mainloop()