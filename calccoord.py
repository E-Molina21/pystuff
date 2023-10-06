#calculadora para coordenadas desde anguloy y distancias
import os
import csv
import numpy as np
import matplotlib

#abrir el csv con los promedipos de los ángulos y grado, minuto y segundo en columnas separadas.
fl = input('Arrastra el csv donde se encuentran tus coordenadas:')
coordArray = []
dist = []
with open(fl, mode='r')as file:
    csvFl = csv.reader(file)

    next(csvFl)

    for lines in csvFl:
        grad = float(lines[1])
        minu = float(lines[2])
        seg = float(lines[3])
        dis = float(lines[4])
        #print(grad,minu,seg)
        dist.append(dis)
        coord = grad + minu/60 + seg/3600
        coordArray.append(coord)
        #print(f"Coordenadas: ",coord)

#print(coordArray[0])

AzG = input('Grados azimut inicial: ')
AzM = input('Minutos Azimut inicial: ')
AzS = input('Segundos Azimut inicial: ')

AzGd = float(AzG)
AzMd = float(AzM)
AzSd = float(AzS)
AZd = AzGd + AzMd/60 + AzSd/3600 
Azimuts = []
v = AZd 
Azimuts.append(AZd)
for i in range(len(coordArray) - 1):
    v += coordArray[i+1] + 180
    if v > 360:
        v -= 360
    Azimuts.append(v)

#print(Azimuts)

proyx = []
proyy = []

for i in range(len(Azimuts)):
    va = np.sin(np.radians(Azimuts[i]))
    val = va * dist[i]
    proyx.append(val)

print(proyx)

for i in range(len(Azimuts)):
    va = np.cos(np.radians(Azimuts[i]))
    val = va * dist[i]
    proyy.append(val)

print(proyy)
#print(dist)
Ex = np.sum(proyx)
Ey = np.sum(proyy)

print(Ex)
print(Ey)

t = np.sqrt(Ex*Ex + Ey*Ey)
print(t)
perim = np.sum(dist)
ET = t/perim
print(ET)
pres = 1/ET
print('Presición de 1:',pres)

Cx = []
Cy = []

Tx = Ex*Ex
Ty = Ey*Ey


for i in range(len(Azimuts)):
    val = (Ex/perim)*dist[i]
    Cx.append(val)

for i in range(len(Azimuts)):
    val = (Ey/perim)*dist[i]
    Cy.append(val)

#print(Cx)
#print(Cy)

PrX = []
PrY = []

for i in range(len(Cx)):
    v = proyx[i]+np.abs(Cx[i])
    PrX.append(v)

for i in range(len(Cy)):
    v = proyy[i]+np.abs(Cy[i])
    PrY.append(v)

print(PrX)
print(PrY)

spx = np.sum(PrX)
spy = np.sum(PrY)

#print(spx)
#print(spy)
Xi = input("X de inicio: ")
Yi = input("Y de inicio: ")

xi = float(Xi)
yi = float(Yi)

coords = []
inicial = [xi,yi]
coords.append(inicial)
#print(coords)
#for i in range(len(PrX)):
for i in range(len(coordArray) ):
    coordP = coords[-1]
    x0, y0 = coordP
    dx = PrX[i % len(PrX)]
    dy = PrY[i % len(PrY)]
    xs = x0 + dx
    ys = y0 + dy
    coords.append([xs, ys])


for i, coord in enumerate(coords):
    print(f'coordenadas {i + 1}: ({coord[0]}, {coord[1]})')
    