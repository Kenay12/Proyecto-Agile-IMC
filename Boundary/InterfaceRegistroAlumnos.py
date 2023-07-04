from Entity.DAO.CRUD_Alumno import ingresar
import tkinter as tk
from tkinter import ttk, messagebox


class PanelRegistroAlumnos:
    def __init__(self):
        colorFondo = "#ACC0EB"
        colorRojo = "#F09794"
        colorVerde = "#B3DAA0"

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de seguimiento IMC")
        self.ventana.geometry("500x400")
        self.ventana.config(bg=colorFondo)

        # Frame ventana
        frame = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg=colorFondo)
        frame.pack(expand=tk.YES, fill=tk.BOTH)

        # Frame titulo
        frame_titulo = tk.Frame(frame, height=50, bd=0, relief=tk.SOLID, bg=colorFondo)
        frame_titulo.pack(side="top", fill=tk.X)

        # titulo
        titulo = tk.Label(frame_titulo, text="Administración de alumnos", bg=colorFondo, font=("", 18), pady=10)
        titulo.pack(expand=tk.YES, fill=tk.BOTH, pady=(0, 28))

        # Frame body
        frame_body = tk.Frame(frame, height=50, bd=0, relief=tk.SOLID, bg=colorFondo)
        frame_body.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        # container form
        self.form = tk.Frame(frame_body, height=50, relief=tk.SOLID, bd=1, bg="white")

        #body
        # combobox seleccionar curso
        self.form.curso = ttk.Combobox(frame_body, state="readonly", values=["Curso 1", "Curso 2"])
        self.form.curso.set("    Seleccionar Curso")
        self.form.curso.pack(fill=tk.X, padx=70, pady=(0, 20), ipady=4)

        # container botones
        frame_botones = tk.Frame(frame_body, height=50, bd=0, relief=tk.SOLID, bg=colorFondo)
        frame_botones.pack()

        # boton agregar alumno
        botonAgregarAlumno = tk.Button(frame_botones, text="Agregar un alumno", font=("", 12), bg=colorVerde,
                                       command=self.mostrarForm)
        botonAgregarAlumno.grid(column=0, row=0, sticky=tk.E, padx=(180, 10), ipadx=12)

        # boton Volver
        botonVolver = tk.Button(frame_botones, text="Volver", font=("", 12), bg=colorRojo,
                                command=self.ventana.destroy)
        botonVolver.grid(column=0, row=0, sticky=tk.W, padx=(0, 10), ipadx=12)

        # form
        # input rut
        labelRut = tk.Label(self.form, text="Rut:", font=("", 12), anchor="w", bg="white")
        labelRut.grid(column=0, row=0, sticky=tk.W)
        self.form.rut = tk.Entry(self.form, font=("", 12), bd=2)
        self.form.rut.grid(column=1, row=0, sticky=tk.E)

        # input nombres
        labelNombres = tk.Label(self.form, text="Nombres:", font=("", 12), anchor="w", bg="white")
        labelNombres.grid(column=0, row=1, sticky=tk.W)
        self.form.nombres = tk.Entry(self.form, font=("", 12), bd=2)
        self.form.nombres.grid(column=1, row=1, sticky=tk.E)

        # input apellidos
        labelApellidos = tk.Label(self.form, text="Apellidos:", font=("", 12), anchor="w", bg="white")
        labelApellidos.grid(column=0, row=2, sticky=tk.W)
        self.form.apellidos = tk.Entry(self.form, font=("", 12), bd=2)
        self.form.apellidos.grid(column=1, row=2, sticky=tk.E)

        # input fecha nacimiento
        labelFecNac = tk.Label(self.form, text="Fecha de Nacimiento:", font=("", 12), anchor="w", bg="white")
        labelFecNac.grid(column=0, row=3, sticky=tk.W)
        self.form.fecha_nac = tk.Entry(self.form, font=("", 12), bd=2)
        self.form.fecha_nac.grid(column=1, row=3, sticky=tk.E)

        # input sexo
        labelSexo = tk.Label(self.form, text="Sexo:", font=("", 12), anchor="w", bg="white")
        labelSexo.grid(column=0, row=4, sticky=tk.W)
        self.form.sexo = ttk.Combobox(self.form, state="readonly", values=["Masculino", "Femenino", "Otro"])
        self.form.sexo.grid(column=1, row=4, sticky=tk.E)

        #boton ingresar
        botonIngresar = tk.Button(self.form, text="Ingresar alumno", font=("", 12), bg=colorVerde,
                                  command=self.ingresarAlumno)
        botonIngresar.grid(columnspan=2)

        self.ventana.mainloop()

    def mostrarForm(self):
        curso = self.form.curso.get()
        if curso != "    Seleccionar Curso":
            self.form.pack()
        else:
            messagebox.showerror(message="Debe seleccionar un curso", title="Mensaje")

    def ingresarAlumno(self):
        if self.form.rut.get() != "" and self.form.nombres != "" and self.form.apellidos.get() != "" and self.form.fecha_nac.get() != "" and self.form.sexo.get() != "":
            try:
                ingresar(self.form)
                messagebox.showinfo(message="Alumno registrado con éxito!", title="Mensaje")
            except Exception as e:
                messagebox.showerror(message="Error: {}".format(e), title="Error al ingresar alumno")
        else:
            messagebox.showerror(message="No pueden haber campos vacios", title="Mensaje")



PanelRegistroAlumnos()
