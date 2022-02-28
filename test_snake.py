
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 09:54:11 2020

@author: imac
"""
# -*- coding: utf-8 -*-
"""
Programme Snake

"""

from tkinter import *# Importation de la bibliothèque  Tkinter
from tkinter import font as tkfont
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
im_noeud2 = Image.open("img-snake/corps.png")
noeud2 = ImageTk.PhotoImage(im_noeud2)
pomme = Image.open("img-snake/Pomme.png")
pomme = ImageTk.PhotoImage(pomme)



difficulte = int(input("Choisissez la difficulté du jeu :\n1.Facile\n2.Moyen\n3.Difficile\n"))



def right(event):
    # Modification de la variable globale direction
    global direction
    direction = 'right'
    #print(direction)

def left(event):
    # Modification de la variable globale direction
    global direction
    direction = 'left'
    #print(direction)

def down(event):
    # Modification de la variable globale direction
    global direction
    direction = 'down'
    #print(direction)

def up(event):
    # Modification de la variable globale direction
    global direction
    direction = 'up'
    #print(direction)

def computeNextFrame(numFrame,coordonnee, objet):
    global direction
    global game_over
    # Affiche le numéro de la frame
    #print(numFrame)
    numFrame = numFrame + 1

    can.delete("all")

    for i in range (len(coordonnee)-1,0,-1):
        coordonnee[i] = list(coordonnee[i-1])

        # Mise à jour des coordonnées
    if direction == 'right':
        coordonnee[0][0] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteE)
        if coordonnee[0][0] > 500:
            coordonnee[0][0] = 0
    if direction == 'left':
        coordonnee[0][0] -= 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteW)
        if coordonnee[0][0] < 0:
            coordonnee[0][0] = 480
    if direction == 'up':
        coordonnee[0][1] -= 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteN)
        if coordonnee[0][1] < 0:
            coordonnee[0][1] = 480
    if direction == 'down':
        coordonnee[0][1] += 20
        can.create_image(coordonnee[0][0], coordonnee[0][1], anchor = NW, image = teteS)
        if coordonnee[0][1] > 500:
            coordonnee[0][1] = 0

    for n in range(1,len(coordonnee)):
        if n%2 == 0:
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud1)
        else:
            can.create_image(coordonnee[n][0], coordonnee[n][1], anchor = NW, image = noeud2)


    can.create_image(objet[0], objet[1], anchor = NW, image = pomme)



    if coordonnee[0][0] == objet [0] and coordonnee[0][1] == objet [1]:
        # Déplacement de la pomme
        objet[0] = randint(1,24)* 20
        objet[1] = randint(1,24)* 20
        # Ajout d'un noeud au serpent (à la même place que le dernier noeud)
        coordonnee.append([-20, -20]) # Caché pour l'instant

    game_over = False
    # On test la position de la tête par rapport aux noeuds du serpent
    for n in range(1,len(coordonnee)): # L'indice 0 est exclu, c'est la tête
        if coordonnee[0][0] == coordonnee [n][0] and coordonnee[0][1] == coordonnee [n][1]:
            game_over = True # La partie est finie

    if game_over==True :
        #Fin de partie
        can.create_text(250,250,text = "GAME OVER", fill='red', font=("Helvetica",20,"bold"))
    else:
        # La partie n'est pas finie
        #calcul une nouvelle frame dans 100 ms
        if difficulte==1:
            tk.after(300, lambda: computeNextFrame(numFrame,coordonnee, objet))
        elif difficulte==2:
            tk.after(100, lambda: computeNextFrame(numFrame,coordonnee, objet))
        elif difficulte==3:
            tk.after(50, lambda: computeNextFrame(numFrame,coordonnee, objet))
def newGame():
    global game_over
    if game_over == True:
       game_over = False
    computeNextFrame(0,coordonnee, objet)
    
if __name__=="__main__":
    # On crée un environnement Tkinter
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

    coordonnee = [ [180, 200],
                   [200, 200],
                   [200, 240],
                   [220, 240] ]

    # Premier objet (la pomme)
    x = randint(1,24)
    y = randint(1,24)
    x2 = randint(1,24)
    y2 = randint(1,24)
    game_over = True
    objet = [x*20, y*20]
    b1 = Button(tk, text='Lancer',command=newGame, bg='white' , fg='black')
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(tk, text='Quitter', command=tk.destroy, bg='white' , fg='black')
    b2.pack(side=RIGHT, padx=5, pady =5)

    tex1 = Label(tk, text="Cliquez sur 'Lancer' pour commencer le jeu.", bg='white' , fg='black')
    tex1.pack(padx=0, pady=11)

    tk.bind('<d>', right)
    tk.bind('<q>', left)
    tk.bind('<s>', down)
    tk.bind('<z>', up)
    # lancement de la boucle principale qui écoute les évènements (claviers...)
    tk.mainloop() # Cet appel doit être la derni ere instruction du programme

