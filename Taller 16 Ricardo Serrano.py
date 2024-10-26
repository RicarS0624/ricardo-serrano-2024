class Animal:
    def __init__(self, nombre, edad, fecha_ingreso, **kwargs):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = fecha_ingreso
        self.atributos_adicionales = kwargs

    def mostrar_detalles(self):
        detalles = f"Nombre: {self.nombre}\nEdad: {self.edad}\nFecha de Ingreso: {self.fecha_ingreso}"
        for key, value in self.atributos_adicionales.items():
            detalles += f"\n{key.capitalize()}: {value}"
        return detalles


class Perro(Animal):
    def __init__(self, nombre, edad, fecha_ingreso, raza, entrenado, **kwargs):
        super().__init__(nombre, edad, fecha_ingreso, **kwargs)
        self.atributos_adicionales['raza'] = raza
        self.atributos_adicionales['entrenado'] = entrenado


class Gato(Animal):
    def __init__(self, nombre, edad, fecha_ingreso, tipo_pelaje, esterilizado, **kwargs):
        super().__init__(nombre, edad, fecha_ingreso, **kwargs)
        self.atributos_adicionales['tipo_pelaje'] = tipo_pelaje
        self.atributos_adicionales['esterilizado'] = esterilizado


class Ave(Animal):
    def __init__(self, nombre, edad, fecha_ingreso, tipo, vuela, **kwargs):
        super().__init__(nombre, edad, fecha_ingreso, **kwargs)
        self.atributos_adicionales['tipo'] = tipo
        self.atributos_adicionales['vuela'] = vuela


if __name__ == "__main__":
    perro = Perro(nombre="Belico", edad=4, fecha_ingreso="2023-09-21", raza="Labrador", entrenado=True, color="Marrón")
    gato = Gato(nombre="Clark", edad=1, fecha_ingreso="2023-02-01", tipo_pelaje="Corto", esterilizado=True, microchip=True)
    ave = Ave(nombre="Kevin", edad=1, fecha_ingreso="2023-06-05", tipo="Canario", vuela=True, habitat="Cerca de la ventana")

    print("Detalles del Perro:")
    print(perro.mostrar_detalles())
    print("\nDetalles del Gato:")
    print(gato.mostrar_detalles())
    print("\nDetalles del Ave:")
    print(ave.mostrar_detalles())