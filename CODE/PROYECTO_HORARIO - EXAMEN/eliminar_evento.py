from archivo import cargar_horario, guardar_horario
from modificar_horario import buscador_evento, seleccionar_evento


def eliminar_evento():
    eventos=cargar_horario()
    evento_a_eliminar = seleccionar_evento(eventos)
    if not evento_a_eliminar:
            return None
    else:
         while True:
            try:
                 confirmacion_eliminacion = int(input('Por favor, confirme si desea eliminar este evento de su horario: 1 (Para eliminar)  0 (Para abortar proceso) '))
                 if confirmacion_eliminacion in (1, 0):
                      break
                 else:
                      print('Opción invalida. Intente de nuevo')
            except ValueError:
                      print('Debe ingresar un valor válido')
         if confirmacion_eliminacion == 1:
              eventos.remove(evento_a_eliminar)
              guardar_horario(eventos)
              print(f'Evento "{evento_a_eliminar["materia"]}" eliminado exitosamente.')
         else:
              print('Eliminación cancelada.')
               
               
                       
                 
