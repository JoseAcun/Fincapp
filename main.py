import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        
        # Configuración de la ventana principal
        self.title("FincApp")
        self.geometry("450x900")
        self.resizable(False, False)

        # Configuración del estilo
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        
        # Configuración de los widgets
        self.login_frame = ttk.Frame(self)
        self.login_frame.pack(fill=tk.BOTH, expand=True)

        self.login_label = ttk.Label(self.login_frame, text="Iniciar sesión", font=("Helvetica", 16))
        self.login_label.pack(pady=20)

        self.login_username_label = ttk.Label(self.login_frame, text="Nombre de usuario")
        self.login_username_label.pack(pady=5)

        self.login_username_entry = ttk.Entry(self.login_frame)
        self.login_username_entry.pack(pady=5)

        self.login_password_label = ttk.Label(self.login_frame, text="Contraseña")
        self.login_password_label.pack(pady=5)

        self.login_password_entry = ttk.Entry(self.login_frame, show="*")
        self.login_password_entry.pack(pady=5)

        self.login_button = ttk.Button(self.login_frame, text="Iniciar sesión", command=self.show_main)
        self.login_button.pack(pady=10)

        self.register_frame = ttk.Frame(self)
        self.register_label = ttk.Label(self.register_frame, text="Registro", font=("Helvetica", 16))
        self.register_label.pack(pady=20)

        self.register_username_label = ttk.Label(self.register_frame, text="Nombre de usuario")
        self.register_username_label.pack(pady=5)

        self.register_username_entry = ttk.Entry(self.register_frame)
        self.register_username_entry.pack(pady=5)

        self.register_password_label = ttk.Label(self.register_frame, text="Contraseña")
        self.register_password_label.pack(pady=5)

        self.register_password_entry = ttk.Entry(self.register_frame, show="*")
        self.register_password_entry.pack(pady=5)

        self.register_button = ttk.Button(self.login_frame, text="Registrarse", command=self.show_register)
        self.register_button.pack(pady=10)
        
        self.login_button = ttk.Button(self.register_frame, text="Registrarse", command=self.show_main)
        self.login_button.pack(pady=10)
        
        self.login_button = ttk.Button(self.register_frame, text="Loguearse", command=self.show_login)
        self.login_button.pack(pady=10)

        self.main_frame = ttk.Frame(self)
        self.main_label = ttk.Label(self.main_frame, text="Página principal", font=("Helvetica", 16))
        self.main_label.pack(pady=20)

        self.logout_button = ttk.Button(self.main_frame, text="Cerrar sesión", command=self.show_login)
        self.logout_button.pack(pady=10)

        # Mostrar la pantalla de inicio de sesión
        self.show_login()

    def show_login(self):
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        self.register_frame.pack_forget()
        self.main_frame.pack_forget()
        
    def show_register(self):
        self.register_frame.pack(fill=tk.BOTH, expand=True)
        self.login_frame.pack_forget()
        self.main_frame.pack_forget()
        
    def show_main(self):
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.login_frame.pack_forget()
        self.register
        self.register_frame.pack_forget()

app = App()
app.mainloop()
