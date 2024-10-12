import json
from datetime import datetime

class Transaccion:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "monto": self.monto,
            "fecha_hora": self.fecha_hora
        }

class BilleteraDigital:
    def __init__(self, id_billetera):
        self.id = id_billetera
        self.saldo = 0.0
        self.transacciones = []

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            transaccion = Transaccion("Depósito", monto)
            self.transacciones.append(transaccion)
            return True
        return False

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            transaccion = Transaccion("Retiro", monto)
            self.transacciones.append(transaccion)
            return True
        return False

    def to_dict(self):
        return {
            "id": self.id,
            "saldo": self.saldo,
            "transacciones": [t.to_dict() for t in self.transacciones]
        }

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.lista_billeteras = []

    def crear_billetera(self):
        id_billetera = f"BW-{len(self.lista_billeteras) + 1}"
        billetera = BilleteraDigital(id_billetera)
        self.lista_billeteras.append(billetera)
        return billetera

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "lista_billeteras": [b.to_dict() for b in self.lista_billeteras]
        }

class SistemaFinanciero:
    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, nombre, email):
        cliente = Cliente(nombre, email)
        self.clientes.append(cliente)

    def crear_billetera(self, email):
        cliente = next((c for c in self.clientes if c.email == email), None)
        if cliente:
            return cliente.crear_billetera()
        return None

    def registrar_transaccion(self, id_billetera, tipo, monto):
        billetera = next((b for c in self.clientes for b in c.lista_billeteras if b.id == id_billetera), None)
        if billetera:
            if tipo == "Depósito":
                return billetera.depositar(monto)
            elif tipo == "Retiro":
                return billetera.retirar(monto)
        return False

    def guardar_datos(self, archivo='datos.json'):
        with open(archivo, 'w') as f:
            json.dump([c.to_dict() for c in self.clientes], f)

    def cargar_datos(self, archivo='datos.json'):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for cliente_data in data:
                    cliente = Cliente(cliente_data['nombre'], cliente_data['email'])
                    for billetera_data in cliente_data['lista_billeteras']:
                        billetera = BilleteraDigital(billetera_data['id'])
                        billetera.saldo = billetera_data['saldo']
                        billetera.transacciones = [Transaccion(t['tipo'], t['monto']) for t in billetera_data['transacciones']]
                        cliente.lista_billeteras.append(billetera)
                    self.clientes.append(cliente)
        except FileNotFoundError:
            pass

# Ejemplo de uso del sistema
if __name__ == "__main__":
    sistema = SistemaFinanciero()
    sistema.cargar_datos()

    # Registrar un nuevo cliente
    sistema.registrar_cliente("Juan Pérez", "juan@example.com")
    
    # Crear una billetera para el cliente
    billetera = sistema.crear_billetera("juan@example.com")
    
    # Realizar transacciones
    sistema.registrar_transaccion(billetera.id, "Depósito", 100.0)
    sistema.registrar_transaccion(billetera.id, "Retiro", 50.0)

    # Guardar datos en archivo JSON
    sistema.guardar_datos()