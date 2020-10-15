# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:14:05 2020

@author: Mauricio
"""


# Esta libreria permite combinar o permutar segun el caso
from itertools import  permutations


# Tarea semana tres: implementacion de diccionarios y en general todo lo trabajasdo hasta la fecha
# problema de optimizacion de distancias
# Nueva version en la lógica del programa

#Definicion de los diccionarios de ejemplo
ciudades1={('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

ciudades2={('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106, ('E', 'D'): 25, ('E', 'E'): 0}


#Definicion de rutas a evaluar
ruta1= ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
ruta2= ['H', 'B', 'E', 'A', 'C', 'D', 'H']
ruta3=['H','A','B','C','D','H']
ruta4= ['H','A','B','F','E','H']



def ruteo(distancias:dict, ruta:list)->dict:
    try:
        #Validacion del diccionario de entrada    
        # Validacion que todos sean numeros
        for x in distancias:
            if type(distancias[x])!= int:
                raise Exception("Por favor revisar los datos de entrada")
        # Validacion de que inicio y final sea cero
        for x in distancias:
            if x[0]==x[1] and distancias[x]!=0:
                raise Exception("Por favor revisar los datos de entrada")
        ruta_corta=ruta.copy()
        ruta_corta.pop(0)   # Ellimino la salida
        ruta_corta.pop(len(ruta_corta)-1)   # Elimino la llegada
        permutado=list(permutations(ruta_corta, len(ruta_corta)))
                
        # Conversion de las tuplas a listas
        lista=[]
            
        for x in range(0,len(permutado)):
            lista.append(list(permutado[x]))
                
        #Insercion de inicio y final en cada lista
        for x in range(0,len(lista)):
            lista[x].insert(0,ruta[0])
            lista[x].append(ruta[len(ruta)-1])
      
        
        totales=[]
        # inicio de la sumatoria de cada ruta
        for x in range(0,len(lista)):
            suma=0
            for y in range (0,len(lista[x])-1):
                suma= suma + distancias[lista[x][y], lista[x][y+1]]
            totales.append(suma)
                
        dis_minima=min(totales)
        ubi_minima=totales.index(dis_minima)
        ruta_optima = lista[ubi_minima]
       
        
        #creacion de la cadena ruta con las especificacions 'A-B-C-D'
        texto_ruta=""
        for x in range (0,len(ruta_optima)):
            if x== len(ruta_optima)-1:
                texto_ruta=texto_ruta+ruta_optima[x]
            else:
                texto_ruta=texto_ruta+ruta_optima[x]+"-"
                
        salida={'ruta':texto_ruta,'distancia':dis_minima}
    
        return salida
    except Exception as e:
        print(e)
  

print (ruteo(ciudades1,ruta1))