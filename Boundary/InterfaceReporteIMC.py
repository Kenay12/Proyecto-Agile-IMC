import tkinter
from tkinter import *
from tkinter import ttk
from Control.AdministradorReporteController import AdministradorReporteController
from tkinter import messagebox
from openpyxl import Workbook


class InterfaceReporteIMC:


    def __init__(self):
        colorFondo = "#ACC0EB"
        colorRojo = "#F09794"
        colorVerde = "#B3DAA0"
        colorAmarillo = "#FFE599"

        def guardar_en_excel():
            # Crear un nuevo libro de Excel
            libro_excel = Workbook()
            hoja = libro_excel.active

            # Obtener el texto de la caja de texto
            texto = self.cajaTexto.get("1.0", "end-1c")

            # Separar las líneas de texto en una lista
            lineas = texto.split("\n")

            # Escribir cada línea en una fila de la hoja de Excel
            for i, linea in enumerate(lineas):
                hoja.cell(row=i + 1, column=1, value=linea)

            try:
                # Guardar el libro de Excel
                libro_excel.save("Reporte_Curso.xlsx")
                messagebox.showinfo("Guardado", "Los datos se guardaron correctamente en tabla.xlsx")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al guardar los datos:\n{str(e)}")

        #inicializacion de frame principal
        self.ventanaReport = Tk()
        self.ventanaReport.title("Sistema de seguimiento IMC")
        self.ventanaReport.config(bg=colorFondo)

        # Frame
        tituloReportFrame = Frame(self.ventanaReport)
        tituloReportFrame.pack()


        #Titulo
        tituloReport = Label(tituloReportFrame, text="Emitir Reportes", bg=colorFondo, font=("", 24), pady=10)
        tituloReport.pack()

        # frame curso
        selectCursoFrame = Frame(self.ventanaReport, bg=colorFondo)
        selectCursoFrame.pack()

        # legend para seleccionar
        legendSelect = LabelFrame(selectCursoFrame, text="Seleccionar Curso", bg=colorFondo)
        legendSelect.pack()


        self.seleccionarCurso = ttk.Combobox(legendSelect,state="readonly",values=self.listaCursos(),width=70)
        self.seleccionarCurso.grid(row=1, column=1)


        #caja de texto para lista de alumnos
        #frame de la caja
        cajaFrame = Frame(self.ventanaReport,bg=colorFondo)
        cajaFrame.pack()

        #legend de la caja
        cajaLegend = LabelFrame(cajaFrame,text="Lista de alumnos",bg=colorFondo)
        cajaLegend.pack()

        self.cajaTexto = Text(cajaLegend,width=45,state="normal")
        self.cajaTexto.pack(ipady=20)


        #frame para botones
        btnesFrame = Frame(self.ventanaReport,bg=colorFondo)
        btnesFrame.pack()


        #botones

        buttonSalir = Button(btnesFrame, text="Salir", command=self.ventanaReport.destroy, bg=colorRojo)
        buttonSalir.grid(row=0, column=0, padx=50)

        buttonVisualizar = Button(btnesFrame, text="Visualizar",command=self.listaAlumnos ,bg=colorAmarillo)
        buttonVisualizar.grid(row=0, column=1, padx=50)

        buttonEmitir = Button(btnesFrame,text="Emitir",bg=colorVerde,command=guardar_en_excel)
        buttonEmitir.grid(row=0,column=2,padx=50)

        self.ventanaReport.mainloop()

    def listaCursos(self):
        self.cursos = AdministradorReporteController().listaCursos()
        listaCursos = []
        for curso in self.cursos:
            listaCursos.append("{} {}".format(curso.nivel, curso.seccion))
        print(listaCursos)
        return listaCursos

    def listaAlumnos(self):
        self.cursoSelec = self.seleccionarCurso.get()
        self.cur = self.cursoSelec.split()
        self.alumnos = AdministradorReporteController().listaAlumnos(self.cur[0],self.cur[1])
        listaAlumnos = []

        for alumno in self.alumnos:
            listaAlumnos.append("{} {} {} {} {} {}".format(alumno.nombre, alumno.apellido,alumno.valor,alumno.rango,alumno.nivel,alumno.seccion))

        # Limpiar la caja de texto
        self.cajaTexto.delete('1.0', END)

        for alumnoItera in listaAlumnos:
            alumno_str = [str(item) for item in alumnoItera]
            self.cajaTexto.insert(END, "".join(alumno_str) + " \n")

























