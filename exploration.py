from sklearn import datasets
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('data/avocado.csv')

print("Cantidad de filas: ", data.shape[0])
print("Cantidad de columnas: ", data.shape[1])

print("\nPrimeros 100 registros:")
print(data.head(100).to_string())

print("\nUltimos 20 registros:")
print(data.tail(20).to_string())

print("\nPrecio minimo: ", data['AveragePrice'].min())
print("\nPrecio maximo ", data['AveragePrice'].max())
print("\nPrecio Promedio ", data['AveragePrice'].mean())



# Regiones elegidas
regiones = ["Albany", "Atlanta", "Boston"]

plt.figure(figsize=(10, 6))

for region in regiones:
    datos_region = data[data["region"] == region]
    plt.scatter(
        datos_region["year"],
        datos_region["AveragePrice"],
        label=region
    )

plt.xlabel("Año")
plt.ylabel("Precio promedio del aguacate")
plt.title("Precio promedio por año en tres regiones")
plt.legend(title="Región")
plt.grid(True)
plt.tight_layout()
plt.show()
