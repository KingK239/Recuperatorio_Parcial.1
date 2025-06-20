# Solicita al usuario que ingrese una opcion de menu valida (entre 0 y 11)
def pedir_opcion_menu():
    while True:
        texto = input("Opcion: ")  # Pide al usuario que ingrese una opcion
        es_numero = True  # Bandera para verificar si el texto ingresado es numerico
        # Recorre cada caracter del texto para validar que sean números
        for caracter in texto:
            if caracter < '0' or caracter > '9':
                es_numero = False  # Si encuentra un caracter no numerico, cambia la bandera
        if es_numero:
            numero = int(texto)  # Convierte el texto a entero
            # Verifica que el numero este dentro del rango permitido (0 a 13)
            if 0 <= numero <= 13:
                return numero  # Retorna la opcion valida
            else:
                print("ERROR: Numero fuera de rango (0 a 13).")
        else:
            print("ERROR: Ingresa solo numeros.")  # Mensaje de error si no es numerico