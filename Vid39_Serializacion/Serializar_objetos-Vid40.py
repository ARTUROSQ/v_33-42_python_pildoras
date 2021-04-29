
import pickle

class Vehiculo():
    
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ", self.marca, "\n Modelo: ", self.modelo, "\n En Marcha: ", self.enmarcha,
              "\n Acelerando", self.acelera, "\n Frenando", self.frena)
        

coche1 = Vehiculo("Mazda", "MX5")

coche2 = Vehiculo("Seat", "Leon")

coche3 = Vehiculo("Renault", "Megane")

coches = [coche1, coche2, coche3] #Metemos los obgetos coche en una lista

fichero = open("losCoches", "wb") #creamos el ficero con permiso escritura binaria con nombre losCoches

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    
    print(c.estado())