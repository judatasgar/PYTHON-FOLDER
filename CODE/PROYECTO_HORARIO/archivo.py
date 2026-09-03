import json

def cargar_horario():
    try:
        with open('horario_json.json', 'r', encoding='utf-8') as archivo:
            horario = json.load(archivo)
    except FileNotFoundError:
        horario = []
    return horario

def guardar_horario(eventos):
    with open('horario_json.json', 'w', encoding='utf-8') as archivo:
        json.dump(eventos, archivo, ensure_ascii=False, indent=4)
