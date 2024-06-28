from ConfigArchi import *
from ConfigCifra import *
from tkinter import Tk, Label, Button, OptionMenu, StringVar

def configurar_botones(ventmid):
    etiqueta_archivo = Label(ventmid, text="No se ha seleccionado ningún archivo.")
    etiqueta_archivo.pack(pady=10)
    
    texto = [None]
    texto_actual = [None]

    boton_archivo = Button(ventmid, text="Seleccionar Archivo", command=lambda: texto.append(seleccionar_archivo(etiqueta_archivo)))
    boton_archivo.pack(pady=20)

    etiqueta_texto = Label(ventmid, text="Aquí se mostrará el texto.")
    etiqueta_texto.pack(pady=10)

    # Opciones para visualizar el cifrado
    opciones_visualizacion = ["Texto Original", "Cifrado César", "Cifrado Afín", "Cifrado Mixto"]
    seleccion_visualizacion = StringVar(ventmid)
    seleccion_visualizacion.set(opciones_visualizacion[0])

    def actualizar_visualizacion():
        if seleccion_visualizacion.get() == "Texto Original":
            texto_actual[0] = texto[-1]
        elif seleccion_visualizacion.get() == "Cifrado César":
            texto_actual[0] = cifrado_cesar(texto[-1])
        elif seleccion_visualizacion.get() == "Cifrado Afín":
            texto_actual[0] = cifrado_affine(texto[-1])
        elif seleccion_visualizacion.get() == "Cifrado Mixto":
            texto_actual[0] = cifrado_mixto(texto[-1])
        mostrar_texto(texto_actual[0], etiqueta_texto)

    menu_visualizacion = OptionMenu(ventmid, seleccion_visualizacion, *opciones_visualizacion, command=lambda _: actualizar_visualizacion())
    menu_visualizacion.pack(pady=5)

    def guardar_seleccion():
        if seleccion_visualizacion.get() == "Texto Original":
            guardar_archivo(texto_actual[0], "Original")
        elif seleccion_visualizacion.get() == "Cifrado César":
            guardar_archivo(texto_actual[0], "César")
        elif seleccion_visualizacion.get() == "Cifrado Afín":
            guardar_archivo(texto_actual[0], "Afín")
        elif seleccion_visualizacion.get() == "Cifrado Mixto":
            guardar_archivo(texto_actual[0], "Mixto")

    boton_guardar = Button(ventmid, text="Guardar", command=guardar_seleccion)
    boton_guardar.pack(pady=5)