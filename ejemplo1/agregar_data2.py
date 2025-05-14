import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

archivo_csv = '/mnt/data/saludos_mundo.csv'

with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
    lector = csv.DictReader(csvfile, delimiter='|')  # delimitador corregido
    for fila in lector:
        saludo = Saludo()
        saludo.mensaje = fila['saludo']
        saludo.tipo = fila['tipo']
        saludo.pais = fila['origen']  # origen = país
        session.add(saludo)

session.commit()
