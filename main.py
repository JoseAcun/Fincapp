import tkinter as tk
from tkinter import ttk

# Crea una instancia de la ventana principal
root = tk.Tk()

# Establece el título de la ventana
root.title("Mi aplicación")

# Establece las dimensiones de la ventana
root.geometry("600x400")

# Función para mostrar la página de inicio de sesión
def show_login():
    
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de inicio de sesión
    label_username = tk.Label(root, text="Usuario")
    label_username.pack()

    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Contraseña")
    label_password.pack()

    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    button_login = tk.Button(root, text="Iniciar sesión", command=show_movements)
    button_login.pack()
    
    button_login = tk.Button(root, text="Registrarse", command=show_register)
    button_login.pack()

# Función para mostrar la página de registro
def show_register():
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de registro
    label_username = tk.Label(root, text="Usuario")
    label_username.pack()

    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Contraseña")
    label_password.pack()

    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    button_register = tk.Button(root, text="Registrarse", command=show_movements)
    button_register.pack()

# Función para mostrar la tabla de movimientos
def show_movements():
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Menu desplegable
    menu = tk.Menu()

    # Crea los widgets necesarios para la tabla de movimientos
    label_movements = tk.Label(root, text="Movimientos")
    label_movements.pack()

    treeview = ttk.Treeview(root, columns=("Fecha", "Concepto", "Cantidad"))
    treeview.heading("#0", text="ID")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("Concepto", text="Concepto")
    treeview.heading("Cantidad", text="Cantidad")
    treeview.pack()

    # Agrega algunos datos de muestra a la tabla
    for i in range(10):
        treeview.insert("", "end", text=i, values=("2022-04-01", "Concepto {}".format(i), "${}".format(i*100)))

    button_profile = tk.Button(root, text="Perfil", command=show_profile)
    button_profile.pack(side=tk.TOP)

    button_newmov = tk.Button(root, text="Nuevo Movimiento", command=show_newmov)
    button_newmov.pack(side=tk.TOP)
    
    button_vercats = tk.Button(root, text="Ver Categorias", command=show_Cats)
    button_vercats.pack(side=tk.TOP)
    
    button_verprods = tk.Button(root, text="Ver Productos", command=show_prods)
    button_verprods.pack(side=tk.TOP)
    
    button_vertrab = tk.Button(root, text="Ver Trabajadores", command=show_trabajadores)
    button_vertrab.pack(side=tk.TOP)

def show_Cats():
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    label_categorias = tk.Label(root, text="Categorias")
    label_categorias.pack()

    treeview = ttk.Treeview(root, columns=("Fecha", "Concepto", "Cantidad"))
    treeview.heading("#0", text="ID")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("Concepto", text="Concepto")
    treeview.heading("Cantidad", text="Cantidad")
    treeview.pack()

    for i in range(10):
        treeview.insert("", "end", text=i, values=("2022-04-01", "Concepto {}".format(i), "${}".format(i*100)))

    button_inscategorias = tk.Button(root, text="Crear Categoría", command=show_inscategoria)
    button_inscategorias.pack()

    button_volvcat = tk.Button(root, text="Volver", command=show_movements)
    button_volvcat.pack()

def show_prods():
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    label_productos = tk.Label(root, text="Productos")
    label_productos.pack()

    treeview = ttk.Treeview(root, columns=("Fecha", "Concepto", "Cantidad"))
    treeview.heading("#0", text="ID")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("Concepto", text="Concepto")
    treeview.heading("Cantidad", text="Cantidad")
    treeview.pack()

    # Agrega algunos datos de muestra a la tabla
    for i in range(10):
        treeview.insert("", "end", text=i, values=("2022-04-01", "Concepto {}".format(i), "${}".format(i*100)))

    button_insproductos = tk.Button(root, text="Ingresar Productos", command=show_insprods)
    button_insproductos.pack()

    button_volvprods = tk.Button(root, text="Volver", command=show_movements)
    button_volvprods.pack()

def show_insprods():
    
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de inicio de sesión
    label_insprods = tk.Label(root, text="Modulo Ingreso de Productos")
    label_insprods.pack()

    label_selcat = tk.Label(root, text="Seleccione la categoria del producto")
    label_selcat.pack()
    
    variable = tk.StringVar(root)
    
    variable.set("Frutas")
    
    w = tk.OptionMenu(root, variable, "Frutas", "Verduras", "Lacteos")
    w.pack()

    label_nomprod = tk.Label(root, text="Nombre Producto")
    label_nomprod.pack()

    entry_nomprod = tk.Entry(root)
    entry_nomprod.pack()

    label_cantprod = tk.Label(root, text="Cantidad de producto")
    label_cantprod.pack()

    entry_cantprod = tk.Entry(root)
    entry_cantprod.pack()
    
    label_precioprod = tk.Label(root, text="Precio unitario del producto")
    label_precioprod.pack()

    entry_precioprod = tk.Entry(root)
    entry_precioprod.pack()

    label_Descprod = tk.Label(root, text="Descripcion del producto")
    label_Descprod.pack()

    entry_Descprod = tk.Entry(root)
    entry_Descprod.pack()

    button_insprod = tk.Button(root, text="Ingresar producto", command=show_prods)
    button_insprod.pack()

    button_volvtrab = tk.Button(root, text="Volver", command=show_movements)
    button_volvtrab.pack()

def show_instrabajador():
    
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de inicio de sesión
    label_instrab = tk.Label(root, text="Modulo Ingreso de Trabajadores")
    label_instrab.pack()

    label_nomtrab = tk.Label(root, text="Nombre del trabajador")
    label_nomtrab.pack()

    entry_nomtrab = tk.Entry(root)
    entry_nomtrab.pack()

    label_apetrab = tk.Label(root, text="Apellido del trabajador")
    label_apetrab.pack()

    entry_apeprod = tk.Entry(root)
    entry_apeprod.pack()
    
    label_teltrab = tk.Label(root, text="Telefono")
    label_teltrab.pack()

    entry_teltrab = tk.Entry(root)
    entry_teltrab.pack()

    label_sueltrab = tk.Label(root, text="Sueldo")
    label_sueltrab.pack()

    entry_sueltrab = tk.Entry(root)
    entry_sueltrab.pack()

    button_insprod = tk.Button(root, text="Ingresar Trabajador", command=show_trabajadores)
    button_insprod.pack()

    button_volvtrab = tk.Button(root, text="Volver", command=show_trabajadores)
    button_volvtrab.pack()

def show_inscategoria():
    
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de inicio de sesión
    label_inscat = tk.Label(root, text="Modulo Ingreso de categorias")
    label_inscat.pack()

    label_nomcat = tk.Label(root, text="Nombre de la categoria")
    label_nomcat.pack()

    entry_nomcat = tk.Entry(root)
    entry_nomcat.pack()

    label_icocat = tk.Label(root, text="Insertar Icono")
    label_icocat.pack()

    button_icocat = tk.Button(root, text="+")
    button_icocat.pack()

    button_insprod = tk.Button(root, text="Ingresar Categoria", command=show_Cats)
    button_insprod.pack()

    button_volvtrab = tk.Button(root, text="Volver", command=show_Cats)
    button_volvtrab.pack()



def show_trabajadores():

    for widget in root.winfo_children():
        widget.destroy()

    label_trabajadores = tk.Label(root, text="Trabajadores")
    label_trabajadores.pack()

    treeview = ttk.Treeview(root, columns=("Fecha", "Concepto", "Cantidad"))
    treeview.heading("#0", text="ID")
    treeview.heading("Fecha", text="Fecha")
    treeview.heading("Concepto", text="Concepto")
    treeview.heading("Cantidad", text="Cantidad")
    treeview.pack()

    for i in range(10):
        treeview.insert("", "end", text=i, values=("2022-04-01", "Concepto {}".format(i), "${}".format(i*100)))

    button_instrabajadores = tk.Button(root, text="Nuevo Trabajador", command=show_instrabajador)
    button_instrabajadores.pack()

    button_volvtrab = tk.Button(root, text="Volver", command=show_movements)
    button_volvtrab.pack()

def show_profile():
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de perfil
    label_profile = tk.Label(root, text="Perfil")
    label_profile.pack()

    button_logout = tk.Button(root, text="Cerrar sesión", command=show_login)
    button_logout.pack()

def show_newmov():
    
    for widget in root.winfo_children():
        widget.destroy()

    label_typemov = tk.Label(root, text="Tipo de Movimiento")
    label_typemov.pack()

    button_insprod = tk.Button(root, text="Ingresar Producto", command=show_insprods)
    button_insprod.pack()
    
    button_salprod = tk.Button(root, text="Salida por Venta", command=show_salprod)
    button_salprod.pack()
    
    button_salprodo = tk.Button(root, text="Salida por Otro Motivo", command=show_salprodo)
    button_salprodo.pack()

def show_salprod():
    
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de inicio de sesión
    label_salprod = tk.Label(root, text="Venta")
    label_salprod.pack()

    label_selprod = tk.Label(root, text="Seleccione el producto")
    label_selprod.pack()
    
    variable = tk.StringVar(root)
    
    variable.set("Mango")
    
    w = tk.OptionMenu(root, variable, "Mango", "Limon", "Leche")
    w.pack()

    label_cantprod = tk.Label(root, text="Cantidad a vender")
    label_cantprod.pack()

    entry_cantprod = tk.Entry(root)
    entry_cantprod.pack()
    
    label_Metopag = tk.Label(root, text="Seleccione Metodo de Pago")
    label_Metopag.pack()
    
    variable1 = tk.StringVar(root)
    
    variable1.set("Efectivo")
    
    w = tk.OptionMenu(root, variable1, "Efectivo", "PSE", "Transferencia")
    w.pack()

    label_valvent = tk.Label(root, text="Valor total de la venta")
    label_valvent.pack()

    text_field = tk.Entry(root, state='disabled')
    text_field.pack()   
    
    
    button_Realvent = tk.Button(root, text="Realizar Venta", command=show_movements)
    button_Realvent.pack()

    button_Realvent = tk.Button(root, text="Volver", command=show_newmov)
    button_Realvent.pack()

def show_salprodo():
    
    # Elimina cualquier widget que esté en la ventana principal
    for widget in root.winfo_children():
        widget.destroy()

    # Crea los widgets necesarios para la página de inicio de sesión
    label_salprod = tk.Label(root, text="Otra Salida")
    label_salprod.pack()

    label_selprod = tk.Label(root, text="Seleccione el producto")
    label_selprod.pack()
    
    variable = tk.StringVar(root)
    
    variable.set("Mango")
    
    w = tk.OptionMenu(root, variable, "Mango", "Limon", "Leche")
    w.pack()

    label_cantprod = tk.Label(root, text="Cantidad")
    label_cantprod.pack()

    entry_cantprod = tk.Entry(root)
    entry_cantprod.pack()
    
    label_Metopag = tk.Label(root, text="Descripcion de Salida")
    label_Metopag.pack()
    
    entry_descsal = tk.Entry(root)
    entry_descsal.pack()

    label_valvent = tk.Label(root, text="Valor Total de la Salida")
    label_valvent.pack()

    text_field = tk.Entry(root, state='disabled')
    text_field.pack()   
    
    button_RealSal = tk.Button(root, text="Procesar Salida", command=show_movements)
    button_RealSal.pack()

    button_RealSal = tk.Button(root, text="Volver", command=show_newmov)
    button_RealSal.pack()


# Mostrar la página de inicio de sesión al inicio
show_login()

# Inicia el bucle principal de la ventana
root.mainloop()