from tkinter import *
from tkinter import filedialog
import pandas as pd

def seleccionar_archivo(etiqueta):
    ruta = filedialog.askopenfilename(title="Seleccionar Archivo", filetypes=[("CSV files", "*.csv")])
    if ruta:
        try:
            df = pd.read_csv(ruta)
            texto = df.to_string(index=False)
            etiqueta.config(text=f"Archivo seleccionado: {ruta}")
            return texto
        except Exception as e:
            etiqueta.config(text=f"Error al leer el archivo: {e}")
            return None
    return None

def mostrar_texto(texto, etiqueta):
    etiqueta.config(text=texto)

def guardar_archivo(texto, metodo):
    ruta = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
                                        title=f"Guardar archivo {metodo}")
    if ruta:
        try:
            with open(ruta, 'w', encoding='utf-8') as file:
                file.write(texto)
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")




