import requests
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMZN&interval=60min&apikey=5V02CIE131TAY8YV"
resultado =  requests.get(url)
contenido =  resultado.json()

series_tiempo = contenido["Time Series (60min)"]

alto = []
bajo = []
cierre = []
etiqueta = []
for tiempo in series_tiempo:
    datos = series_tiempo[tiempo]

    alto.append(float(datos["2. high"]))
    bajo.append(float(datos["3. low"]))
    cierre.append(float(datos["4. close"]))
    etiqueta.append(tiempo)

alto = list(reversed(alto))
bajo = list(reversed(bajo))
cierre = list(reversed(cierre))
etiqueta = list(reversed(etiqueta))

x1= np.array(etiqueta)
y1= np.array(cierre)
y2 = np.array(bajo)
y3= np.array(alto)

plt.plot(x1, y1, x1, y2, x1, y3)
plt.show()