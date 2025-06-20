from Input import pedir_opcion_menu

# Solicita al usuario un nombre valido (minimo 3 letras, solo letras y espacios)
def pedir_nombre():
    while True:
        nombre = input("Nombre del participante: ")
        # Verifica que el nombre tenga al menos 3 caracteres
        if len(nombre) >= 3:
            letras_validas = True
            # Recorre cada letra del nombre para validar que sean letras o espacios
            for letra in nombre:
                es_letra = (letra >= "a" and letra <= "z") or (letra >= "A" and letra <= "Z")
                if not (es_letra or letra == " "):
                    letras_validas = False
            # Si todas las letras son validas, retorna el nombre
            if letras_validas:
                return nombre
            else:
                print("ERROR: Solo letras y espacios.")
        else:
            print("ERROR: Minimo 3 letras.")

# Solicita al usuario un puntaje para un jurado especifico (entre 1 y 10)
def pedir_puntaje(numero_jurado):
    while True:
        texto = input("Puntaje jurado " + str(numero_jurado) + ": ")
        es_numero = True
        # Verifica que todos los caracteres sean numeros
        for caracter in texto:
            if caracter < '0' or caracter > '9':
                es_numero = False
        if es_numero:
            numero = int(texto)
            # Verifica que el numero esté en el rango permitido
            if numero >= 1 and numero <= 10:
                return numero
            else:
                print("ERROR: Entre 1 y 10.")
        else:
            print("ERROR: Solo numeros.")

# Crea una lista de 5 participantes vacios (nombre, lista de puntajes y promedio)
def cargar_participantes():
    lista_participantes = [None] * 5  # Inicializa la lista con 5 elementos vacios
    for posicion in range(5):
        print("\nParticipante", posicion + 1)
        nombre = pedir_nombre()  # Pide el nombre del participante
        # Cada participante es una lista: [nombre, [], 0.0]
        lista_participantes[posicion] = [nombre, [], 0.0]
    return lista_participantes

# Carga los puntajes de 3 jurados para cada participante y calcula su promedio
def cargar_puntajes(lista_participantes):
    for indice_participante in range(5):
        nombre = lista_participantes[indice_participante][0]
        print("\nPuntajes de", nombre)
        # Pide los puntajes de los 3 jurados
        puntaje_1 = pedir_puntaje(1)
        puntaje_2 = pedir_puntaje(2)
        puntaje_3 = pedir_puntaje(3)
        # Guarda los puntajes y el promedio en la lista del participante
        lista_participantes[indice_participante][1] = [puntaje_1, puntaje_2, puntaje_3]
        lista_participantes[indice_participante][2] = (puntaje_1 + puntaje_2 + puntaje_3) / 3

# Muestra el nombre, los puntajes y el promedio de cada participante
def mostrar_puntajes(lista_participantes):
    for participante in lista_participantes:
        nombre = participante[0]
        puntajes = participante[1]
        promedio = participante[2]
        print(nombre, "->", puntajes, "-> Promedio:", "%.2f" % promedio)

# Muestra los participantes cuyo promedio es mayor al minimo indicado
def mostrar_promedios_mayores(lista_participantes, minimo):
    hay_resultados = False  # Bandera para saber si hay algun resultado
    for participante in lista_participantes:
        nombre = participante[0]
        promedio = participante[2]
        if promedio > minimo:
            print(nombre, "->", "%.2f" % promedio)
            hay_resultados = True
    if not hay_resultados:
        print("ERROR: Nadie supera ese promedio.")

# Calcula y muestra el promedio de cada jurado considerando todos los participantes
def promedio_por_jurado(lista_participantes):
    suma_jurados = [0, 0, 0]  # Acumuladores para cada jurado
    for participante in lista_participantes:
        puntajes = participante[1]
        for numero_de_jurado in range(3):
            suma_jurados[numero_de_jurado] += puntajes[numero_de_jurado]
    # Calcula y muestra el promedio de cada jurado
    for numero_de_jurado in range(3):
        promedio = suma_jurados[numero_de_jurado] / 5
        print("Jurado", numero_de_jurado + 1, "->", "%.2f" % promedio)

# Muestra cual jurado fue el mas estricto (el de menor promedio)
def jurado_estricto(lista_participantes):
    suma_jurados = [0, 0, 0]  # Acumuladores para cada jurado
    for participante in lista_participantes:
        puntajes = participante[1]
        for numero_de_jurado in range(3):
            suma_jurados[numero_de_jurado] += puntajes[numero_de_jurado]
    # Calcula los promedios de cada jurado
    promedios = [suma / 5 for suma in suma_jurados]
    promedio_mas_bajo = min(promedios)
    # Busca y muestra el jurado con el promedio mas bajo
    for numero_de_jurado in range(3):
        if promedios[numero_de_jurado] == promedio_mas_bajo:
            print("EL Jurado N°", numero_de_jurado + 1, "es el mas estricto.")

# Permite buscar un participante por nombre hasta que se encuentre
def buscar_participante(lista_participantes):
    encontrado = False
    while encontrado == False:
        nombre_buscado = input("Buscar nombre: ").lower()
        for participante in lista_participantes:
            nombre = participante[0]
            if nombre.lower() == nombre_buscado:
                puntajes = participante[1]
                promedio = participante[2]
                print(nombre, "->", puntajes, "-> Promedio:", "%.2f" % promedio)
                encontrado = True
                break
        if encontrado == False:
            print("ERROR: El nombre que buscas NO conicide con los datos ingresados.")

# Muestra los 3 participantes con mayor promedio
def top3(lista_participantes): #cambiar top3 por: mostrar_top3/calcular_top3
    copia = lista_participantes[:]  # Crea una copia de la lista para no modificar la original
    # Ordena la copia de la lista por promedio descendente (mayor a menor)
    for posicion_actual in range(5):
        for siguiente_posicion in range(posicion_actual + 1, 5):
            if copia[siguiente_posicion][2] > copia[posicion_actual][2]:
                copia[posicion_actual], copia[siguiente_posicion] = copia[siguiente_posicion], copia[posicion_actual]
    # Muestra los tres primeros participantes con mayor promedio
    for lugar in range(3):
        nombre = copia[lugar][0]
        promedio = copia[lugar][2]
        print(nombre, "->", "%.2f" % promedio)

# Ordena y muestra los participantes por nombre alfabéticamente (A-Z)
def ordenar_alfabetico(lista_participantes):
    copia = lista_participantes[:]  # Crea una copia de la lista para no modificar la original
    # Ordena la copia de la lista por nombre (de la A a la Z)
    for posicion_actual in range(5):
        for siguiente_posicion in range(posicion_actual + 1, 5):
            if copia[siguiente_posicion][0].lower() < copia[posicion_actual][0].lower():
                copia[posicion_actual], copia[siguiente_posicion] = copia[siguiente_posicion], copia[posicion_actual]
    # Muestra los participantes ordenados alfabeticamente
    for participante in copia:
        nombre = participante[0]
        promedio = participante[2]
        print(nombre, "-> Promedio:", "%.2f" % promedio)

# Funcion para sumar todos los puntajes de todos los participantes y mostrar el total
def sumar_puntajes_totales(lista_participantes):
    suma_total = 0
    for participante in lista_participantes:
        suma_total += sum(participante[1])
    print("Suma total de todos los puntajes:", suma_total)

# Muestra el ganador del concurso basándose en el promedio de puntajes
def mostrar_ganador(lista_participantes):
    # Emepezamos buscando el mayor promedio encontrado en -1
    mayor_promedio = -1
    # Variables para guardar el nombre del/los ganadores
    nombre_1 = ""
    nombre_2 = ""

    # Recorre la lista de participantes
    for participante in lista_participantes:
        promedio = participante[2]  # El promedio está en la posicion 2
        nombre = participante[0]    # El nombre está en la posicion 0
        if promedio > mayor_promedio:
            # Si encuentra un promedio mayor, actualiza el mayor promedio y el nombre del ganador
            mayor_promedio = promedio
            nombre_1 = nombre
            nombre_2 = ""  # Reinicia nombre_2 porque hay un nuevo maximo
        elif promedio == mayor_promedio:
            # Si hay empate, guarda el segundo nombre (solo el primero que empata)
            if nombre_2 == "":
                nombre_2 = nombre

    # Si no hubo empate, muestra el ganador
    if nombre_2 == "":
        print("El ganador es:", nombre_1)
    else:
        # Si hubo empate, muestra los nombres y avisa que debe desempatarse
        print("Hay un empate entre:", nombre_1, "y", nombre_2)
        print("Debe realizarse un desempate.")

# Desempata entre los participantes con el mayor promedio el ganador
def desempatar(lista_participantes):
    # Inicializa la variable para guardar el mayor promedio encontrado
    mayor_promedio = -1
    # Inicializa la variable para guardar el nombre del ganador
    ganador = ""

    # Recorre la lista de participantes
    for participante in lista_participantes:
        promedio = participante[2]  # Obtiene el promedio del participante
        nombre = participante[0]    # Obtiene el nombre del participante
        if promedio > mayor_promedio:
            # Si el promedio es mayor al mayor encontrado hasta ahora, actualiza el mayor promedio y el nombre del ganador
            mayor_promedio = promedio
            ganador = nombre
        elif promedio == mayor_promedio:
            # Si hay empate en el mayor promedio, elige el nombre que sea menor alfabeticamente
            if nombre < ganador:
                ganador = nombre

    # Informa que hubo empate y muestra el ganador elegido alfabeticamente
    print("Empate entre los mejores promedios.")
    print("El ganador despues del desempate es:", ganador)