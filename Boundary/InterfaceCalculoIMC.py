from Control.CalculoIMC import CalculoIMCController
from tkinter import *
from tkinter import messagebox, ttk


class InterfaceCalculadoraIMC:
    def __init__(self):
        colorFondo = "#ACC0EB"
        colorRojo = "#F09794"
        colorVerde = "#B3DAA0"
        colorAmarillo = "#FFE599"

        # funciones
        def mostrarAlumnos(curso):
            alumnos_por_curso = CalculoIMCController().obtenerListaAlumno()

            # Obtener la lista de alumnos correspondiente al curso seleccionado
            lista_alumnos = []
            for alumno in alumnos_por_curso[curso]:
                lista_alumnos.append("{} - {} {}".format(alumno.rut, alumno.nombres, alumno.apellidos))

            # Limpiar el OptionMenu existente, si lo hay
            if valorAlumnoSelect[0] is not None:
                valorAlumnoSelect[0].destroy()

            # Crear un nuevo OptionMenu con la lista de alumnos
            alumno_var.set(lista_alumnos[0])  # Establecer el valor inicial

            alumno_label = Label(infoImc, text="Seleccione Alumno:", bg=colorFondo)
            alumno_label.grid(row=1, column=0)
            valorAlumnoSelect[0] = OptionMenu(infoImc, alumno_var, *lista_alumnos)
            valorAlumnoSelect[0].grid(row=1, column=1)

        # inicializacion de la interfaz
        ventanaImc = Tk()
        ventanaImc.title("Sistema de seguimiento IMC")
        ventanaImc.config(bg=colorFondo)

        # Variables
        peso = DoubleVar()
        altura = DoubleVar()
        imc = StringVar()
        rango = StringVar()

        # Frame
        tituloFrame = Frame(ventanaImc)
        tituloFrame.pack()

        frame = Frame(ventanaImc)
        frame.pack()
        frame.config(bg=colorFondo)

        # Titulo
        titulo = Label(tituloFrame, text="Calculadora IMC", bg=colorFondo, font=("", 24), pady=10)
        titulo.pack()

        # legend2
        infoImc = LabelFrame(frame, text="Calculadora de IMC", bg=colorFondo)
        infoImc.grid(row=6, column=1, ipadx=26, ipady=6, pady=12)

        # Crear un Combobox para seleccionar un curso
        curso_label = Label(infoImc, text="Seleccione Curso:", bg=colorFondo)
        curso_label.grid(row=0, sticky=W)
        cursos = CalculoIMCController().obtenerCursos()
        # definiremos las variables del los option menus
        curso_var = StringVar(infoImc)
        alumno_var = StringVar()

        cursoSelect = OptionMenu(infoImc, curso_var, *cursos, command=mostrarAlumnos)
        cursoSelect.grid(row=0, column=1)
        valorAlumnoSelect = [None]

        # Ingresar Imc

        labelPeso = Label(infoImc, text='Peso (kg): ', bg=colorFondo)
        labelAltura = Label(infoImc, text='Altura (m): ', bg=colorFondo)

        entryPeso = Entry(infoImc, width=40, textvariable=peso, validate="key")
        entryAltura = Entry(infoImc, width=40, textvariable=altura, validate="key")

        labelPeso.grid(row=2, sticky=W)
        labelAltura.grid(row=3, sticky=W)

        entryPeso.grid(row=2, column=1)
        entryAltura.grid(row=3, column=1)

        # Boton Guardar
        btnGuardar = Button(infoImc, text="Guardar",
                            command=lambda: self.guardarCalculo(peso, altura, alumno_var, imc, rango, infoResulImc),
                            bg=colorVerde)
        btnGuardar.grid(row=6, column=0, pady=6)

        # Boton Calcular
        calculoIMC = Button(infoImc, text="Calcular",
                            command=lambda: self.calculoIMC(peso, altura, alumno_var, imc, rango, infoResulImc),
                            bg=colorVerde)
        calculoIMC.grid(row=6, column=1, pady=6)

        # legend3
        infoResulImc = LabelFrame(frame, text="Resultados", bg=colorFondo)
        infoResulImc.grid_forget()

        # caja de resultado y descriptivo
        resultado = Label(infoResulImc, text="IMC:", bg=colorFondo)
        resultado.grid(row=0, column=0)
        resulEntry = Entry(infoResulImc, width=40, state="disabled", textvariable=imc, disabledforeground="black",
                           disabledbackground="white")
        resulEntry.grid(row=0, column=1)
        descriptivo = Label(infoResulImc, text="Descriptivo:", bg=colorFondo, padx=12)
        descriptivo.grid(row=1, column=0)
        descriptivo = Entry(infoResulImc, width=40, state="disabled", textvariable=rango, disabledforeground="black",
                            disabledbackground="white")
        descriptivo.grid(row=1, column=1)

        # boton salir y regresar
        buttonSalir = Button(frame, text="Salir", command=ventanaImc.destroy, bg=colorRojo)
        buttonSalir.grid(row=0, column=0, padx=4)

        buttonRegresar = Button(frame, text="Regresar", bg=colorAmarillo)
        buttonRegresar.grid(row=0, column=2, padx=4)

        ventanaImc.mainloop()

    def calculoIMC(self, peso, altura, alumno_var, imc, rango, infoResulImc):
        valorPeso = peso.get()
        valorAltura = altura.get()
        valorRut = alumno_var.get().split(" - ")[0]
        calculoIMC = CalculoIMCController().calcularIMC(valorPeso, valorAltura, valorRut)
        if isinstance(calculoIMC, str):
            imc.set(calculoIMC)
            rango.set(calculoIMC)
        else:
            imc.set(calculoIMC.valor)
            rango.set(calculoIMC.rango)
        infoResulImc.grid(row=9, column=1, ipadx=26, ipady=10, pady=6)
        return calculoIMC

    def guardarCalculo(self, peso, altura, alumno_var, imc, rango, infoResulImc):
        valorPeso = peso.get()
        valorAltura = altura.get()
        valorRut = alumno_var.get().split(" - ")[0]
        registroIMC = CalculoIMCController().ingresarIMC(valorPeso, valorAltura, valorRut)
        if isinstance(registroIMC, str):
            imc.set(registroIMC)
            rango.set(registroIMC)
        else:
            imc.set(registroIMC.valor)
            rango.set(registroIMC.rango)
        infoResulImc.grid(row=9, column=1, ipadx=26, ipady=10, pady=6)
        return registroIMC
