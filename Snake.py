# -*- coding: utf-8 -*-
"""
Programme Snake

"""

from tkinter import * # Importation de la bibliothèque  Tkinter 
from random import randint
from PIL import Image, ImageTk 
from subprocess import Popen

# On crée un environnement Tkinter
tk = Tk()
im_teteN = Image.open("img-snake/SH_UP.png")
teteN = ImageTk.PhotoImage(im_teteN)
im_teteS = Image.open("img-snake/SH_SOUTH.png")
teteS = ImageTk.PhotoImage(im_teteS)
im_teteE = Image.open("img-snake/SH_EST.png")
teteE = ImageTk.PhotoImage(im_teteE)
im_teteW = Image.open("img-snake/SH_WEST.png")
teteW = ImageTk.PhotoImage(im_teteW)
im_noeud1 = Image.open("img-snake/corps.png")
noeud1 = ImageTk.PhotoImage(im_noeud1)
# On crée les images des powerups

im_java_script = Image.open("logo-languages/javascript.png")
im_java_script = ImageTk.PhotoImage(im_java_script)

im_python = Image.open("logo-languages/python.png")
im_python = ImageTk.PhotoImage(im_python)

im_csharp = Image.open("logo-languages/c-sharp.png")
im_csharp = ImageTk.PhotoImage(im_csharp)

im_matlab = Image.open("logo-languages/matlab.png")
im_matlab = ImageTk.PhotoImage(im_matlab)


def finish():
    
    p = Popen("batch.bat", cwd=r"./")
    stdout, stderr = p.communicate()


def right(event):
    # Modification de la variable globale direction
    global direction
    direction = 'right'
    
def left(event):
    # Modification de la variable globale direction
    global direction
    direction = 'left'
    
def down(event):
    # Modification de la variable globale direction
    global direction
    direction = 'down'
    
def up(event):
    # Modification de la variable globale direction
    global direction
    direction = 'up'

# Calcule la nouvelle frame de jeu
def computeNextFrame(numFrame,coordonnee,objet):
    global direction
    global speed
    global score
    # Affiche le numérod de la frame
    #print(numFrame)
    numFrame = numFrame + 1
    
    # Effacer le canevas
    can.delete('all')
    
    # Propagation du déplacement des noeuds
    for i in range (len(coordonnee)-1,0,-1):
        coordonnee[i][0] = coordonnee[i-1][0]
        coordonnee[i][1] = coordonnee[i-1][1]
        
    # Mise à jour des coordonnées
    if direction == 'right':
        coordonnee[0][0] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteE)
        if coordonnee[0][0] > 480:
            coordonnee[0][0] = 0
            
    if direction == 'left':
        coordonnee[0][0] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteW)
        if coordonnee[0][0] < 0:
            coordonnee[0][0] = 480
            
    if direction == 'up':
        coordonnee[0][1] += -20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteN)
        if coordonnee[0][1] < 0:
            coordonnee[0][1] = 480
            
    if direction == 'down':
        coordonnee[0][1] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteS)
        if coordonnee[0][1] > 480:
            coordonnee[0][1] = 0
    
    for n in range(1,len(coordonnee)):
        if n%2 == 0:
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud1)
        else:
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud1)   
    # Dessine les objets
    for p in range(len(objet)):
        can.create_image(objet[0][0], objet[0][1], anchor = NW, image = im_csharp)
        can.create_image(objet1[0][0], objet1[0][1], anchor = NW, image = im_java_script)
        can.create_image(objet2[0][0], objet2[0][1], anchor = NW, image = im_matlab)
        can.create_image(objet2bis[0][0], objet2bis[0][1], anchor = NW, image = im_matlab)
        can.create_image(objet3[0][0], objet3[0][1], anchor = NW, image = im_python)
    #système de téléportage
    for p in range(len(objet2)):
        if coordonnee[0][0] == objet2[0][0] and coordonnee[p][1] == objet2[p][1]:
            coordonnee[0][0] = objet2bis[0][0]
            coordonnee[0][1] = objet2bis[0][1]
        elif coordonnee[0][0] == objet2bis[0][0] and coordonnee[p][1] == objet2bis[p][1]:
            coordonnee[0][0] = objet2[0][0]
            coordonnee[0][1] = objet2[0][1]
    game_finish = False      
    for j in range(len(objet)):
        Txt= can.create_text(85,25,text = "Score :"+" "+str(score), fill='red', font=("Arial",15,"bold"))
        if coordonnee[0][0] == objet[0][0] and coordonnee[p][1] == objet[p][1]:
            objet[0][0] = randint(1,24)* 20
            objet[0][1] = randint(1,24)* 20
            # On ajoute deux noeuds
            coordonnee.append([-20, -20])
            coordonnee.append([-40, -40])
            speed=100
            score = score + 20
        elif coordonnee[0][0] == objet1[0][0] and coordonnee[p][1] == objet1[p][1]:
            objet1[0][0] = randint(1,24)* 20
            objet1[0][1] = randint(1,24)* 20
            #On augmente la vitesse et onenlève un noeud 
            if speed == 20 :
                speed = 100
            else :
                speed = speed - 10
            coordonnee.pop()
            score = score - 10
            print(len(coordonnee))
            

        elif coordonnee[0][0] == objet2[0][0] and coordonnee[p][1] == objet2[p][1]:
            objet2bis[0][0] = randint(1,24)* 20
            objet2bis[0][1] = randint(1,24)* 20
            score = score + 1
            speed=100
            #on ajoute rien car téléporteur 1
            
        elif coordonnee[0][0] == objet2bis[0][0] and coordonnee[p][1] == objet2bis[p][1]:
            objet2[0][0] = randint(1,24)* 20
            objet2[0][1] = randint(1,24)* 20
            score = score + 1
            speed=100
            #on ajoute rien car téléporteur 2
        elif coordonnee[0][0] == objet3[0][0] and coordonnee[p][1] == objet3[p][1]:
            objet3[0][0] = randint(1,24)* 20
            objet3[0][1] = randint(1,24)* 20
            speed=100
            #On tue le serpend x)
            game_finish = True
            
            
    
    game_over = False
    # On test la position de la tête par rapport aux noeuds du serpent
    for n in range(1,len(coordonnee)): # L'indice 0 est exclu, c'est la tête
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee[0][1] == coordonnee [n][1] or len(coordonnee)== 2:
            game_over = True # La partie est finie
            Text = "GAME OVER"
    if game_finish == True :
        finish()
        game_over= True
        Text = "You died of poisoning"

    if game_over==True :
        #Fin de partie
        can.create_text(250,250,text = Text, fill='red', font=("Impact",35,"bold"))
    else :
        # Calcule une nouvelle frame toute les 100 ms
        tk.after(speed, lambda:computeNextFrame(numFrame,coordonnee, objet))

    
        
    

def switchButtonState():
    if b1['state'] == NORMAL:
        b1['state'] = DISABLED
    else:
        b1['state'] = NORMAL
def newGame():
    global game_over
    global b1, b3, tex1
    if game_over == True:
       game_over = False
    computeNextFrame(0,coordonnee, objet)
    b1.destroy()
    tex1.destroy()
    tex1 = Label(tk, text="Good Luck Have Fun",font=("Arial",10,"bold"), bg='white' , fg='black')
    tex1.pack(padx=0, pady=15)
    b1=Button(tk, text='Recommencer',font=("Arial",10), command=newGame, bg='white', fg='black', state= DISABLED)
    b1.pack()

    
    

if __name__ == "__main__":
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    tk.title("The Snake")
    can = Canvas(tk, width=500, height=500, bg='black')
    
    # On affiche le canevas
    can.pack()
    
    # Direction par défaut
    direction = 'up'
    speed = 100
    coordonnee = [[200, 200], [200, 220], [200, 240], [220, 240] ]
    objet = []
    objet1 = []
    objet2 = []
    objet3 = []
    objet2bis = []
    score = 0
    game_over = True
    # On Crée les 3 objets
    x = randint(1,24)
    y = randint(1,24)
    objet.append([x*20, y*20])
    x1 = randint(1,24)
    y1 = randint(1,24)
    objet1.append([x1*20, y1*20])
    x2 = randint(1,24)
    y2 = randint(1,24)
    objet2.append([x2*20, y2*20])
    x3 = randint(1,24)
    y3 = randint(1,24)
    objet3.append([x3*20, y3*20])
    xbis = randint(1,24)
    ybis = randint(1,24)
    objet2bis.append([xbis*20, ybis*20])

    
    # Construction de l'aspect graphique pour lancement du jeux
    b1=Button(tk, text='Lancer',font=("Arial",10), command=newGame, bg='white' , fg='black',)
    b1.pack()


    b2 = Button(tk, text='Quitter',font=("Arial",10), command=tk.destroy, bg='white' , fg='black')
    b2.pack()

    b3=Button(tk, text="Activer le Bouton Triche",font=("Arial",10),command = switchButtonState)
    b3.pack()

    tex1 = Label(tk, text="Cliquez sur 'Lancer' pour commencer le jeu.",font=("Arial",10,"bold"), bg='white' , fg='black')
    tex1.pack(padx=0, pady=15)
    
    # Appuyer sur la touche 'd' appellera la fonction right()
    tk.bind('<Right>', right) 
    tk.bind('<Left>', left) 
    tk.bind('<Down>', down) 
    tk.bind('<Up>', up)

    tk.bind('<d>', right) 
    tk.bind('<q>', left) 
    tk.bind('<s>', down) 
    tk.bind('<z>', up) 
    
    # lancement de la boucle principale qui écoute les évènements (claviers..)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme