import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Función para validar la fecha
def validar_fecha(fecha_str):
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
        return fecha
    except ValueError:
        print("La fecha ingresada no es válida. Intenta de nuevo.")
        return None

# Función para consultar los datos del clima
def obtener_datos_clima(ciudad, fecha):
    url = f"http://api.weatherapi.com/v1/history.json?key=641cb1794a0d4b90bae112227240511&q={ciudad}&dt={fecha}"
    try:
        r = requests.get(url)
        r.raise_for_status()  # Lanza una excepción si el código de estado es 4xx o 5xx
        data = r.json()
        if "error" in data:
            print(f"Error: {data['error']['message']}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None

# Función para mostrar los datos generales del lugar
def mostrar_datos_generales(data):
    ciudad = data['location']['name']
    pais = data['location']['country']
    latitud = data['location']['lat']
    longitud = data['location']['lon']
    print(f"\nDatos de {ciudad}, {pais}:")
    print(f"  - Latitud: {latitud}")
    print(f"  - Longitud: {longitud}")

# Función para graficar precipitaciones por hora
def graficar_precipitaciones(data):
    hourly_data = data['forecast']['forecastday'][0]['hour']
    horas = [hour['time'][-5:] for hour in hourly_data]
    precipitaciones = [hour.get('precip_mm', 0) for hour in hourly_data]

    plt.figure(figsize=(10, 5))
    plt.plot(horas, precipitaciones, marker='o', color='blue', linestyle='-', label='Precipitación (mm)')
    plt.title('Precipitaciones por hora')
    plt.xlabel('Hora')
    plt.ylabel('Precipitación (mm)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Función para graficar las temperaturas mínimas, máximas y promedio por hora
def graficar_temperaturas(data):
    hourly_data = data['forecast']['forecastday'][0]['hour']
    horas = [hour['time'][-5:] for hour in hourly_data]
    temps_min = [hour['temp_c'] for hour in hourly_data]
    temps_max = [hour['temp_c'] for hour in hourly_data]
    temps_prom = [hour['temp_c'] for hour in hourly_data]  # Asumimos que la temperatura es la misma para max, min, y promedio por hora

    plt.figure(figsize=(10, 5))
    plt.plot(horas, temps_min, marker='o', label='Temp. Mínima (°C)', color='blue')
    plt.plot(horas, temps_max, marker='o', label='Temp. Máxima (°C)', color='red')
    plt.plot(horas, temps_prom, marker='o', label='Temp. Promedio (°C)', color='green')
    plt.title('Temperaturas por hora')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

# Función principal que ejecuta el programa
def ejecutar_aplicacion():
    while True:
        print("\nBienvenido al sistema de consulta del clima histórico.")
        
        # Solicitar ciudad y fecha
        ciudad = input("Introduce el nombre de la ciudad o municipio: ").strip()
        fecha = None
        
        while not fecha:
            fecha_input = input("Introduce la fecha (formato: aaaa-mm-dd): ").strip()
            fecha = validar_fecha(fecha_input)
        
        # Obtener los datos de la API
        datos_clima = obtener_datos_clima(ciudad, fecha.strftime("%Y-%m-%d"))
        
        if datos_clima:
            # Mostrar datos generales
            mostrar_datos_generales(datos_clima)
            
            # Graficar precipitaciones y temperaturas
            graficar_precipitaciones(datos_clima)
            graficar_temperaturas(datos_clima)
        
        # Preguntar al usuario si desea continuar
        continuar = input("\n¿Deseas realizar otra consulta? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Hasta luego!")
            break

# Ejecutar la aplicación
if __name__ == "__main__":
    ejecutar_aplicacion()
