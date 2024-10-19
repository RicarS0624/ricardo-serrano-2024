class Vehiculo:
    def _init_(self, marca, modelo, año, precio_base):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio_base = precio_base

    def mostrar_info(self):
        return f'{self.marca} {self.modelo} ({self.año}) - Precio base: ${self.precio_base:.2f}'

    def calcular_costo_alquiler(self):
        pass


class Auto(Vehiculo):
    def _init_(self, marca, modelo, año, precio_base, cantidad_pasajeros):
        super()._init_(marca, modelo, año, precio_base)
        self.cantidad_pasajeros = cantidad_pasajeros

    def calcular_costo_alquiler(self):
        return self.precio_base * 1.05


class Motocicleta(Vehiculo):
    def _init_(self, marca, modelo, año, precio_base, cilindraje):
        super()._init_(marca, modelo, año, precio_base)
        self.cilindraje = cilindraje

    def calcular_costo_alquiler(self):
        return self.precio_base * 0.95


class Camion(Vehiculo):
    def _init_(self, marca, modelo, año, precio_base, capacidad_carga):
        super()._init_(marca, modelo, año, precio_base)
        self.capacidad_carga = capacidad_carga

    def calcular_costo_alquiler(self):
        return self.precio_base * 1.2

vehiculos = []

while True:
    print('\n\nMENÚ PRINCIPAL')
    print('1. Registrar Automovil')
    print('2. Mostrar listado de automoviles')
    print('3. Mostrar información de un automovil')
    print('4. Calcular costo de alquiler de un automovil')
    print('5. Salir')
    opcion = int(input('Selecciona una opción: '))

    if opcion == 1:
        print('Registro de automoviles')
        marca = input('Marca: ')
        modelo = input('Modelo: ')
        año = int(input('Año: '))
        precio_base = float(input('Precio base por día: '))
        tipo = int(input('Tipo (1. Auto - 2. Motocicleta - 3. Camión): '))

        if tipo == 1:
            cantidad_pasajeros = int(input('Cantidad de pasajeros: '))
            vehiculo = Auto(marca, modelo, año, precio_base, cantidad_pasajeros)
        elif tipo == 2:
            cilindraje = int(input('Cilindraje: '))
            vehiculo = Motocicleta(marca, modelo, año, precio_base, cilindraje)
        elif tipo == 3:
            capacidad_carga = float(input('Capacidad de carga (toneladas): '))
            vehiculo = Camion(marca, modelo, año, precio_base, capacidad_carga)
        else:
            print('Tipo de vehículo no reconocido.')
            continue
        
        vehiculos.append(vehiculo)
        print('Vehículo registrado con éxito.')

    elif opcion == 2:
        print('Listado de automoviles:')
        for index, vehiculo in enumerate(vehiculos):
            print(f'{index + 1}. {vehiculo.mostrar_info()}')

    elif opcion == 3:
        num_vehiculo = int(input('Selecciona el número del automovil: '))
        if 1 <= num_vehiculo <= len(vehiculos):
            print(vehiculos[num_vehiculo - 1].mostrar_info())
        else:
            print('Número de automovil inválido.')

    elif opcion == 4:
        num_vehiculo = int(input('Selecciona el número del automovil: '))
        if 1 <= num_vehiculo <= len(vehiculos):
            costo = vehiculos[num_vehiculo - 1].calcular_costo_alquiler()
            print(f'El costo de alquiler del automovil es: ${costo:.2f} por día.')
        else:
            print('Número de automovil inválido.')

    elif opcion == 5:
        print('Programa Finalizado')
        break

    else:
        print('Opción Incorrecta')