print("Nolasco_aguilar_martha_sofia_0948_3W")
class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)

estudiante = Estudiante("Juan", "Pérez", "Ingeniería en Sistemas")
estudiante.nombre_completo()
estudiante.mostrar_carrera()

print(" ")