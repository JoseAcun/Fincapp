import sqlite3



class DbMain():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()

        cmd = """CREATE TABLE IF NOT EXISTS email(id integer primary key autoincrement,correo varchar(50),dominio varchar(50))"""
        self.curs.execute(cmd)
        self.conn.commit()

        cmd = """CREATE TABLE IF NOT EXISTS telefono(id integer primary key autoincrement,prefijo int,numero bigint)"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS tipo_persona(id integer primary key autoincrement, tipo_persona varchar(25))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS persona(id integer primary key autoincrement,nom1 varchar(50),nom2 varchar(50),ap1 varchar(50),ap2 varchar(50),id_email int,id_telefono int, id_tipo_persona int, active INTEGER NOT NULL, foreign key (id_tipo_persona) references tipo_persona(id), foreign key (id_email) references email(id),foreign key (id_telefono) references telefono(id))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS trabajador(id integer primary key autoincrement,sueldo float,id_persona int,foreign key (id_persona) references persona(id))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS metodopago(id integer primary key autoincrement,metodo_pago varchar(50))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS pago(id integer primary key autoincrement,id_metodopago int,foreign key (id_metodopago) references metodopago(id))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS categoria(id integer primary key autoincrement,nom_cat varchar(50), icono icon)"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS producto(id integer primary key autoincrement, cantidad int, nombre varchar(50),valor_unit float,descripcion text,id_categoria int,foreign key (id_categoria) references categoria(id))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS administrador(id integer primary key autoincrement,usuario varchar(25),passwordu varchar(25),id_persona int,foreign key (id_persona) references persona(id))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS movimiento(cantidad int,fecha date,descripcion_movimiento text,id_persona int,id_pago int,id_producto int,foreign key (id_producto) references producto(id),foreign key (id_pago) references pago(id),foreign key (id_persona) references persona(id))"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        cmd = """CREATE TABLE IF NOT EXISTS curr_admin(currid INTEGER, active INTEGER NOT NULL)"""
        self.curs.execute(cmd)
        self.conn.commit()
        
        # Verifica si la tabla "tipo_persona" ya tiene registros
        self.curs.execute("SELECT * FROM tipo_persona")
        if not self.curs.fetchone():
            cmd = """INSERT INTO tipo_persona(tipo_persona) values('Natural'),('Juridica')"""
            self.curs.execute(cmd)
            self.conn.commit()
        
        # Verifica si la tabla "metodopago" ya tiene registros
        self.curs.execute("SELECT * FROM metodopago")
        if not self.curs.fetchone():
            cmd = """INSERT INTO metodopago(metodo_pago) values('Efectivo'), ('tarjeta'), ('transferencia'), ('otro')"""
            self.curs.execute(cmd)
            self.conn.commit()
        
        self.trc_tbl('curr_admin')
        
        self.botones = []

    def ins_tbl_telefono(self, indice, numero):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = """INSERT INTO telefono(prefijo, numero)
                    VALUES(?,?)"""
        data_tuple = (indice, numero)
        self.curs.execute(sqltext, data_tuple)
        self.conn.commit()
        self.conn.close()

    def ins_tbl_email(self, correof):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        separador = "@"
        correoS = correof.split(separador)
        correo = correoS[0]  
        dominio = correoS[1]  
              
        sqltext = """INSERT INTO email(correo, dominio)
                    VALUES(UPPER(?), UPPER(?))"""
        data_tuple = (correo, dominio)
        self.curs.execute(sqltext, data_tuple)
        self.conn.commit()
        self.conn.close()

    def ins_tbl_persona(self, usuario, nombre_completo, passwordu, tipo_persona, active):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        
        result = self.conn.execute("SELECT id FROM telefono ORDER BY id DESC LIMIT 1")
        last_id_telefono = result.fetchone()[0]

        result = self.conn.execute("SELECT id FROM email ORDER BY id DESC LIMIT 1")
        last_id_email = result.fetchone()[0]

        nombres_apellidos = nombre_completo.split()
        nombres = nombres_apellidos[:2]
        apellidos = nombres_apellidos[2:]

        if len(nombres_apellidos) <= 2:
            nombres = nombres_apellidos
            apellidos = [None]
        else:
            nombres = nombres_apellidos[:2]
            apellidos = nombres_apellidos[2:]

        if len(nombres) == 1:
            nombre_1 = nombres[0]
            nombre_2 = None
        else:
            nombre_1 = nombres[0]
            nombre_2 = nombres[1] if len(nombres) > 1 else None

        if len(apellidos) == 1:
            apellido_1 = apellidos[0]
            apellido_2 = None
        else:
            apellido_1 = apellidos[0]
            apellido_2 = apellidos[1] if len(apellidos) > 1 else None
        
        sqltext = """INSERT INTO persona(nom1, nom2, ap1, ap2, id_email, id_telefono, id_tipo_persona, active)
                    VALUES(?,?,?,?,?,?,?,?)"""
        
        data_tuple = (nombre_1, nombre_2, apellido_1, apellido_2, last_id_email, last_id_telefono, tipo_persona, active)
        self.curs.execute(sqltext, data_tuple)
           
        result = self.conn.execute("SELECT id FROM persona ORDER BY id DESC LIMIT 1")
        last_id_persona = result.fetchone()[0]
                    
        sqltexta = """INSERT INTO administrador(usuario, passwordu, id_persona)
                    VALUES(?,?,?)"""
        data_tuplea = (usuario, passwordu, last_id_persona)
        self.curs.execute(sqltexta, data_tuplea)
        self.conn.commit()
        self.conn.close()

    def chk_usuario_cont(self, usuario, passwordu):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT EXISTS(SELECT 1 FROM administrador WHERE usuario='{}' AND passwordu='{}' LIMIT 1)".format(
            usuario, passwordu)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        return row[0]

    def chk_exist_user(self, usuario):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT EXISTS(SELECT 1 FROM administrador WHERE usuario='{}' LIMIT 1)".format(
            usuario)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        return row[0]

    def get_user_id(self, usuario):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT id FROM administrador WHERE usuario='{}' LIMIT 1".format(
            usuario)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        return row[0]

    def get_user_name(self, id):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT nom1 FROM persona WHERE id='{}' LIMIT 1".format(id)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        if row is not None:
            return row[0]
        else:
            return None

    def get_user_email(self, id):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT correo FROM email WHERE id='{}' LIMIT 1".format(
            id)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        return row[0]

    def get_user_pswd(self, id):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "SELECT passwordu FROM administrador WHERE id='{}' LIMIT 1".format(
            id)
        self.curs.execute(sqltext)
        row = self.curs.fetchone()
        self.conn.close()
        return row[0]

    def upd_curr_user(self, id):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = """INSERT INTO curr_admin(currid,active)
                    VALUES(?,?)"""
        data_tuple = (id, 1)
        self.curs.execute(sqltext, data_tuple)
        self.conn.commit()
        self.conn.close()

    def upd_user_passwd(self, id, nupwd):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = """UPDATE administrador SET passwordu = '{}' WHERE id = {}""".format(
            nupwd, id)
        print(sqltext)
        self.curs.execute(sqltext)
        self.conn.commit()
        self.conn.close()

    def trc_tbl(self, tbl_name):
        self.conn = sqlite3.connect(self.dbname)
        self.curs = self.conn.cursor()
        sqltext = "DELETE FROM "+tbl_name
        self.curs.execute(sqltext)
        self.conn.commit()
        self.conn.close()
        # return 1

    def ins_tbl_cat(self, nom_cat, icon):
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()

        if bool(icon):
            icon = icon
        else:
            icon = None

        query = "INSERT INTO categoria(nom_cat, icono) values (?, ?)"
        cur.execute(query, (nom_cat, icon))

        con.commit()
        con.close()