import json
import os  

RUTA_ARCHIVO = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..',
    '..',
    'RAW',
    'PROYECTO_HORARIO',
    'horario_json.json'
)

def cargar_horario():
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            horario = json.load(archivo)
    except FileNotFoundError:
        horario = []
    return horario

def guardar_horario(eventos):
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(eventos, archivo, ensure_ascii=False, indent=4)
