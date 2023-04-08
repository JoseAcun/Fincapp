import sqlite3
    # funcion para insertar datos en la tabla telefonos
def insert_telefono():
    # se crea la coneccion con la base de datos local "Fincapp.db"
    con = sqlite3.connect("Fincapp.db")
    # asignacion de la funcion cursor a una variable
    cur = con.cursor()
    # captura de los datos de entrada
    indice = int(input("Indique el prefijo de su pais: "))

    numero = int(input("Indique su numero de telefono: "))
    # sql querry a usar definido en una variable
    sql = "INSERT INTO telefono(prefijo, numero) VALUES(?, ?)"
    # uso del comando execute para usar una funcion sql en la base de datos en este caso para insertar los datos
    cur.execute(sql, (indice, numero))
    con.commit()

    # funcion para insertar datos en la tabla email
def insert_email():
    # se crea la coneccion con la base de datos local "Fincapp.db"
    con = sqlite3.connect("Fincapp.db")
    # se crea la coneccion con la base de datos local "Fincapp.db"
    cur = con.cursor()    
    # captura de los datos de entrada
    correoF = input("Ingrese su correo: ")
    # se define un separador a usar con la funcion split()
    separador = "@"
    # se usa la funcion split() con la variable separador sobre el texto contenido en la variable "correoF" para 
    # almacenar ambas partes del texto en el array "correoS"
    correoS = correoF.split(separador)
    # se crean dos variables que van a contener la posicion 0 y la posicion 1 del array para insertarlos en sus respectivos campos en la DB
    correo = correoS[0]  

    dominio = correoS[1]
    # sql querry a usar definido en una variable
    sql = "INSERT INTO email(correo, dominio) VALUES(UPPER(?), UPPER(?))"
    # uso del comando execute para usar una funcion sql en la base de datos en este caso para insertar los datos
    cur.execute(sql, (correo, dominio))
    con.commit()
    # funcion para agregar datos en la tabla personas


def insert_persona():
    con = sqlite3.connect("Fincapp.db")

    cur = con.cursor()  
    # se consultan los ultimos id generados de las tablas que contienen las llaves primarias respectivas a las foraneas de persona
    result = con.execute("SELECT id FROM telefono ORDER BY id DESC LIMIT 1")
    last_id_telefono = result.fetchone()[0]

    result = con.execute("SELECT id FROM email ORDER BY id DESC LIMIT 1")
    last_id_email = result.fetchone()[0]

    nombre_completo = input("Introduce el nombre completo de la persona: ")

    tipo_persona = int(input("""Seleccione el tipo de persona: \n
                            1.Natural \n
                            2.Juridica \n"""))

    nombres_apellidos = nombre_completo.split()
    nombres = nombres_apellidos[:2]
    apellidos = nombres_apellidos[2:]

    if len(nombres) == 1:
        nombre_1 = nombres[0]
        nombre_2 = ''
    else:
        nombre_1 = nombres[0]
        nombre_2 = nombres[1]

    if len(apellidos) == 1:
        apellido_1 = apellidos[0]
        apellido_2 = ''
    else:
        apellido_1 = apellidos[0]
        apellido_2 = apellidos[1]

        con.execute("INSERT INTO persona (nom1, nom2, ap1, ap2, id_email, id_telefono, id_tipo_persona) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                    (nombre_1, nombre_2, apellido_1, apellido_2, last_id_email, last_id_telefono, tipo_persona))

    con.commit()

            #el insert trabajador requiere una consulta al registro persona y tammbien una consulta a la tabla administrador

def insert_trabajador():
    con = sqlite3.connect("Fincapp.db")

    cur = con.cursor()  

    result = con.execute("SELECT id FROM persona ORDER BY id DESC LIMIT 1")
    last_id_persona = result.fetchone()[0]

    sueldo = float(input("Ingrese el sueldo del trabajador: "))


    con.commit()

  # los metodos de pagos pueden insertarse directamente en la base de datos para pedirse en una consulta y mostrarse en una lista
def metodo_pago():
    con = sqlite3.connect("Fincapp.db")

    cur = con.cursor()

    cur.execute("SELECT * FROM metodopago")
    metodo_pago = cur.fetchall()
    for metodo in metodo_pago:
        lista_metodo = list(metodo)
        print(') '.join(str(valor) for valor in lista_metodo))
    input("""Elija el metodo de pago: """)


        # funcion para insertar id de metodos de pago en pagos
def insert_pago():
    con = sqlite3.connect("Fincapp.db")

    cur = con.cursor()

    result = con.execute("SELECT id FROM metodopago ORDER BY id DESC LIMIT 1")
    last_id_metodopago = result.fetchone()[0]

    con.execute("INSERT INTO id_metodopago VALUES (?)",(last_id_metodopago))
    con.commit()


def insert_categorias():
    con = sqlite3.connect("Fincapp.db")

    cur = con.cursor()

    con.commit()
    con.close()

# insert_email()
# insert_telefono()
# insert_persona()
metodo_pago()
con = sqlite3.connect("Fincapp.db")
cur = con.cursor()

cur.execute("""select p.nom1, p.ap1, t.numero,e.correo || '@' || e.dominio as correo, tp.tipo_persona from persona p 
                 inner join telefono t on t.id = p.id_telefono 
                 inner join email e on e.id = p.id_email
                 inner join tipo_persona tp on tp.id = p.id_tipo_persona""")


print(cur.fetchall())
con.commit()
