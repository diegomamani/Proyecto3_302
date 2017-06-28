from tkinter import *



import tkinter.messagebox
#Funcion Botones
def saluda ():
    lblSaludar = Label(ventana,text="Bienvenido: " + entradaU.get()+ " "+entradaN.get()+ "  ¿Que categoría deseas?").place(x=120,y=190)

ventana = Tk()
ventana.geometry("500x320+100+100")
ventana.title("Cine Star")
ventana.config(bg="white")

#SpinBox

#Radiobutton

def estado():
    s =selec.get()

    if s==1:
        tkinter.messagebox.showinfo("Categoria Drama","Se le recomienda ver Titanic")
    elif s==2:
        tkinter.messagebox.showinfo("Categoria Comedia","Se le recomienda ver Scary Movie")
    elif s==3:
        tkinter.messagebox.showinfo("Categoria Terror","Se le recomienda ver El exorcista")


fondo=PhotoImage(file="cinestar_paralax_bkg.gif")
lblFondo=Label(ventana,image=fondo).place(x=0,y=0)

selec= IntVar()
rdBAnimoE=Radiobutton(ventana,text="Drama",value=1,variable=selec,command=estado).place(x=10,y=220)
rdBAnimoF=Radiobutton(ventana,text="Comedia",value=2,variable=selec,command=estado).place(x=10,y=240)
rdBAnimoG=Radiobutton(ventana,text="Terror",value=3,variable=selec,command=estado).place(x=10,y=260)



#Cargar imagen

#Comandos maquinolas para el menu :V






#Cuadro de textirijillo
#Usuario
entradaU = StringVar()
txtMakinola = Entry(ventana,textvariable=entradaU,width=30).place(x=80, y=130)
lblNombre = Label(text= "Nombre").place(x=10 , y=130)

#Contraseña
entradaN = StringVar()
txtMakinola2 = Entry(ventana,textvariable=entradaN,width=30).place(x=80 , y=160)
lblNombre2 = Label(text= "Apellido").place(x=10 , y=160)
####lblUsuario.pack()




#Botonoes
btnSaludar = Button(ventana,text="Ingresar",command =saluda).place(x = 350,y = 140)




BarraMenu = Menu
ventana.mainloop()
