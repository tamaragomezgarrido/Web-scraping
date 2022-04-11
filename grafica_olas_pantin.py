#Gráfica del dataset.
#Extraemos la altura de las olas mediante la siguiente función:

import re
def extraer_numero(celda):
    m = re.match(r'-?\d+\.?\d*', celda)
    if m:
      # Si hubo coincidencia, m.group() devuelve el texto que coincidió
      # Basta convertirlo en entero
        return float(m.group())
    else:
      # Si no hubo coincidencia (lo que ocurre también en celdas vacías)
      # el valor a retornar es cero
        return 0

data_pantin = pd.read_csv('/home/datasci/prevision_olas_pantin.csv')
    
data_pantin["olas(m)"] = data_pantin["olas(m/direccion)"].map(extraer_numero)

#Juntamos las columas mes,dia y tramo.
data_pantin['fecha'] = data_pantin["mes"].map(str) + "-" + data_pantin["dia"] + " " + data_pantin['tramo']

#Creamos la gráfica: altua de las olas cada día.
import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
ax = plt.subplot()
x_values = data_pantin['fecha']
y_values = data_pantin['olas(m)']
plt.plot(x_values,y_values)
ax.set_xticks(x_values)                    
ax.set_xticklabels(x_values,rotation=90)
ax.set_xlabel('Fecha')
ax.set_ylabel('Altura olas')
plt.savefig('Altura olas Pantin.jpg', bbox_inches='tight')



