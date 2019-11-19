import pygame
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

## Matriz de prueba
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


##Clase que controla la lógica de la matriz
class Controller:
    def __init__(self):
        self.name = "controler"
    ##Funcion para leer la matriz desde el archivo csv
    def init(self):
        
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
           #self.printMat(matriz)
           # print("-----------------section------------------")
            return matriz

    ##Funcion para guardar la información de la matriz en un archivo csv
    def saveToDisk(self,data):

         with open('matriz.csv', 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
            f.close()
  
    ##Funcion para la creacion de matrices cuadradas
    def makeMat(self,num):
        matriz = []
        for i in range(num):
            row = []
            for j in range(num):
                row += [0]
            matriz += [row]
        #self.printMat(matriz)
        return matriz

    ##Funcion para imprimir una matriz en consola
    def printMat(self,mat):
        for i in mat:
            print(i)


    ##Obtiene los valores de todas las casillas adyacentes
    ## a un punto de la matriz y los inserta en una lista
    def check(self,m,x,y):
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
    def getNum(self,num,llist):
        cont = 0
        for i in llist:
            if i == num:
                cont+=1
        return cont
    def verifyIN(self,entry):
        numeros = "1234567890"
        for i in entry:
            if i not in numeros:
                return False
        return True

    ##Funcion que comprueba si una condicion se cumple
    ##para intercambiar el valor de la casilla de la matriz
    def transform(self,m,lista,x,y):
        if m[x][y] == 0:
            if self.getNum(2,lista) >= 1:
                m[x][y] = 1
            elif  self.getNum(1,lista) >= 2 and self.getNum(3,lista) >= 1:
                m[x][y] = 2
            elif  self.getNum(1,lista)>= 3 or self.getNum(2,lista)>=3 or self.getNum(3,lista)>=3:
                m[x][y] = 3


        elif m[x][y] == 2:
            if self.getNum(1,lista) >= 6:
                m[x][y] = 0
        elif m[x][y] == 3:
            if self.getNum(1,lista) >= 6:
                m[x][y] = 0
        elif m[x][y] == 1:
            if self.getNum(2,lista) == 0 or self.getNum(3,lista) == 0:
                m[x][y] = 0

        return m


    def turn(self,matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                lista = self.check(matriz,i,j)
                matriz = self.transform(matriz,lista,i,j)
        return matriz






##Clase Mouse

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()


class Button(pygame.sprite.Sprite):
    def __init__(self,image1,image2,x=100,y=100):
        self.image_n = image1
        self.image_s = image2
        self.image_a = self.image_n
        self.rect = self.image_a.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,window,cursor):
        
        if cursor.colliderect(self.rect):
            self.image_a = self.image_s
        else:
            self.image_a = self.image_n

        window.blit(self.image_a , self.rect)


 
# Definimos algunos colores

##Variable global para controlar lógica de la matriz en cualquier lugar
global controllerA
controllerA = Controller()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = ( 0, 255, 255)
ROJO = (255, 0, 0)
SILVER = (192,192,192)
MAROON = (128,0,0)
AQUA = (0,255,255) 
YELLOW = (255,255,0)


 
# Establecemos el LARGO y ALTO de cada celda de la retícula.

LARGO  = 20
ALTO = 20
 
# Establecemos el margen entre las celdas.

MARGEN = 5


#Creando matriz logica

global grid2
grid2 = controllerA.init()


 
# Inicializamos pygame
pygame.init()


# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [800, 640]
window = pygame.display.set_mode(DIMENSION_VENTANA)

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

#Clase de texbox para entrada de texto
global playFlag
playFlag = False
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
        
            if self.active:
                if event.key == pygame.K_RETURN:
                    global timeVar
                    global playFlag
                    
                    if controllerA.verifyIN(self.text):
                        timeVar = int(self.text)
                        if playFlag == 1:
                            playFlag = not playFlag
                        
                
                    self.text = ''
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
 
# Establecemos el título de la pantalla.
pygame.display.set_caption("Life")
 
# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False
 
# Lo usamos para establecer cuán rápido de refresca la pantalla.
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000) 
entry1 = InputBox(650, 350, 10, 32)

# -------- Bucle Principal del Programa-----------

# Fuente del texto + label
myfont = pygame.font.SysFont("monospace", 15)
myfont2 = pygame.font.SysFont("monospace", 15)

#Color de las casillas
cont = 0
#variable de tiempo luego debe ser cambiada por el input
global timeVar
timeVar = 0

# Imagenes
save1 = pygame.image.load("images/save3.png")
save2 = pygame.image.load("images/save4.png")
play = pygame.image.load("images/play.png")
play2 = pygame.image.load("images/play2.png")
pause = pygame.image.load("images/pause.png")
pause2 = pygame.image.load("images/pause2.png")
nexxt = pygame.image.load("images/next.png")
nexxt2 = pygame.image.load("images/next2.png")
previous = pygame.image.load("images/previous.png")
previous2 = pygame.image.load("images/previous2.png")

reload =  pygame.image.load("images/reload.png")
#imagenesObjetos
lot = pygame.image.load("images/lote.png")
house = pygame.image.load("images/casa.png")
water = pygame.image.load("images/agua.png")
light = pygame.image.load("images/luz.png")

#Sonidos
#pygame.mixer.music.load("sounds/clock.mp3")


# Botones
buttonSave = Button(save1,save2,680,50)

buttonPrevious = Button(previous,previous2,630,150)
buttonPlay = Button(play,play2,680,150)
buttonNext = Button(nexxt,nexxt2,725,150)
buttonReload = Button(reload,reload,680,250)

cursor1 = Cursor()

savedFlag = False
timeSave = 1

while not hecho:
  
    

    for event in pygame.event.get():
        
        entry1.handle_event(event)
        
        if event.type == pygame.USEREVENT and playFlag:
            if timeVar > 0:
                timeVar -= 1
                controllerA.turn(grid2)
            elif timeVar <= 0:
                timeVar = 0
        if event.type == pygame.USEREVENT and savedFlag:
            if timeSave > 0:
                timeSave -= 1
            else:
                timeSave = 1
                savedFlag = False
          
        if event.type == pygame.QUIT: 
            hecho = True


            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            

            #SAVE BUTTON
            if cursor1.colliderect(buttonSave.rect):

                controllerA.printMat(grid2)
                controllerA.saveToDisk(grid2)
                savedFlag = True

            
            
            #PREVIOUS BUTTON
            elif cursor1.colliderect(buttonPrevious.rect):

                print("")
            #PLAY BUTTON
            elif cursor1.colliderect(buttonPlay.rect):

                playFlag = not playFlag
                if playFlag:
                    buttonPlay = Button(pause,pause2,680,150)
                    if timeVar != 0:
                        pygame.mixer.music.load("sounds/clock.mp3")
                        pygame.mixer.music.play(0)
                else:
                    buttonPlay = Button(play,play2,680,150)
                    pygame.mixer.music.stop()

            #NEXT BUTTON
            elif cursor1.colliderect(buttonNext.rect):

                 
                 grid2 = controllerA.turn(grid2)
            #RELOAD BUTTON     
            elif cursor1.colliderect(buttonReload.rect):

                newGrid = controllerA.makeMat(25)
                grid2 = newGrid
                #controllerA.saveToDisk(newGrid) Se podria guardar en disco
                #grid2 = controllerA.init()
        
             #El usuario presiona el ratón. Obtiene su posición.
            pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            
            # Establece esa ubicación a cero
            if columna < 25 and fila < 25:
                grid2[fila][columna] = cont
                cont+=1
            if cont > 3:
                cont = 0
            

    if timeVar <= 0:
        pygame.mixer.music.stop()
        buttonPlay = Button(play,play2,680,150)
        
    cursor1.update()
    #Animacion del texbox

    
    entry1.update()
    window.fill(NEGRO)
    entry1.draw(window)
    
    buttonSave.update(window,cursor1)
    buttonPlay.update(window,cursor1)
    buttonNext.update(window,cursor1)
    buttonPrevious.update(window,cursor1)
    buttonReload.update(window,cursor1)
    label = myfont.render("  Time: " +  str(timeVar), 1, (255,255,0))
    label2 = myfont2.render("¡ Saved !",1,(255,255,0))
    window.blit(label, (655, 20))
    if savedFlag:
        window.blit(label2,(670,110))

 
    # Establecemos el fondo de pantalla.
    
 
    # Dibujamos la retícula
    for fila in range(25):
        for columna in range(25):
            color = BLANCO
            #image = lot
            if grid2[fila][columna] == 0:
                color = SILVER
               # image = lot
            elif grid2[fila][columna] == 1:
                color = MAROON
                #image = house
            elif grid2[fila][columna] == 2:
                color = AQUA
                #image = water
            elif grid2[fila][columna] == 3:
                color = YELLOW
                #image = light
            pygame.draw.rect(window,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                             (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                             ALTO])

     
    # Limitamos a 60 fotogramas por segundo.
    clock.tick(60)
 
    # Actualizar pantalla
    pygame.display.flip()

pygame.quit()













