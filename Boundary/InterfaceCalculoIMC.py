from Control.CalculoIMC import CalculoIMCController
from Control.EstudianteController import EstudianteController
from tkinter import *
from tkinter import messagebox, ttk


class InterfaceCalculadoraIMC:
    def __init__(self):
        #funciones
        def mostrarAlumnos(curso):
            alumnos_por_curso = {
                "Quinto Básico A": [EstudianteController("11.111.111-1", "Bastián", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("22.222.222-2", "Nicolás", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("33.333.333-3", "Valencia", "Zarate", "01-01-2000", 1, 1)],
                "Quinto Básico B": [EstudianteController("44.444.444-4", "Vidal", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("55.555.555-5", "Medel", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("66.666.666-6", "Landeros", "Zarate", "01-01-2000", 1, 1)],
                "Sexto Básico A":  [EstudianteController("77.777.777-7", "Guerra", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("88.888.888-8", "Assadi", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("99.999.999-9", "Sanchez", "Zarate", "01-01-2000", 1, 1)],
                "Sexto Básico B":  [EstudianteController("12.345.678-9", "Messi", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("98.765.432-1", "Julian", "Zarate", "01-01-2000", 1, 1),
                                    EstudianteController("00.000.000-0", "Mono", "Sanchez", "01-01-2000", 1, 1)]
            }

            # Obtener la lista de alumnos correspondiente al curso seleccionado
            lista_alumnos = []
            for alumno in alumnos_por_curso[curso]:
                lista_alumnos.append("{} - {} {}".format(alumno.rut, alumno.nombres, alumno.apellidos))

            # Limpiar el OptionMenu existente, si lo hay
            if valorAlumnoSelect[0] is not None:
                valorAlumnoSelect[0].destroy()

            # Crear un nuevo OptionMenu con la lista de alumnos
            alumno_var.set(lista_alumnos[0])  # Establecer el valor inicial

            alumno_label = Label(infoImc, text="Seleccione Alumno:")
            alumno_label.grid(row=1, column=0)
            valorAlumnoSelect[0] = OptionMenu(infoImc, alumno_var, *lista_alumnos)
            valorAlumnoSelect[0].grid(row=1, column=1)

        #inicializacion de la interfaz
        ventanaImc = Tk()
        ventanaImc.title("Sistema de seguimiento IMC")

        #Variables
        peso = DoubleVar()
        altura = DoubleVar()
        imc = StringVar()
        rango = StringVar()

        #Frame
        tituloFrame = Frame(ventanaImc)
        tituloFrame.pack()

        frame = Frame(ventanaImc)
        frame.pack()

        #Titulo
        titulo = Label(tituloFrame, text="Sistema de seguimiento IMC")
        titulo.pack()

        #legend2
        infoImc = LabelFrame(frame, text="Calculadora de IMC")
        infoImc.grid(row=6, column=1, ipadx=40, ipady=6)

        # Crear un Combobox para seleccionar un curso
        curso_label = Label(infoImc, text="Seleccione Curso:")
        curso_label.grid(row=0, sticky=W)
        cursos = ["Quinto Básico A", "Quinto Básico B", "Sexto Básico A", "Sexto Básico B"]
        #definiremos las variables del los option menus
        curso_var = StringVar(infoImc)
        alumno_var = StringVar()

        cursoSelect = OptionMenu(infoImc, curso_var, *cursos, command=mostrarAlumnos)
        cursoSelect.grid(row=0, column=1)
        valorAlumnoSelect = [None]

        #Ingresar Imc

        labelPeso = Label(infoImc, text='Peso (kg): ')
        labelAltura = Label(infoImc, text='Altura (m): ')

        entryPeso = Entry(infoImc, width=40, textvariable=peso,validate="key")
        entryAltura = Entry(infoImc, width=40, textvariable=altura, validate="key")

        labelPeso.grid(row=2, sticky=W)
        labelAltura.grid(row=3, sticky=W)

        entryPeso.grid(row=2, column=1)
        entryAltura.grid(row=3, column=1)

        def calculoIMC():
            valorPeso = peso.get()
            valorAltura = altura.get()
            valorRut = alumno_var.get().split(" - ")[0]
            registroIMC = CalculoIMCController().calcularIMC(valorPeso, valorAltura, valorRut)
            if isinstance(registroIMC, str):
                imc.set(registroIMC)
                rango.set(registroIMC)
            else:
                imc.set(registroIMC.valor)
                rango.set(registroIMC.rango)
            return registroIMC


        #Boton Calcular
        calculoIMC = Button(infoImc, text="Calcular", command=calculoIMC)
        calculoIMC.grid(row=6, column=1, pady=6)

        #legend3
        infoResulImc = LabelFrame(frame, text="Resultados")
        infoResulImc.grid(row=9,column=1,ipadx=40,ipady=10)

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
        buttonSalir = Button(frame, text="Salir", command=ventanaImc.destroy)
        buttonSalir.grid(row=0, column=0)

        buttonRegresar = Button(frame, text="Regresar")
        buttonRegresar.grid(row=0, column=2)

        ventanaImc.mainloop()
