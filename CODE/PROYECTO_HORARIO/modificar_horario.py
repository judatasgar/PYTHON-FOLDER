from archivo import cargar_horario, guardar_horario
from horario import quitar_tildes, validar_dia, validar_hora, registrar_evento, normalizar_texto, pedir_hora_validada, evitar_conflictos


def buscador_evento(eventos, materia_ingresado, dia_ingresado):
    materias_simultaneas=[]
    for evento in eventos:
        if quitar_tildes(evento['dia']).lower() == quitar_tildes(dia_ingresado).lower() and quitar_tildes(evento['materia']).lower() == quitar_tildes(materia_ingresado).lower():
            materias_simultaneas.append(evento)
    return materias_simultaneas

def seleccionar_evento(eventos):
        dia_ingresado = input('Ingrese el nombre del dia en el que quiere realizar la modificacion')
        materia_ingresado = input('Ingrese el nombre de la materia que desea modificar')
        eventos_encontrados = buscador_evento(eventos, materia_ingresado, dia_ingresado)
        if len(eventos_encontrados) == 0:
             print('No se han hallado eventos bajos los parametros que establecio ')
             return None 
        elif len(eventos_encontrados) == 1:
             print('Se encontro un unico evento bajo los parametros que establecio ')
             evento_elegido = eventos_encontrados[0]
             print(f'Evento encontrado: {evento_elegido["materia"]} de {evento_elegido["hora_inicio"]} a {evento_elegido["hora_fin"]}')
             return evento_elegido
        else:
             print('Se encontro mas de un evento bajo los parametros que establecio ')
             for i,e in enumerate(eventos_encontrados):
                  print(f'{i+1}: {e["hora_inicio"]} a {e["hora_fin"]} en {e["ubicacion"]}')
             while True:
                 try:
                     opcion = int(input('Seleccione el numeral del evento que quiere modificar: '))
                     if 1 <= opcion <= len(eventos_encontrados):
                         break
                     else:
                         print('Opción inválida. Intente de nuevo.')
                 except ValueError:
                         print('Debe ingresar un número válido.')
             evento_elegido = eventos_encontrados[opcion - 1]
             return evento_elegido

def modificar_evento():
    eventos = cargar_horario()

    materias_existentes = []
    for evento in eventos:
        materias_existentes.append(evento['materia'])
    materias_existentes = list(set(materias_existentes))

    ubicaciones_existentes = []
    for evento in eventos:
        ubicaciones_existentes.append(evento['ubicacion'])
    ubicaciones_existentes = list(set(ubicaciones_existentes))

    evento_a_modificar = seleccionar_evento(eventos)
    if not evento_a_modificar:
        return None
    else:
        print('Por favor ingrese los datos a modificar del evento. Si desea no cambiar alguno, oprima ENTER')

        ubicacion_ingresado = input('Ingrese la ubicacion que desea modificar. Si desea no cambiar alguno, oprima ENTER: ').strip().title()
        if ubicacion_ingresado == '':
            ubicacion_ingresado = evento_a_modificar['ubicacion']
        else:
            ubicacion_ingresado = normalizar_texto(ubicacion_ingresado, ubicaciones_existentes)

        hora_inicio_ingresado = input('Ingrese la hora de inicio (formato 24 horas). Si desea no cambiar alguno, oprima ENTER: ').strip()
        if hora_inicio_ingresado == '':
            hora_inicio_ingresado = evento_a_modificar['hora_inicio']
        else:
            hora_inicio_ingresado = validar_hora(hora_inicio_ingresado)
            while not hora_inicio_ingresado:
                hora_inicio_ingresado = pedir_hora_validada('Ingrese una hora de inicio valida. ')

        hora_fin_ingresado = input('Ingrese la hora de fin (formato 24 horas). Si desea no cambiar alguno, oprima ENTER: ').strip()
        if hora_fin_ingresado == '':
            hora_fin_ingresado = evento_a_modificar['hora_fin']
        else:
            hora_fin_ingresado = validar_hora(hora_fin_ingresado)
            while not hora_fin_ingresado:
                hora_fin_ingresado = pedir_hora_validada('Ingrese una hora de fin valida. ')

        dia_ingresado = input('Ingrese el dia que desea modificar. Si desea no cambiar alguno, oprima ENTER: ').strip().title()
        if dia_ingresado == '':
            dia_ingresado = evento_a_modificar['dia']
        else:
            dia_ingresado = validar_dia(dia_ingresado)
            while not dia_ingresado:
                dia_ingresado = input('Ingrese un dia valido: ').strip().title()
                dia_ingresado = validar_dia(dia_ingresado)

        while not evitar_conflictos(eventos, dia_ingresado, hora_inicio_ingresado, hora_fin_ingresado, evento_a_modificar):
            print('El horario ingresado causa conflictos con eventos previamente registrados. Verifique e ingrese horario deseado')
            hora_inicio_ingresado = pedir_hora_validada('Ingrese la hora de inicio (formato 24 horas): ')
            hora_fin_ingresado = pedir_hora_validada('Ingrese la hora de fin (formato 24 horas): ')

        evento_a_modificar.update({
            'dia': dia_ingresado,
            'hora_inicio': hora_inicio_ingresado,
            'hora_fin': hora_fin_ingresado,
            'ubicacion': ubicacion_ingresado
        })

        guardar_horario(eventos)
        print("Evento modificado exitosamente.")