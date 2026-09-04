from archivo import cargar_horario

def ver_horario_semanal():
    eventos = cargar_horario()
    if not eventos:
        print('No hay eventos registrados.')
        return None

    dias = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')

    horas = sorted(list(set(e['hora_inicio'] for e in eventos)))

    def buscar_materia(dia, hora):
        for evento in eventos:
            if evento['dia'] == dia and evento['hora_inicio'] <= hora < evento['hora_fin']:
                return evento['materia']
        return 'Libre'

    ancho_hora = 10
    ancho_dia = 15

    separador = '=' * (ancho_hora + (ancho_dia * len(dias)) + len(dias) + 1)

    print(separador)
    encabezado = f'| {"Hora":<{ancho_hora}}'
    for dia in dias:
        encabezado += f'| {dia:<{ancho_dia}}'
    encabezado += '|'
    print(encabezado)
    print(separador)

    for hora in horas:
        fila = f'| {hora:<{ancho_hora}}'
        for dia in dias:
            materia = buscar_materia(dia, hora)
            fila += f'| {materia:<{ancho_dia}}'
        fila += '|'
        print(fila)

    print(separador)