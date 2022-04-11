

import requests
import bs4
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import date

url = 'https://es.surf-forecast.com/breaks/Pantin/forecasts/latest/six_day'
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
nfila = 0

for fila in tabla.find_all('tr'):
    if nfila == 0:
        for celda in fila.find_all('td'):
            dia.append(celda.text)       
    if nfila == 1:
        for celda in fila.find_all('td'):
            momento.append(celda.text)
    if nfila == 4:
        for celda in fila.find_all('td'):
            olas.append(celda.text)
    if nfila == 5:
        for celda in fila.find_all('td'):
            periodo.append(celda.text)
    if nfila == 7:
        for celda in fila.find_all('td'):
            energia.append(celda.text)
    if nfila == 8:
        for celda in fila.find_all('td'):
            viento.append(celda.text)
    if nfila == 9:
        for celda in fila.find_all('td'):
            direccion_viento.append(celda.text)
    if nfila == 10:
        for celda in fila.find_all('td'):
            marea_alta.append(celda.text)
    if nfila == 11:
        for celda in fila.find_all('td'):
            marea_baja.append(celda.text)
    nfila = nfila+1
    
dia2 = [1]
dia2 *= 36

if momento[0] == 'mañana':
    for i in range(3):
        dia2[i] = dia[0]
    for i in range(3,6):
        dia2[i] = dia[1]
    for i in range(6,9):
        dia2[i] = dia[2]
    for i in range(9,12):
        dia2[i] = dia[3]
    for i in range(12,15):
        dia2[i] = dia[4]
    for i in range(15,18):
        dia2[i] = dia[5]
    for i in range(18,21):
        dia2[i] = dia[6]
    for i in range(21,24):
        dia2[i] = dia[7]
    for i in range(24,27):
        dia2[i] = dia[8]
    for i in range(27,30):
        dia2[i] = dia[9]
    for i in range(30,33):
        dia2[i] = dia[10]
    for i in range(33,36):
        dia2[i] = dia[11]
elif momento[0] == 'tarde':
    for i in range(2):
        dia2[i] = dia[0]
    for i in range(2,5):
        dia2[i] = dia[1]
    for i in range(5,8):
        dia2[i] = dia[2]
    for i in range(8,11):
        dia2[i] = dia[3]
    for i in range(11,14):
        dia2[i] = dia[4]
    for i in range(14,17):
        dia2[i] = dia[5]
    for i in range(17,20):
        dia2[i] = dia[6]
    for i in range(20,23):
        dia2[i] = dia[7]
    for i in range(23,26):
        dia2[i] = dia[8]
    for i in range(26,29):
        dia2[i] = dia[9]
    for i in range(29,32):
        dia2[i] = dia[10]
    for i in range(32,35):
        dia2[i] = dia[11]
    dia2[35] = dia[12]
else:
    dia2[0] = dia[0]
    for i in range(1,4):
        dia2[i] = dia[1]
    for i in range(4,7):
        dia2[i] = dia[2]
    for i in range(7,10):
        dia2[i] = dia[3]
    for i in range(10,13):
        dia2[i] = dia[4]
    for i in range(13,16):
        dia2[i] = dia[5]
    for i in range(16,19):
        dia2[i] = dia[6]
    for i in range(19,22):
        dia2[i] = dia[7]
    for i in range(22,25):
        dia2[i] = dia[8]
    for i in range(25,28):
        dia2[i] = dia[9]
    for i in range(28,31):
        dia2[i] = dia[10]
    for i in range(31,34):
        dia2[i] = dia[11]
    for i in range(34,36):
        dia2[i] = dia[12]
        
month = []
for i in range(len(momento)):
    month.append(actual_date.month)

t = soup.find('span', class_='temp')
temp = t.get_text()
sea_temp = []
for i in range(len(momento)):
    sea_temp.append(temp)
    
dataset = {'mes':month,'dia':dia2,'tramo':momento, 'olas(m/direccion)':olas, 'periodo':periodo, 'energia':energia, 'viento(velocidad/direccion)':viento, 'estado viento':direccion_viento, 'marea_alta':marea_alta, 'marea_baja': marea_baja}
dataframe = pd.DataFrame(dataset)
dataframe.to_csv('prevision_olas_pantin.csv')

