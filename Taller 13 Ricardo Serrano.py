class Empleado:

  def __init__(self, nombre, email,):
    self.nombre = nombre
    self.email = email

  def pagar(self):
    pass

  def mostrar_info(self):
    datos = f'{self.nombre}-{self.email}'
    if isinstance(self, EmpleadoFijo):
      datos += ' - Empleado Fijo'
    elif isinstance(self, EmpleadoHora):
      datos += ' - Empleado Horas'
    else:
      datos += ' - Esto no sirvio'

    return datos

class EmpleadoFijo(Empleado):

  def __init__(self,nombre, email,salario):
    super().__init__(nombre,email)
    self.salario = salario
    self.dias_laborados = 30

  def pagar(self):
    valor = self.salario / 30 * self.dias_laborados
    return valor
  
  def registrar_dias_laborados(self,dias_laborados):
    self.dias_laborados = dias_laborados

class EmpleadoHora(Empleado):
  def __init__(self, nombre, email, valor_hora):
    super().__init__(nombre, email)
    self.valor_hora = valor_hora
    self.horas_trabajadas = 0

  def definir_horas_t(self, horas_trabajadas):
    self.horas_trabajadas = horas_trabajadas

  def pagar(self):
    valor = self.horas_trabajadas * self.valor_hora
    return valor
# --------------------------- MENÚ PRINCIPAL --------------------------------------
empleados = []

while True:
  print('\n\nMENÚ PRINCIPAL')
  print('\n1. Registrarempleado')
  print('\n2. Registrar horas trabajadas')
  print('\n3. Registrar días trabajados')
  print('\n4. Pagar empleados')
  print('\n5. Salir')
  opcion = int(input('Selecciona una opción: '))

  if opcion == 1:
    print('Registro de empleados')
    nombre = input('Nombre: ')
    email = input('Email: ')
    tipo = int(input('Tipo (1. Fijo - 2. Por horas): '))
    
    if tipo == 1:
      salario = float(input('Salario mensual: '))

      empleado = EmpleadoFijo(nombre, email,salario)
      empleados.append(empleado)
    elif tipo == 2:
      valor_hora = float(input('Valor por hora: '))

      empleado = EmpleadoHora(nombre, email, valor_hora)
      empleados.append(empleado)
    else:
      print('Tipo de usuario no reconocido.')
    
    print('\n INFORMACION EMPLEADO')

    for empleado in empleados:
      print(empleado.mostrar_info())
  elif opcion == 5:
    print('\nPrograma Finalizado')
    break
  else:
    print('\nOpción Incorrecta')