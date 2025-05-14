import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

archivo_csv = '/home/santiago/Escritorio/web/semana06/clase06-1bim-SantiagoVSR/ejemplo1/data/saludos_mundo.csv'

with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    lector = csv.DictReader(csvfile, delimiter='|')  # delimitador
    for fila in lector:
        saludo = Saludo2()
        saludo.mensaje = fila['saludo']
        saludo.tipo = fila['tipo']
        saludo.origen = fila['origen']  # origen = país
        session.add(saludo)

session.commit()
