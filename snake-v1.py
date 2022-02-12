# -*- coding: utf-8 -*-
"""
Programme Snake

"""
from tkinter import *
from winreg import DisableReflectionKey # Importation de la bibliothèque  Tkinter 

# On crée un environnement Tkinter
tk = Tk()
   
# On crée un canevas dans l'environnement Tkinter d'une taille de 500x500
# Ce constructeur prend comme premier paramètre l'objet dans lequel il sera
# intégré (ici l'environnement Tkinter)
# Les trois autres paramètres permettent de spécifier la taille et la couleur
# de fond du canevas
def computeNextFrame(numFrame, coordonnee):
    """ print(numFrame) """
    numFrame= numFrame + 1
    can.delete('all')
    if direction == 'left':
        coordonnee[0] = coordonnee[0] - 20
    elif direction == 'right':
        coordonnee[0] = coordonnee[0] + 20
    elif direction == 'up':
        coordonnee[1] = coordonnee[1] - 20
    elif direction == 'down':
        coordonnee[1] = coordonnee[1] + 20
    can.create_rectangle(coordonnee[0], coordonnee[1]+20, coordonnee[0]+20, coordonnee[1], fill='red', outline='yellow')
    can.create_rectangle(coordonnee[0]+20, coordonnee[1]+20, coordonnee[0]+40, coordonnee[1], fill='green', outline='yellow')
    can.create_rectangle(coordonnee[0]+40, coordonnee[1]+20, coordonnee[0]+60, coordonnee[1], fill='white', outline='yellow')    
    tk.after(100, lambda: computeNextFrame(numFrame, coordonnee))

def right(event):
    global direction
    direction = 'right'
    print(direction)
def left(event):
    global direction
    direction = 'left'
    print(direction)
def up(event):
    global direction
    direction = 'up'
    print(direction)
def down(event):
    global direction
    direction = 'down'
    print(direction)

 

if __name__ == '__main__':
    can = Canvas(tk, width=500, height=500, bg='black')
    can.pack()
    direction='up'
    computeNextFrame(0, [400,400])
    tk.bind('<Right>', right)
    tk.bind('<Left>', left)
    tk.bind('<Up>', up)
    tk.bind('<Down>', down)
    # On affiche le canevas
    tk.mainloop() # Cet appel doit être la derniere instruction du programme




""" can.create_rectangle(480, 0, 500,  20, fill='green', outline='yellow')
can.create_oval(100, 200, 120, 120, fill='blue', outline='red') """

""" computeNextFrame(0, coordonnee=400)
 """

# lancement de la boucle principale qui écoute les évènements (claviers...)





