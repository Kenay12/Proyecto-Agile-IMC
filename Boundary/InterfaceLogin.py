import tkinter as tk
from tkinter import ttk, messagebox
from Boundary.InterfaceCalculoIMC import InterfaceCalculadoraIMC
from Control.LoginController import LoginController


class PanelLogin:
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
        titulo = tk.Label(frame_titulo, text="AUTENTIFICACIÓN", bg=colorFondo, font=("", 18), pady=10)
        titulo.pack(expand=tk.YES, fill=tk.BOTH, pady=(0, 28))

        # Frame body
        frame_body = tk.Frame(frame, height=50, bd=0, relief=tk.SOLID, bg=colorFondo)
        frame_body.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #body
        # label email
        labelEmail = tk.Label(frame_body, text="EMAIL", font=("", 12), anchor="w", bg=colorFondo)
        labelEmail.pack(fill=tk.X, padx=50)
        # input email
        self.email = tk.Entry(frame_body, font=("", 12))
        self.email.pack(fill=tk.X, padx=70, pady=(0, 60))

        # label contraseña
        labelContra = tk.Label(frame_body, text="CONTRASEÑA", font=("", 12), anchor="w", bg=colorFondo)
        labelContra.pack(fill=tk.X, padx=50)
        # input contraseña
        self.contra = tk.Entry(frame_body, font=("", 12))
        self.contra.pack(fill=tk.X, padx=70)
        self.contra.config(show="*")

        #boton ingresar
        botonIngresar = tk.Button(frame_body, text="INGRESAR", font=("", 12), bg=colorVerde,
                                  command=self.validarCredenciales)
        botonIngresar.pack(pady=(26, 36), ipadx=12, ipady=1)

        # container botones
        frame_botones = tk.Frame(frame_body, height=50, bd=0, relief=tk.SOLID, bg=colorFondo)
        frame_botones.pack()
        # boton Salir
        botonSalir = tk.Button(frame_botones, text="SALIR", font=("", 12), bg=colorRojo,
                               command=self.ventana.destroy)
        botonSalir.grid(column=1, row=0, sticky=tk.E, padx=(180, 10), ipadx=12)

        # recuperar contraseña
        labelRecuperarContra = tk.Label(frame_botones, text="Recuperar Contraseña", font=("", 11), bd=0, cursor="hand2",
                                        bg=colorFondo)
        labelRecuperarContra.grid(column=0, row=0, sticky=tk.W)
        labelRecuperarContra.bind("<Button-1>", lambda e: self.recuperarContra())

        self.ventana.mainloop()

    def validarCredenciales(self):
        login = LoginController().inicioSesion(self.email.get(), self.contra.get())
        if login:
            self.ventana.destroy()
            InterfaceCalculadoraIMC()
        else:
            messagebox.showerror(message="Credenciales Inválidas", title="Mensaje")

    def recuperarContra(self):
        messagebox.showinfo(title="Recuperar Contraseña", message="Contacte con el administrador")

