import mysql.connector

from app.config import *

def conectar():

    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )