from Control.CalculoIMC import CalculoIMCController
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#funciones
def mostrarAlumnos(curso):
    alumnos_por_curso = {
        "5to Basico": ["Bastian", "Nicolas", "Valencia"],
        "6to Basico": ["Vidal", "Medel", "Landeros"],
        "7to Basico": ["Guerra", "Assadi", "Sanchez"],
        "8vo Basico": ["Messi", "Julian", "Mono Sanchez"]
    }

    # Obtener la lista de alumnos correspondiente al curso seleccionado
    lista_alumnos = alumnos_por_curso[curso]

    # Limpiar el OptionMenu existente, si lo hay
    if valorAlumnoSelect[0] is not None:
        valorAlumnoSelect[0].destroy()

    # Crear un nuevo OptionMenu con la lista de alumnos
    alumno_var.set(lista_alumnos[0])  # Establecer el valor inicial
    valorAlumnoSelect[0] = OptionMenu(infoImc, alumno_var, *lista_alumnos)
    valorAlumnoSelect[0].grid(row=1,column=1)




#inicializacion de la interfaz
ventanaImc = Tk()
ventanaImc.title("Sistema de seguimiento IMC")

#Variables
peso = DoubleVar()
altura = DoubleVar()
rut = StringVar()
imc = StringVar()
rango = StringVar()

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


#legend2
infoImc = LabelFrame(frame,text="Calculadora de IMC")
infoImc.grid(row=6,column=1,ipadx=40,ipady=20)

# Crear un Combobox para seleccionar un curso
curso_label = Label(infoImc, text="Seleccione Curso:")
curso_label.grid(row=0, sticky=W)
cursos = ["5to Basico", "6to Basico", "7to Basico","8vo Basico"]
#definiremos las variables del los option menus
curso_var = StringVar(infoImc)
alumno_var = StringVar()

cursoSelect = OptionMenu(infoImc, curso_var, *cursos,command=mostrarAlumnos)
cursoSelect.grid(row=0,column=1)
valorAlumnoSelect = [None]



#Ingresar Imc

labelPeso = Label(infoImc, text='Peso (kg): ')
labelAltura = Label(infoImc, text='Altura (m): ')
labelRut = Label(infoImc, text='Rut: ')

entryPeso = Entry(infoImc, width=40, textvariable=peso,validate="key")
entryAlumno = Entry(infoImc, width=40, textvariable=peso,validate="key")
entryAltura = Entry(infoImc,width=40, textvariable=altura, validate="key")
entryRut = Entry(infoImc,width=40, textvariable=rut, validate="key")


labelPeso.grid(row=2, sticky=W)
labelAltura.grid(row=3,sticky=W)
labelRut.grid(row=4,sticky=W)

entryPeso.grid(row=2, column=1)
entryAltura.grid(row=3, column=1)
entryRut.grid(row=4, column=1)


def mostrar():
    valorPeso = peso.get()
    valorAltura = altura.get()
    valorRut = rut.get()
    registroIMC = CalculoIMCController().calcularIMC(valorPeso, valorAltura, valorRut)
    if isinstance(registroIMC, str):
        imc.set(registroIMC)
        rango.set(registroIMC)
    else:
        imc.set(registroIMC.valor)
        rango.set(registroIMC.rango)
    return registroIMC


#Boton Calcular
calculoIMC = Button(infoImc, text ="Calcular", command=mostrar)
calculoIMC.grid(row=7, column=1)

#legend3
infoResulImc = LabelFrame(frame,text="Resultados")
infoResulImc.grid(row=10,column=1,ipadx=40,ipady=10)

#caja de resultado y descriptivo
resultado = Label(infoResulImc, text="IMC =")
resultado.grid(row=0, column=0)
resulEntry = Entry(infoResulImc,width=40,state="disabled", textvariable=imc)
resulEntry.grid(row=0, column=1)
descriptivo = Label(infoResulImc, text="Descriptivo =")
descriptivo.grid(row=1, column=0)
descriptivo = Entry(infoResulImc,width=40,state="disabled", textvariable=rango)
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