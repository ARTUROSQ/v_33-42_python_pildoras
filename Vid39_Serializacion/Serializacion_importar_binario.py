import pickle

# Lectura en modo binario 
fichero=open("lista_nombres", "rb")

# Cargamos los datos del fichero
lista=pickle.load(fichero)

print(lista)

fichero.close()