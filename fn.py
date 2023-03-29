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

    tipo_persona = input

    con.commit()


con = sqlite3.connect("Fincapp.db")
cur = con.cursor()

cur.execute("select * from email")
print(cur.fetchall())
# data = [
#     ("Monty", "Python", "Live at the," "Hollywood Bowl", 1982, 7.9)
# ]
# cur.executemany("INSERT INTO persona VALUES(?, ?, ?)", data)
con.commit()