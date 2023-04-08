import sqlite3

con = sqlite3.connect("Fincapp.db")

cur = con.cursor()
                    #Creacion de la tabla email
cur.execute("create table email(id integer primary key autoincrement,correo varchar(50),dominio varchar(50))")
                    
                    # Creacion de la tabla telefonos
cur.execute("create table telefono(id integer primary key autoincrement,prefijo int,numero bigint);")

                    # Creacion de la tabla tipo persona
cur.execute("create table tipo_persona(id integer primary key autoincrement, tipo_persona varchar(25))")
                    
                    # Creacion de la tabla personas
cur.execute("Create table persona(id integer primary key autoincrement,nom1 varchar(50),nom2 varchar(50),ap1 varchar(50),ap2 varchar(50),id_email int,id_telefono int, id_tipo_persona int, foreign key (id_tipo_persona) references tipo_persona(id), foreign key (id_email) references email(id),foreign key (id_telefono) references telefono(id));")
                    
                    # Creacion de la tabla trabajador
cur.execute("create table trabajador(id integer primary key autoincrement,sueldo float,id_persona int,foreign key (id_persona) references persona(id));")
                    
                    # Creacion de la tabla metodo de pago
cur.execute("create table metodopago(id integer primary key autoincrement,metodo_pago varchar(50));")
                    
                    # Creacion de la tabla pago
cur.execute("create table pago(id integer primary key autoincrement,id_metodopago int,foreign key (id_metodopago) references metodopago(id));")
                    
                    # Creacion de la tabla categorias
cur.execute("create table categoria(id integer primary key autoincrement,nom_cat varchar(50),icono blob);")
                    
                    # Creacion de la tabla productos
cur.execute("create table producto(id integer primary key autoincrement,nombre varchar(50),valor_unit float,descripcion text,id_categoria int,foreign key (id_categoria) references categoria(id));")
                    
                    # Creacion de la tabla administrador
cur.execute("create table administrador(id integer primary key autoincrement,usuario varchar(25),contraseña varchar(25),id_persona int,foreign key (id_persona) references persona(id));")
                    
                    # Creacion de la tabla movimientos
cur.execute("create table movimiento(cantidad int,fecha date,descripcion_movimiento text,id_persona int,id_pago int,id_producto int,foreign key (id_producto) references producto(id),foreign key (id_pago) references pago(id),foreign key (id_persona) references persona(id));")

                    # Insercion de los datos en la tabla tipo_persona
cur.execute("""INSERT INTO tipo_persona(tipo_persona) values('Natural'),('Juridica')""") 

                    # Insercion de los datos en la tabla metodo de pago
cur.execute("INSERT INTO metodopago(metodo_pago) values('Efectivo'), ('tarjeta'), ('transferencia'), ('otro')",)

con.commit()