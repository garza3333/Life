#import pygame
import csv

##REGLAS

## 0 + 2 = 1
## 0 + +1+1+1 = 3
## 2 + 1+1+1+1+1+1 (preguntar que tipo de edificio) = 0
## 1 -2-3 = 0
## 0 +1+1+3 = 2

#SIMBOLOGIA

## 0 lote baldio
## 1 casa
## 2 Agua
## 3 Luz
matriz = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #0
                  [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #1
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #2
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #3
                  [0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],   #4
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #5
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #6
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #7
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #8
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #9
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #10
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #11
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #12
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #13
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #14
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #15
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #16
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #17
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #18
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #19
                  [0,0,0,0,0,1,3,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],   #20
                  [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #21
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #22
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #23
                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   #24
          ]


##Funcion para leer la matriz desde el archivo csv
def init():
    
    matriz = []
    with open('matriz.csv') as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if len(row) != 0:
                matriz += [row]
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                matriz[i][j] = int(matriz[i][j])
        printMat(matriz)
        print("-----------------section------------------")

##Funcion para guardar la información de la matriz en un archivo csv
def saveToDisk(data):

     with open('matriz.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
        f.close()
  
##Funcion para la creacion de matrices cuadradas
def makeMat(num):
    matriz = []
    for i in range(num):
        row = []
        for j in range(num):
            row += [0]
        matriz += [row]
    printMat(matriz)

##Funcion para imprimir una matriz en consola
def printMat(mat):
    for i in mat:
        print(i)


##Obtiene los valores de todas las casillas adyacentes
## a un punto de la matriz y los inserta en una lista
def check(m,x,y):
    lista = []
    if not x-1 <0:
        lista += [m[x-1][y]]
    if not x+1 > len(m)-1:
        lista += [m[x+1][y]]
    if not y-1 < 0 :
        lista += [m[x][y-1]]
    if not y+1 > len(m)-1:
        lista += [m[x][y+1]]
    if not x-1 < 0 and not y-1 < 0 :
        lista += [m[x-1][y-1]]
    if not x-1 < 0 and not y+1 > len(m)-1:
        lista += [m[x-1][y+1]]
    if not x+1 > len(m)-1 and not y-1 <0:
        lista += [m[x+1][y-1]]
    if not x+1 > len(m)-1 and not y+1 > len(m)-1:
        lista += [m[x+1][y+1]]
    return lista
    

##Obtiene la cantidad de veces que un numero
##se repite en una lista
def getNum(num,llist):
    cont = 0
    for i in llist:
        if i == num:
            cont+=1
    return cont

##Funcion que comprueba si una condicion se cumple
##para intercambiar el valor de la casilla de la matriz
def transform(m,lista,x,y):
    if m[x][y] == 0:
        if getNum(2,lista) >= 1:
            m[x][y] = 1
        elif  getNum(1,lista)>= 3 or getNum(2,lista)>=3 or getNum(3,lista)>=3:
            m[x][y] = 3
        elif  getNum(1,lista) >= 2 and getNum(3,lista) >= 1:
            m[x][y] = 3
    #if m[x][y] == 0:
       # if getNum(1,lista)>= 3 or getNum(2,lista)>=3 or getNum(3,lista)>=3:
          #  m[x][y] = 3

    elif m[x][y] == 2:
        if getNum(1,lista) >= 6:
            m[x][y] = 0
    elif m[x][y] == 1:
        if getNum(2,lista) == 0 or getNum(3,lista) == 0:
            m[x][y] = 0
    #if m[x][y] == 0:
      #  if getNum(1,lista) >= 2 and getNum(3,lista) >= 1:
        #    m[x][y] = 3
    return m


def turn(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista = check(matriz,i,j)
            matriz = transform(matriz,lista,i,j)
    return matriz




#print(check(matriz,0,0))
#print(getNum(1,check(matriz,0,0)))
#lista = [0,1,2,3,1,2,0,1,2,0,0,1,2,3]
#print(getNum(1,lista))
#turn(matriz)
saveToDisk(turn(matriz))
init()
saveToDisk(turn(matriz))
init()


##Ejemplo movimiento de un cubo


#pygame.init()
#win = pygame.display.set_mode(500,500)
#x = 50
#y = x
#width = 40
#height = 60
#vel = 5
#run = True
#while run:
#    pygame.time.delay(100)
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            run = False      
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_LEFT]:
#        x -= vel
#    if keys[pygame.K_RIGHT]:
#        x += vel
#    if keys[pygame.K_UP]:
#        y -= vel
#    if keys[pygame.K_DOWN]:
#        y += vel

#    win.fill((0,0,0))
#    pygame.draw.rect(win (255,0,0) , (x,y,width,height))
#    pygame.display.update()

#pygame.quit()



 
# Definimos algunos colores

#NEGRO = (0, 0, 0)
#BLANCO = (255, 255, 255)
#AZUL = ( 0, 255, 255)
#ROJO = (255, 0, 0)
 
# Establecemos el LARGO y ALTO de cada celda de la retícula.

#LARGO  = 20
#ALTO = 20
 
# Establecemos el margen entre las celdas.

#MARGEN = 5
 
# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
#grid = []
#for fila in range(10):

    # Añadimos un array vacío que contendrá cada celda 
    # en esta fila
    
    #grid.append([])
    #for columna in range(10):
        #grid[fila].append(0) # Añade una celda

#grid2 = makeMat(25)

 
# Establecemos la fila 1, celda 5 a uno. (Recuerda, los números de las filas y
# columnas empiezan en cero.)
#grid2[1][5] = 1
 
# Inicializamos pygame
#pygame.init()
  
# Establecemos el LARGO y ALTO de la pantalla
#DIMENSION_VENTANA = [500, 500]
#pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
 
# Establecemos el título de la pantalla.
#pygame.display.set_caption("Life")
 
# Iteramos hasta que el usuario pulse el botón de salir.
#hecho = False
 
# Lo usamos para establecer cuán rápido de refresca la pantalla.
#reloj = pygame.time.Clock()
 
# -------- Bucle Principal del Programa-----------
#while not hecho:
    #for evento in pygame.event.get(): 
        #if evento.type == pygame.QUIT: 
            #hecho = True
        #elif evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
            #pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            #columna = pos[0] // (LARGO + MARGEN)
            #fila = pos[1] // (ALTO + MARGEN)
            # Establece esa ubicación a cero
            #grid2[fila][columna] = 1
            #print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
 
    # Establecemos el fondo de pantalla.
    #pantalla.fill(NEGRO)
 
    # Dibujamos la retícula
    #for fila in range(10):
       # for columna in range(10):
            #color = BLANCO
            #if grid2[fila][columna] == 1:
                #color = AZUL
            #pygame.draw.rect(pantalla,
                             #color,
                            # [(MARGEN+LARGO) * columna + MARGEN,
                              #(MARGEN+ALTO) * fila + MARGEN,
                             # LARGO,
                              #ALTO])
     
    # Limitamos a 60 fotogramas por segundo.
    #reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    #pygame.display.flip()
     
# Pórtate bien con el IDLE.
#pygame.quit()


