class MobilePhone:
        def __init__(self, manufacturer, screensize, numcores):
            self.manufacturer = manufacturer
            self.screen_size = float(screensize)
            self.num_cores = int(numcores)
            self.apps = []
            self.apps_desinstaladas = []
            self.status = False
        
        def power_on(self):
             self.status = True
             print("Bienvenido")
        
        def power_off(self):
             self.status = False
             print("Adiós")

        def install_app(self, app):
             self.apps.append(app)
        
        def uninstall_app(self, app):
            self.apps.remove(app)
            self.apps_desinstaladas.append(app)


celphone1 = MobilePhone("Nokia", 8.8, 10)
print(celphone1.manufacturer, celphone1.screen_size, celphone1.num_cores)


celphone1.power_on()
print("power celphone1 on: ", celphone1.status)

celphone1.install_app("WhatsApp")
celphone1.install_app("Instagram")
print("Aplicaciones instaladas correctamente: ", celphone1.apps)

celphone1.uninstall_app("WhatsApp")
print("Aplicaciones desinstaladas correctamente: ", celphone1.apps_desinstaladas)

celphone1.power_off()
print("power celphone1 on: ", celphone1.status)

