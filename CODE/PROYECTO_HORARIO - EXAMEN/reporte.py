import json
import os
from archivo import cargar_horario, guardar_horario

RUTA_REPORTE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..',
    '..',
    'PROCCESED',
    'PROYECTO_HORARIO',
    'reporte_horario.json'
)


def generar_reporte():
    eventos = cargar_horario()
    if not eventos:
        print('No hay eventos registrados.')
        return None

    dias = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')

    reporte = []
    for dia in dias:
        eventos_del_dia = [e for e in eventos if e['dia'] == dia]
        if eventos_del_dia:
            eventos_del_dia.sort(key=lambda e: e['hora_inicio'])
            reporte.append({
                'dia': dia,
                'eventos': [
                    {
                        'materia': e['materia'],
                        'hora_inicio': e['hora_inicio'],
                        'hora_fin': e['hora_fin'],
                        'ubicacion': e['ubicacion']
                    } for e in eventos_del_dia
                ]
            })

    separador = '=' * 42
    print(separador)
    print('REPORTE DEL HORARIO SEMANAL')
    print(separador)

    contador = 0
    for bloque in reporte:
        print(f'{bloque["dia"]}:')
        for ev in bloque['eventos']:
            ubicacion = f' en {ev["ubicacion"]}' if ev['ubicacion'] and ev['ubicacion'] != 'Lugar no especificado' else ''
            print(f'  - {ev["materia"]} ({ev["hora_inicio"]} - {ev["hora_fin"]}){ubicacion}')
        print('-' * 42)
        contador += 1
        if contador % 2 == 0 and contador < len(reporte):
            input('Presione ENTER para continuar...')

    os.makedirs(os.path.dirname(RUTA_REPORTE), exist_ok=True)
    with open(RUTA_REPORTE, 'w', encoding='utf-8') as archivo:
        json.dump(reporte, archivo, ensure_ascii=False, indent=4)

    print('Reporte guardado en reporte_horario.json')