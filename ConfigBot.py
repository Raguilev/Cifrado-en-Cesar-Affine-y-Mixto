from Intermid import *
from Cifrados import *
def configurar_botones(ventmid):
    etiqueta_archivo = Label(ventmid, text="No se ha seleccionado ningún archivo.")
    etiqueta_archivo.pack(pady=10) 
    
    texto = [None]

    boton_archivo = Button(ventmid, text="Seleccionar Archivo", command=lambda: texto.append(seleccionar_archivo(etiqueta_archivo)))
    boton_archivo.pack(pady=20)

    etiqueta_texto = Label(ventmid, text="Aquí se mostrará el texto.")
    etiqueta_texto.pack(pady=10)

    boton_original = Button(ventmid, text="Texto Original", command=lambda: mostrar_texto(texto[-1], etiqueta_texto))
    boton_original.pack(pady=5)

    boton_cesar = Button(ventmid, text="Cifrado César", command=lambda: mostrar_texto(cifrado_cesar(texto[-1]), etiqueta_texto))
    boton_cesar.pack(pady=5)

    boton_affine = Button(ventmid, text="Cifrado Afín", command=lambda: mostrar_texto(cifrado_affine(texto[-1]), etiqueta_texto))
    boton_affine.pack(pady=5)

    boton_mixto = Button(ventmid, text="Cifrado Mixto", command=lambda: mostrar_texto(cifrado_mixto(texto[-1]), etiqueta_texto))
    boton_mixto.pack(pady=5)

    boton_guardar_cesar = Button(ventmid, text="Guardar César", command=lambda: guardar_archivo(cifrado_cesar(texto[-1]), "César"))
    boton_guardar_cesar.pack(pady=5)

    boton_guardar_affine = Button(ventmid, text="Guardar Afín", command=lambda: guardar_archivo(cifrado_affine(texto[-1]), "Afín"))
    boton_guardar_affine.pack(pady=5)

    boton_guardar_mixto = Button(ventmid, text="Guardar Mixto", command=lambda: guardar_archivo(cifrado_mixto(texto[-1]), "Mixto"))
    boton_guardar_mixto.pack(pady=5)