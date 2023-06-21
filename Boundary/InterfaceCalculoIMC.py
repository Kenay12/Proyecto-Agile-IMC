from tkinter import *
from tkinter import messagebox

from tkinter import ttk

#funciones
def opcionCurso():
    print("Selecciona un curso: {}".format(value_inside.get()))
    return None


#inicializacion de la interfaz
ventanaImc = Tk()
ventanaImc.title("Sistema de seguimiento IMC")

#Variables
peso = StringVar()
altura = StringVar()
edad = IntVar()


#Frame
frame = Frame(ventanaImc)
frame.pack()

#Legend
infoUsu = LabelFrame(frame,text="Seleccionar Curso")
infoUsu.grid(row=0,column=0)

#selecciona curso
cursos = ["Option 1", "Option 2", "Option 3", "Option 4"]
valCurso = StringVar(ventanaImc)
valCurso.set('Selecciona un Curso')
selecCurso = OptionMenu(infoUsu,valCurso,*cursos)
selecCurso.grid(row=0,column=0)

#Caja de texto
cajaText = Text(infoUsu)
cajaText.configure(state="disabled")
cajaText.grid(row=3, columnspan=1)

#legend2
infoImc = LabelFrame(frame,text="Calculadora de IMC")
infoImc.grid(row=6,column=0)

#Ingresar Imc
labelPeso = Label(infoImc, text='Peso (kg): ')
labelAltura = Label(infoImc, text='Altura (m): ')
labelEdad = Label(infoImc, text='Edad: ')
entryPeso = Entry(infoImc, width=10, textvariable=peso,validate="key")
entryAltura = Entry(infoImc,width=10, textvariable=altura, validate="key")
entryEdad = Entry(infoImc,width=10, textvariable=edad, validate="key")
labelPeso.grid(row=0, sticky=W)
labelAltura.grid(row=1,sticky=W)
labelEdad.grid(row=2,sticky=W)
entryPeso.grid(row=0, column=1)
entryAltura.grid(row=1, column=1)
entryEdad.grid(row=2, column=1)

#caja de resultado
resultado = Label(infoImc, text="")
resultado.grid(row=4, columnspan=1)

#legend3
infoResulImc = LabelFrame(frame,text="Resultados")
infoResulImc.grid(row=10,column=0)

#mostrar resultado imc



#Boton Calcular
calculoIMC = Button(infoImc, text ="Calcular")
calculoIMC.grid(row=7, columnspan=1)


#boton salir y regresar
# buttonSalir = Button(ventanaImc, text ="Salir", command=ventanaImc
# .destroy)
# buttonSalir.grid(row=7, column=1)







ventanaImc.mainloop()