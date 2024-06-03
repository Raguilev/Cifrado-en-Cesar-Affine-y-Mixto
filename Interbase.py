from ConfigBot import *
ventana=Tk()

ventana.title("Universidad de Lima")
ventana.resizable(False,False) 
ventana.iconbitmap("estrella.ico")
ventana.geometry("1024x720")
ventana.config(bg="grey")

ventmid = Frame(ventana)
ventmid=configuracion_mid(ventmid)
configurar_botones(ventmid)

ventana.mainloop() 
