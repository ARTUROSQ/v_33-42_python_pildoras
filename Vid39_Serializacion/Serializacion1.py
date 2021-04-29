"Serializacion de colecciones de objetos"

"Guardar en un ficheo externo, una coleccion, un diccionario o un objeto, codificado en binario"

"Pickle: Biblioteca necesaria para la serializacion"


import pickle

# Podemos guardar lo que queramos, listas, diccionarios, tuplas...
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

# Escritura en modo binario, vacía el fichero si existe
fichero_binario=open("lista_nombres", "wb")

# Escribe la colección en el fichero 
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)