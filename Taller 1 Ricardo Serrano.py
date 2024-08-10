from datetime import datetime

def es_bisiesto(anio):
    """Determina si un año es bisiesto o no."""
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

def pedir_datos():
    """Pide los datos al usuario y valida la fecha y hora."""
    try:
        dia = int(input("Ingrese el día (1-31): "))
        mes = int(input("Ingrese el mes (1-12): "))
        anio = int(input("Ingrese el año (por ejemplo, 2024): "))
        hora = int(input("Ingrese la hora (0-23): "))
        minuto = int(input("Ingrese los minutos (0-59): "))
        segundo = int(input("Ingrese los segundos (0-59): "))
        am_pm = input("¿Es AM o PM? (Escriba 'AM' o 'PM'): ").strip().upper()

        # Convertir hora en formato de 24 horas
        if am_pm not in ['AM', 'PM']:
            raise ValueError("El valor para AM/PM debe ser 'AM' o 'PM'.")
        
        if am_pm == 'PM' and hora != 12:
            hora += 12
        elif am_pm == 'AM' and hora == 12:
            hora = 0

        # Verificar si la fecha es válida
        fecha_str = f"{anio}-{mes:02d}-{dia:02d} {hora:02d}:{minuto:02d}:{segundo:02d}"
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        
        # Validar el año bisiesto
        if es_bisiesto(anio):
            print(f"El año {anio} es bisiesto.")
        else:
            print(f"El año {anio} no es bisiesto.")
        
        print(f"Fecha y hora ingresada es válida: {fecha_str}")
    
    except ValueError as e:
        print(f"Error en los datos ingresados: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# Llamar a la función para solicitar datos al usuario
pedir_datos()
