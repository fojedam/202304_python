# Definir la lista con los diccionarios
lista = [
    {"clave1": "valor1", "clave2": "valor2"},
    {"clave1": "valor3", "clave2": "valor4"},
    {"clave1": "valor5", "clave2": "valor6"}
]

# Acceder al diccionario en el índice deseado de la lista
indice = 1  # Índice del diccionario que deseas modificar
diccionario = lista[indice]

# Modificar el valor en el diccionario
nuevo_valor = "nuevo_valor"
diccionario["clave1"] = nuevo_valor

# Imprimir la lista actualizada
print(lista)

def cambiar_valor_lista_diccionarios(lista, indice, clave, nuevo_valor):
    # Verificar si el índice es válido
    if indice >= 0 and indice < len(lista):
        # Acceder al diccionario en el índice deseado de la lista
        diccionario = lista[indice]
        
        # Modificar el valor en el diccionario
        diccionario[clave] = nuevo_valor
    else:
        print("El índice está fuera de rango.")

# Ejemplo de uso
lista = [
    {"clave1": "valor1", "clave2": "valor2"},
    {"clave1": "valor3", "clave2": "valor4"},
    {"clave1": "valor5", "clave2": "valor6"}
]

cambiar_valor_lista_diccionarios(lista, 1, "clave1", "nuevo_valor")

# Imprimir la lista actualizada
print(lista)


###############################################
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}

jugadores_futbol = directorio_deportes['fútbol']
if 'Messi' in jugadores_futbol:
    indice_messi = jugadores_futbol.index('Messi')
    jugadores_futbol[indice_messi] = 'Pelé'

print(directorio_deportes)