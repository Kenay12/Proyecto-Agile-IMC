from Control.CalculoIMC import CalculoIMCController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#funciones
def opcionCurso():
    print("Selecciona un curso: {}".format())
    return None

#inicializacion de la interfaz
ventanaImc = Tk()
ventanaImc.title("Sistema de seguimiento IMC")

#Variables
peso = IntVar()
altura = IntVar()
rut = StringVar()

# registro = CalculoIMCController.calcularIMC(peso, altura, rut)
# registro.__valor,registro.__rango, registro.__fecha, registro.__peso, registro.__altura, registro.__rut_estudiante



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
cursos = ["Curso 1", "Curso 2", "Curso 3", "Curso 4"]
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
labelRut = Label(infoImc, text='Rut: ')
entryPeso = Entry(infoImc, width=40, textvariable=peso,validate="key")
entryAltura = Entry(infoImc,width=40, textvariable=altura, validate="key")
entryRut = Entry(infoImc,width=40, textvariable=rut, validate="key")
labelPeso.grid(row=0, sticky=W)
labelAltura.grid(row=1,sticky=W)
labelRut.grid(row=2,sticky=W)
entryPeso.grid(row=0, column=1)
entryAltura.grid(row=1, column=1)
entryRut.grid(row=2, column=1)

def mostrar():
    CalculoIMCController().calcularIMC(peso.get(), altura.get(), rut.get())


#Boton Calcular
calculoIMC = Button(infoImc, text ="Calcular", command=mostrar)
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


# CalculoIMCController().calcularIMC(peso.get(), altura.get(), rut.get())



ventanaImc.mainloop()


# registro = CalculoIMCController.calcularIMC(peso, altura, rut)
# registro.__valor,registro.__rango, registro.__fecha, registro.__peso, registro.__altura, registro.__rut_estudiante