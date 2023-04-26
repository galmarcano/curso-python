#Creando una clase
class Transporte:
    pass

#Instanciar la clase y crear un objeto
transporte1 = Transporte()
transporte2 = Transporte()
transporte3 = Transporte()
transporte4 = Transporte()

print(type(transporte1)) #para saber el tipo de la variable, en este caso es una clase y pertenece a clase Transporte, es lo que indica

class Droid:
    def switch_on(self):
        print("Hola soy un droid, y estoy a tu orden")
        self.power_on = True

    def switch_off(self):
        print("Adiós, enciéndeme cuando me necesites")
        self.power_on = False

k8_arthur = Droid()
k8_citripio = Droid()

k8_arthur.switch_on()
print("power Arthur on: ", k8_arthur.power_on)
k8_citripio.switch_off()
print("power Citripio off: ", k8_citripio.power_on)
k8_arthur.switch_off()
print("power Arthur off: ", k8_arthur.power_on)

#con el método constructor, que es el método que tienen por defecto todas las variables solo con llamar la clase:

class Droid:
    def __init__(self):
        self.power_on = False

    def switch_on(self):
        print("Hola soy un droid, y estoy a tu orden")
        self.power_on = True

    def switch_off(self):
        print("Adiós, enciéndeme cuando me necesites")
        self.power_on = False

k8_arthur = Droid()
k8_citripio = Droid()

k8_arthur.switch_on()
print("power Arthur on: ", k8_arthur.power_on)
print("power Citripio off: ", k8_citripio.power_on)
k8_arthur.switch_off()
print("power Arthur off: ", k8_arthur.power_on)

#nueva clase:

class Vehicle:
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle("Sedan", "Aveo")
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle("Pickup", "Ranger")
print(pickup.type_vehicle, pickup.model_vehicle)


