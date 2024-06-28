from ConfigVisual import *

class ventanas:
    def __init__(self, root):
        self.root = root
        self.root.title("Universidad de Lima")
        self.root.resizable(False, False)
        self.root.iconbitmap("Images/estrella.ico") 
        self.root.geometry("1280x720")
        

        self.cargar_imagen_fondo("Images/universidad.png")  

        self.ventmid = Frame(self.root)
        self.configuracion_mid(self.ventmid)
        configurar_botones(self.ventmid)

    def cargar_imagen_fondo(self, image_path):
        self.bg_image = PhotoImage(file=image_path) 
        bg_label = Label(self.root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

    def configuracion_mid(self, ventmid):
        ventmid.config(bg="white")
        ventmid.config(width=900, height=900)
        ventmid.place(relx=0.5, rely=0.5, anchor=CENTER)
     
if __name__ == "__main__":
    root = Tk()
    app = ventanas(root)
    root.mainloop()



