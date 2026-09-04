from horario import registrar_evento
from modificar_horario import modificar_evento
from eliminar_evento import eliminar_evento
from generar_horario_estructurado import ver_horario_semanal
from reporte import generar_reporte


def menu():
    while True:
        print('=' * 42)
        print('GENERADOR DE HORARIOS PARA ESTUDIANTES')
        print('=' * 42)
        print('1. Registrar una materia o actividad')
        print('2. Ver horario semanal')
        print('3. Modificar una materia o actividad')
        print('4. Eliminar una materia o actividad')
        print('5. Generar reporte del horario')
        print('6. Salir')
        print('=' * 42)

        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            registrar_evento()
        elif opcion == '2':
            ver_horario_semanal()
        elif opcion == '3':
            modificar_evento()
        elif opcion == '4':
            eliminar_evento()
        elif opcion == '5':
            generar_reporte()
        elif opcion == '6':
            print('Gracias por usar el Generador de Horarios. ¡Hasta pronto!')
            break
        else:
            print('Opción inválida. Intente de nuevo.')


if __name__ == '__main__':
    menu()