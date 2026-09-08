import unicodedata
from archivo import cargar_horario, guardar_horario

def quitar_tildes(texto): 
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')
    return texto_sin_tildes


dias_semana=('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')

horas_validas = []
for i in range(6, 20):
    hora = str(i).zfill(2) + ':00'
    horas_validas.append(hora)



def normalizar_texto(texto_nuevo, lista_existente):
    texto_normalizado = quitar_tildes(texto_nuevo).lower()
    for texto in lista_existente:
        if quitar_tildes(texto).lower() == texto_normalizado:
            return texto
    return texto_nuevo

def validar_dia(dia):
    dia_limpio = quitar_tildes(dia).lower()
    for d in dias_semana:
        if quitar_tildes(d).lower() == dia_limpio:
            return d
    return None

def validar_hora(hora):
    if hora.count(':') == 1:
        parte_hora = hora.split(':')
        numero = str(parte_hora[0])
        hora = numero.zfill(2) + ':00'
    elif hora.count(':') == 0:
            numero = str(hora)
            hora = numero.zfill(2) + ':00'
    else:
        return None
    if not numero.isdigit():
            return None
    for h in horas_validas:
        if h == hora:
            return h
    return None

def pedir_hora_validada(mensaje):
     hora = input(mensaje).strip()
     hora = validar_hora(hora)
     while not hora:
         print('Hora invalida. Por favor, ingrese una hora válida (de 06:00 a 20:00). ')
         hora = input(mensaje).strip()
         hora = validar_hora(hora)
     return hora

def evitar_conflictos(eventos, dia_ingresado, hora_inicio_ingresado, hora_fin_ingresado, ignorar=None):
    for evento in eventos:
        if evento == ignorar:
            continue
        if evento['dia'] == dia_ingresado:
            if (hora_inicio_ingresado < evento['hora_fin'] and hora_fin_ingresado > evento['hora_inicio']):
                return False
    return True


def registrar_evento():
    eventos = cargar_horario()
    materias_existentes = list(set(e['materia'] for e in eventos))
    ubicaciones_existentes = list(set(e['ubicacion'] for e in eventos))

    nombre_materia = input('Ingrese el nombre de la materia: ').strip().title()
    nombre_materia = normalizar_texto(nombre_materia, materias_existentes)
    while nombre_materia == '':
            print('Nombre de materia no especificado. Por favor, ingrese un nombre válido para la materia.')
            nombre_materia = input('Ingrese el nombre de la materia: ').strip().title()
    dia_semana = input('Ingrese el día de la semana: ').strip().title()
    dia_semana = validar_dia(dia_semana)
    while not dia_semana:
            print('Día de la semana invalido. Por favor, ingrese un día válido (Lunes, Martes, Miércoles, Jueves, Viernes).')
            dia_semana = input('Ingrese el día de la semana: ').strip().title()
            dia_semana = validar_dia(dia_semana)
    hora_inicio = pedir_hora_validada('Ingrese la hora de inicio (formato 24 horas): ')
    hora_fin = pedir_hora_validada('Ingrese la hora de fin (formato 24 horas): ')
    while hora_fin <= hora_inicio:
            print('La hora de fin debe ser posterior a la hora de inicio. Por favor, ingrese una hora de fin válida.')
            hora_fin = pedir_hora_validada('Ingrese la hora de fin (formato 24 horas): ')
    lugar_evento = input('Ingrese el nombre del lugar donde se llevará a cabo el evento: ').strip().title()
    if lugar_evento!= '':
        lugar_evento = normalizar_texto(lugar_evento, ubicaciones_existentes)
    else:
        lugar_evento = 'No especificado'
    
    while not evitar_conflictos (eventos, dia_semana, hora_inicio, hora_fin):
        print('El horario ingresado causa conflictos con eventos previamente registrados. Verifique e ingrese horario deseado')
        hora_inicio = pedir_hora_validada('Ingrese la hora de inicio (formato 24 horas): ')
        hora_fin = pedir_hora_validada('Ingrese la hora de fin (formato 24 horas): ')

    evento = {'materia': nombre_materia, 
                  'dia': dia_semana, 
                  'hora_inicio': hora_inicio, 
                  'hora_fin': hora_fin, 
                  'ubicacion': lugar_evento
                  }

    eventos.append(evento)
    guardar_horario(eventos)
    print(f'Materia {nombre_materia} registrada exitosamente el {dia_semana} de {hora_inicio} a {hora_fin} en {lugar_evento} .')