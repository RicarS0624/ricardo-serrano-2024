class Vehiculo:
    def __init__(self, marca, linea, modelo, color):
        self.marca = marca
        self.linea = linea
        self.modelo = modelo
        self.color = color
        self.estado = "detenido"  # Estado inicial

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Línea: {self.linea}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Estado: {self.estado}")

    def arrancar(self):
        if self.estado == "en movimiento":
            print("El vehículo ya está en movimiento.")
        else:
            self.estado = "en movimiento"
            print("El vehículo ha arrancado.")

    def detener(self):
        if self.estado == "detenido":
            print("El vehículo ya está detenido.")
        else:
            self.estado = "detenido"
            print("El vehículo ha sido detenido.")

def menu():
    vehiculos = []
    continuar = True

    while continuar:
        print("\n--- Menú de Gestión de Vehículos ---")
        print("1. Agregar un nuevo vehículo")
        print("2. Mostrar información de un vehículo")
        print("3. Arrancar un vehículo")
        print("4. Detener un vehículo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            marca = input("Ingrese la marca del vehículo: ")
            linea = input("Ingrese la línea del vehículo: ")
            modelo = input("Ingrese el año del modelo: ")
            color = input("Ingrese el color del vehículo: ")
            vehiculo = Vehiculo(marca, linea, modelo, color)
            vehiculos.append(vehiculo)
            print("Vehículo agregado exitosamente.")

        elif opcion == "2":
            if not vehiculos:
                print("No hay vehículos registrados.")
                continue
            try:
                indice = int(input("Ingrese el número de lista del vehículo: ")) - 1
                if 0 <= indice < len(vehiculos):
                    vehiculos[indice].mostrar_info()
                else:
                    print("Número de lista no válido.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")

        elif opcion == "3":
            if not vehiculos:
                print("No hay vehículos registrados.")
                continue
            try:
                indice = int(input("Ingrese el número de lista del vehículo: ")) - 1
                if 0 <= indice < len(vehiculos):
                    vehiculos[indice].arrancar()
                else:
                    print("Número de lista no válido.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")

        elif opcion == "4":
            if not vehiculos:
                print("No hay vehículos registrados.")
                continue
            try:
                indice = int(input("Ingrese el número de lista del vehículo: ")) - 1
                if 0 <= indice < len(vehiculos):
                    vehiculos[indice].detener()
                else:
                    print("Número de lista no válido.")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.")

        elif opcion == "5":
            print("Saliendo del programa...")
            continuar = False  # Cambia la variable de control para salir del bucle

        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    menu()
