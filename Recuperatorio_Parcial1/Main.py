import Funciones  # Importa el modulo Funciones con todas las funciones principales
from Input import pedir_opcion_menu  # Importa la función para pedir la opción del menu

lista_participantes = []  # Lista donde se almacenarán los participantes y sus datos
puntajes_cargados = False  # Bandera para saber si ya se cargaron los puntajes

# Función auxiliar para verificar si los puntajes ya fueron cargados
def verificar_datos():
    if puntajes_cargados == True:
        return True
    else:
        return False

# Bucle principal del programa, muestra el menu y ejecuta la opcion seleccionada
while True:
    print("\n=====================  MENU  ======================\n")
    print("1. Cargar participantes")          # Permite ingresar los nombres de los participantes
    print("2. Cargar puntajes")               # Permite ingresar los puntajes de los jurados
    print("3. Mostrar puntajes")              # Muestra los puntajes y promedios de cada participante
    print("4. Promedios > 4")                 # Muestra participantes con promedio mayor a 4
    print("5. Promedios > 7")                 # Muestra participantes con promedio mayor a 7
    print("6. Promedio por jurado")           # Muestra el promedio de cada jurado
    print("7. Jurado mas estricto")           # Indica cuál jurado fue el mas estricto
    print("8. Buscar participante")           # Permite buscar un participante por nombre
    print("9. Top 3")                         # Muestra los 3 participantes con mayor promedio
    print("10. Orden alfabetico")             # Muestra los participantes ordenados alfabéticamente
    print("11. Sumar puntajes totales")       # Suma todos los puntajes de todos los participantes
    print("12. Mostrar ganador")              # Muestra el ganador del concurso según el mayor promedio
    print("13. Desempatar")                   # Desempata si hay empate en el mayor promedio
    print("0. Salir")                         # Sale del programa
    print("\n===================================================\n")

    opcion = pedir_opcion_menu()  # Solicita al usuario que ingrese una opcion valida

    # Opcion 1: Cargar los nombres de los participantes
    if opcion == 1:
        # Llama a la función para cargar los nombres de los participantes
        lista_participantes = Funciones.cargar_participantes()
        puntajes_cargados = False  # Se deben cargar los puntajes después de cargar los participantes
    
    # Opcion 2: Cargar los puntajes de los jurados para cada participante
    elif opcion == 2:
        # Verifica que primero se hayan cargado los participantes
        if len(lista_participantes) > 0:
            # Llama a la funcion para cargar los puntajes de los jurados
            Funciones.cargar_puntajes(lista_participantes)
            puntajes_cargados = True  # Marca que los puntajes ya fueron cargados
        else:
            # Muestra un mensaje de error si no hay participantes cargados
            print("ERROR: Primero carga los participantes.")
    
    # Opcion 3: Mostrar los puntajes y promedios de cada participante
    elif opcion == 3 and verificar_datos():
        # Llama a la función que muestra los puntajes y promedios de cada participante
        Funciones.mostrar_puntajes(lista_participantes)
    
    # Opcion 4: Mostrar participantes con promedio mayor a 4
    elif opcion == 4 and verificar_datos():
        # Llama a la funcion que muestra los participantes con promedio mayor a 4
        Funciones.mostrar_promedios_mayores(lista_participantes, 4)
    
    # Opcion 5: Mostrar participantes con promedio mayor a 7
    elif opcion == 5 and verificar_datos():
        # Llama a la funcion que muestra los participantes con promedio mayor a 7
        Funciones.mostrar_promedios_mayores(lista_participantes, 7)
    
    # Opcion 6: Mostrar el promedio de cada jurado
    elif opcion == 6 and verificar_datos():
        # Llama a la funcion que calcula y muestra el promedio de cada jurado
        Funciones.promedio_por_jurado(lista_participantes)
    
    # Opcion 7: Indicar cuál jurado fue el mas estricto
    elif opcion == 7 and verificar_datos():
        # Llama a la funcion que indica cuál jurado fue el mas estricto (menor promedio)
        Funciones.jurado_estricto(lista_participantes)
    
    # Opcion 8: Buscar un participante por nombre
    elif opcion == 8 and verificar_datos():
        # Llama a la funcion que permite buscar un participante por su nombre
        Funciones.buscar_participante(lista_participantes)
    
    # Opcion 9: Mostrar el top 3 de participantes con mayor promedio
    elif opcion == 9 and verificar_datos():
        # Llama a la funcion que muestra los 3 participantes con mayor promedio
        Funciones.mostrar_top3(lista_participantes)
    
    # Opcion 10: Mostrar los participantes ordenados alfabéticamente
    elif opcion == 10 and verificar_datos():
        # Llama a la funcion que muestra los participantes ordenados alfabéticamente
        Funciones.ordenar_alfabetico(lista_participantes)
    
    # Opcion 11: Sumar todos los puntajes de todos los participantes
    elif opcion == 11 and verificar_datos():
        # Llama a la funcion que suma todos los puntajes de todos los participantes
        Funciones.sumar_puntajes_totales(lista_participantes)
    
    # Opcion 12: Mostrar el ganador de la competencia
    elif opcion == 12 and verificar_datos():
        # Llama a la funcion que muestra el ganador del concurso basándose en el mayor promedio de puntajes
        Funciones.mostrar_ganador(lista_participantes)
    
    # Opcion 13: Desempatar si hay empate
    elif opcion == 13 and verificar_datos():
        # Llama a la funcion que realiza el desempate entre los participantes con el mayor promedio
        Funciones.desempatar(lista_participantes)
    
    # Opcion 0: Salir del programa
    elif opcion == 0:
        # Muestra un mensaje de despedida y termina el programa
        print("\nEspero haber cumpliddo con todo :)\n")
        break

    # Si no se cumplen las condiciones anteriores, muestra un mensaje de error
    else:
        # Muestra un mensaje de error si faltan cargar participantes o puntajes
        print("ERROR: Primero carga los participantes y puntajes.")