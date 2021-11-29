from tkinter.messagebox import showinfo
from peewee import *
from mysql import *


# Definiciones
MI_DATABASE = 'db_socios.db'

db = SqliteDatabase(MI_DATABASE)


class BaseModel(Model):
    class Meta:
        database = db


class tabla_producto(BaseModel):
    id = PrimaryKeyField(unique=True)
    titulo = CharField()
    descripcion = CharField()


def func_db_iniciar():

    # conectamos a la base de datos
    db.connect()

    # Crea la tabla si no existe
    db.create_tables([tabla_producto])
    #
    if db.table_exists('tabla_producto'):
        print("La Tabla Productos ha sido creada/existe")

# func_db_conectar


def func_db_conectar():

    if db.connect(reuse_if_open=True):
        print("\nSe reconecto a la base de datos!")
    else:
        print("\nLa base de datos esta conectada")


def func_db_desconectar():
    if db.close():
        print("\nConexion con DB terminada")

# chequear que esta abierta
# db.connect(reuse_if_open=True)
# cerrar conexion
# db.close()
# db.is_closed()
# EOF
