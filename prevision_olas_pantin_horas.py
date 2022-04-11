import requests
import bs4
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://es.surf-forecast.com/breaks/Pantin/forecasts/latest'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

x = soup.find_all('table')

tabla = x[2]

dia = []
momento = []
olas = []
periodo = []
viento = []
energia = []
direccion_viento = []
marea_alta = []
marea_baja = []
actual_date = date.today()
nfila=0

for fila in tabla.find_all('tr'):
    if nfila==0:
        ncelda=0
        for celda in fila.find_all('td'):
                 for i in range(8):
                        dia.append(celda.text)
        ncelda=ncelda+1
    if nfila==1:
        for celda in fila.find_all('td'):
            momento.append(celda.text)
    if nfila==4:
        for celda in fila.find_all('td'):
            olas.append(celda.text)
    if nfila==5:
        for celda in fila.find_all('td'):
            periodo.append(celda.text)
    if nfila==7:
        for celda in fila.find_all('td'):
            energia.append(celda.text)
    if nfila==8:
        for celda in fila.find_all('td'):
            viento.append(celda.text)
    if nfila==9:
        for celda in fila.find_all('td'):
            direccion_viento.append(celda.text)
    if nfila == 10:
        for celda in fila.find_all('td'):
            marea_alta.append(celda.text)
    if nfila == 11:
        for celda in fila.find_all('td'):
            marea_baja.append(celda.text)
    nfila=nfila+1

month = []
for i in range(len(dia)):
    month.append(actual_date.month)

dataset = {'mes':month,'dia':dia,'tramo':momento, 'olas(m/direccion)':olas, 'periodo':periodo, 'energia':energia, 'viento(fuerza/direccion)':viento, 'estado viento':direccion_viento, 'marea_alta':marea_alta, 'marea_baja': marea_baja}

dataframe = pd.DataFrame(dataset)
dataframe.to_csv('previson_olas_pantin_horas.csv')
dataframe
