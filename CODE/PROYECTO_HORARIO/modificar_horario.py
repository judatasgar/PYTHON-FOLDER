from CODE.PROYECTO_HORARIO.archivo import cargar_horario, guardar_horario
from CODE.PROYECTO_HORARIO.horario import quitar_tildes, validar_dia, validar_hora

def buscador_evento(eventos, materia_ingresado, dia_ingresado):
    materias_simultaneas=[]
    for evento in eventos:
        if quitar_tildes(evento['dia']) == quitar_tildes(dia_ingresado) and quitar_tildes(evento['materia']) == quitar_tildes(materia_ingresado):
            materias_simultaneas.append(evento)
    return materias_simultaneas

def seleccionar_evento():
        dia_ingresado = input('Ingrese el nombre del dia en el que quiere realizar la modificacion')
        materia_ingresado = input('Ingrese el nombre de la materia que desea modificar')
        eventos = cargar_horario()
        eventos_encontrados = buscador_evento(eventos, materia_ingresado, dia_ingresado)
        if len(eventos_encontrados) == 0:
             print('No se han hallado eventos bajos los parametros que establecio ') 
        elif len(eventos_encontrados) == 1:
             print('Se encontro un unico evento bajo los parametros que establecio ')
             evento_elegido = eventos_encontrados[0]
             print(f'Evento encontrado: {evento_elegido["materia"]} de {evento_elegido["hora_inicio"]} a {evento_elegido["hora_fin"]}')
        else:
             print('Se encontro mas de un evento bajo los parametros que establecio ')
        for i,e in enumerate(eventos_encontrados):
            print(f'{i+1}: {e["hora_inicio"]} a {e["hora_fin"]} en {e["ubicacion"]}')
        opcion = int(input('Seleccione el numeral del evento que quiere modificar'))
        evento_elegido=eventos_encontrados[opcion-1]
        return evento_elegido


def modificar_evento():


    print('Por favor ingrese los datos a modificar del evento. Si desea no cambiar alguno, oprima ENTER')   
    materia_ingresado = input('Ingrese el nombre de la materia que desea modificar')
    hora_inicio = input('Ingrese la hora de inicio (formato 24 horas): ')
    hora_fin = input('Ingrese la hora de fin (formato 24 horas): ')










