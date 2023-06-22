from tkinter import *
from tkinter import messagebox

from tkinter import ttk

#funciones
def opcionCurso():
    print("Selecciona un curso: {}".format(value_inside.get()))
    return None
def operacion():
    resultado = float(peso/(altura*altura))
    return resultado

#inicializacion de la interfaz
ventanaImc = Tk()
ventanaImc.title("Sistema de seguimiento IMC")

#Variables
peso = DoubleVar()
altura = DoubleVar()
resultado = DoubleVar()



#Frame
tituloFrame = Frame(ventanaImc)
tituloFrame.pack()

frame = Frame(ventanaImc)
frame.pack()

#Titulo
titulo = Label(tituloFrame,text="Sistema de seguimiento IMC")
titulo.pack()


#Legend
infoUsu = LabelFrame(frame,text="Seleccionar Curso")
infoUsu.grid(row=1,column=1)

#selecciona curso
cursos = ["Option 1", "Option 2", "Option 3", "Option 4"]
valCurso = StringVar(ventanaImc)
valCurso.set('Selecciona un Curso')
selecCurso = OptionMenu(infoUsu,valCurso,*cursos)
selecCurso.grid(row=0,column=0,)

#Caja de texto
cajaText = Text(infoUsu)
cajaText.configure(state="disabled")
cajaText.grid(row=3,columnspan=1)

#legend2
infoImc = LabelFrame(frame,text="Calculadora de IMC")
infoImc.grid(row=6,column=1,ipadx=40,ipady=20)

#Ingresar Imc
labelPeso = Label(infoImc, text='Peso (kg): ')
labelAltura = Label(infoImc, text='Altura (m): ')
labelEdad = Label(infoImc, text='Edad: ')
entryPeso = Entry(infoImc, width=40, textvariable=peso,validate="key")
entryAltura = Entry(infoImc,width=40, textvariable=altura, validate="key")
labelPeso.grid(row=0, sticky=W)
labelAltura.grid(row=1,sticky=W)
entryPeso.grid(row=0, column=1)
entryAltura.grid(row=1, column=1)


#Boton Calcular
calculoIMC = Button(infoImc, text ="Calcular")
calculoIMC.grid(row=7, column=1)

#legend3
infoResulImc = LabelFrame(frame,text="Resultados")
infoResulImc.grid(row=10,column=1,ipadx=40,ipady=10)

#caja de resultado y descriptivo
resultado = Label(infoResulImc, text="IMC =")
resultado.grid(row=0, column=0)
resulEntry = Entry(infoResulImc,width=40,state="disabled")
resulEntry.grid(row=0, column=1)
descriptivo = Label(infoResulImc, text="Descriptivo =")
descriptivo.grid(row=1, column=0)
descriptivo = Entry(infoResulImc,width=40,state="disabled")
descriptivo.grid(row=1, column=1)

#boton salir y regresar
buttonSalir = Button(frame, text ="Salir", command=ventanaImc
.destroy)
buttonSalir.grid(row=0, column=0)

buttonRegresar = Button(frame, text ="Regresar")
buttonRegresar.grid(row=0, column=2)







ventanaImc.mainloop()