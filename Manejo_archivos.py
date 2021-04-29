from io import open

#Importamos de la libreria io el modulo open

archivo_texto=open("archivo.txt", "r+") #w,r,a, r+ - escritura, lectura, agregar, lectura-escritura

#frase = "Estupendo dia para estudiar python \n el sabado"

#archivo_texto.write(frase)

#archivo_texto.close() 



#texto=archivo_texto.read()

#archivo_texto.close()

#print(texto)


#lineas_texto=archivo_texto.readlines()

#archivo_texto.close()

#print(lineas_texto[0])



#archivo_texto.write("\n Siempre es una buena ocasión para estudiar python")

#archivo_texto.close()

#print(archivo_texto.read())

#archivo_texto.seek(11)


"Seek nos pone el cursor en la linea indicada por el numero o parametro de la funcion"
 

#print(archivo_texto.read())

#archivo_texto.seek(0)

#print(archivo_texto.read())

#archivo_texto.seek(11)

"read con el parametro o valor nos lee el texto desde el caracter 0 hasta el caracter del parametro"
"Si se vuelve a imprimir read nos imprime desde la pocicion donde se quedo el cursor."

#print(archivo_texto.read(11))

#print(archivo_texto.read())

"Colocando el puntero exactamente a la mitad del texto"

#archivo_texto.seek(len(archivo_texto.read())/2)

#print(archivo_texto.read())

"Colocar el cursor al final de la primera linea e imprimir desde la segunda linea"

#archivo_texto.seek(len(archivo_texto.readline()))

#print(archivo_texto.read())

"Abrimos el archivo en modo lectura-escritura con r+, escribimos con write"

archivo_texto.write("Comienzo del texto")


"Con readlines obtenemos una lista."

#print(archivo_texto.readlines())

"Con writelines escribimos en nuestro archivo de texto"

lista_texto =archivo_texto.readlines()

lista_texto[1]=" Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()




