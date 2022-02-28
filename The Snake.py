# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import * # Importation de la bibliothèque  Tkinter 
from random import randint
from PIL import Image, ImageTk 

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
pomme = Image.open("img-snake/Pomme.png")
pomme = ImageTk.PhotoImage(pomme)

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
    global aspect
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
        can.create_image(objet[0][0], objet[0][1], anchor = NW, image = pomme)

    for j in range(len(objet)):
        if coordonnee[0][0] == objet [0][0] and coordonnee[p][1] == objet [p][1]:
            if aspect == 0:
                print("rien à foutre")
                objet[0][0] = randint(1,24)* 20
                objet[0][1] = randint(1,24)* 20
                aspect = randint(0,3)
                objet[0][2] = aspect
            elif aspect == 1:
                print("Aie")
                objet[0][0] = randint(1,24)* 20
                objet[0][1] = randint(1,24)* 20
                aspect = randint(0,3)
                objet[0][2] = aspect
            elif aspect == 2:
                print("Aie un peu plus")
                objet[0][0] = randint(1,24)* 20
                objet[0][1] = randint(1,24)* 20
                aspect = randint(0,3)
                objet[0][2] = aspect
            elif aspect == 3:
                print("Merde, je suis mort")
                objet[0][0] = randint(1,24)* 20
                objet[0][1] = randint(1,24)* 20
                aspect = randint(0,3)
                objet[0][2] = aspect
            # Déplacement de la pomme

            # Ajout d'un noeud au serpent (à la même place que le dernier noeud)
            coordonnee.append([-20, -20]) # Caché pour l'instant

 
    # Calcule une nouvelle frame toute les 100 ms
    tk.after(100, lambda:computeNextFrame(numFrame,coordonnee, objet))

def newGame():
    global game_over
    global b1
    if game_over == True:
       game_over = False
    computeNextFrame(0,coordonnee, objet)
    b1.destroy()
    b1=Button(tk, text='Recommencer', command=newGame, bg='white' , fg='black', state='disabled')
    b1.pack()
    
    

if __name__ == "__main__":
    # On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
    # Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
    # intégré (ici l'environnement Tkinter)
    # Les trois autres paramètres permettent de spécifier la taille et la couleur
    # de fond du canevas
    can = Canvas(tk, width=500, height=500, bg='black')
    
    # On affiche le canevas
    can.pack()
    
    # Direction par défaut
    direction = 'up'
    coordonnee = [[200, 200], [200, 220], [200, 240], [220, 240] ]
    objet = []
    game_over = True
    # Premier objet (la pomme)
    x = randint(1,24)
    y = randint(1,24)
    aspect = randint(0,3)
    objet.append([x*20, y*20, aspect])
    
    
    # Construction de la première étape de simulation
    b1=Button(tk, text='Lancer', command=newGame, bg='white' , fg='black')
    b1.pack()

    
    b2 = Button(tk, text='Quitter', command=tk.destroy, bg='white' , fg='black')
    b2.pack()

    tex1 = Label(tk, text="Cliquez sur 'Lancer' pour commencer le jeu.", bg='white' , fg='black')
    tex1.pack(padx=0, pady=11)
    
    # Appuyer sur la touche 'd' appellera la fonction right()
    tk.bind('<Right>', right) 
    tk.bind('<Left>', left) 
    tk.bind('<Down>', down) 
    tk.bind('<Up>', up) 
    
    # lancement de la boucle principale qui écoute les évènements (claviers..)
    tk.mainloop() # Cet appel doit être la derniere instruction du programme