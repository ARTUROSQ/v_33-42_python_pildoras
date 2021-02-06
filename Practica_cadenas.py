nUsuario = input("Ingresa tu nombre: ")

print("El nombre es: ", nUsuario.upper())

print("El nombre es: ", nUsuario.lower())

print("El nombre es: ", nUsuario.capitalize())

edad = input("Introduce tu edad: ")

print("¿La edad es digito? verdadero o falso: ",edad.isdigit())



while(edad.isdigit()==False):
    
    print("Por favor introduce un valor numérico")
    
    edad= input("Introduce la edad: ")

if(int(edad)<18):
    
    print("No puede pasar")
    
else:
    
    print("Puede pasar")




