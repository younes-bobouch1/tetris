import pygame
import random

pygame.init()

#Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)

#Dimension screen
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600

#Dimension bloc
LARGEUR_BLOC = 25
HAUTEUR_BLOC = 25

#Grille
GRILLE_JEU = [[NOIR for j in range(LARGEUR_ECRAN // LARGEUR_BLOC)] for i in range(HAUTEUR_ECRAN // HAUTEUR_BLOC)]

#Formes
FORMES_PIECES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6],
     [6, 6]],

    [[7, 7, 7, 7]]
]

#Couleurs pièces
COULEURS_PIECES = [
    BLEU,
    VERT,
    ROUGE,
    JAUNE,
    BLEU,
    VERT,
    ROUGE
]

class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.forme = random.choice(FORMES_PIECES)
        self.couleur = random.choice(COULEURS_PIECES)

    def tourner(self):
        self.forme = [[self.forme[j][i] for j in range(len(self.forme))] for i in range(len(self.forme[0]))]

    def deplacer_gauche(self):
        self.x -= 1

    def deplacer_droite(self):
        self.x += 1

    def deplacer_bas(self):
        self.y += 1

    def dessiner(self, grille_jeu):
        for i in range(len(self.forme)):
            for j in range(len(self.forme[0])):
                if self.forme[i][j] != 0:
                    pygame.draw.rect(grille_jeu, self.couleur,
                                     [(self.x + j) * LARGEUR_BLOC, (self.y + i) * HAUTEUR_BLOC, LARGEUR_BLOC,
                                      HAUTEUR_BLOC])


#F principal
def main():
    #Screen
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    pygame.display.set_caption("Jeu Tetris")

    #Initiasion var
    piece_actuelle = Piece(3, 0)
    jeu_actif = True
    clock = pygame.time.Clock()

    while jeu_actif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu_actif = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece_actuelle.deplacer_gauche()
                elif event.key == pygame.K_RIGHT:
                    piece_actuelle.deplacer_droite()
                elif event.key == pygame.K_DOWN:
                    piece_actuelle.deplacer_bas()
                elif event.key == pygame.K_UP:
                    piece_actuelle.tourner()

        ecran.fill(BLANC)

        for i in range(len(GRILLE_JEU)):
            for j in range(len(GRILLE_JEU[0])):
                pygame.draw.rect(ecran, GRILLE_JEU[i][j],
                                 [j * LARGEUR_BLOC, i * HAUTEUR_BLOC, LARGEUR_BLOC, HAUTEUR_BLOC], 1)

        piece_actuelle.dessiner(ecran)

        pygame.display.flip()

        #Vitesse chute
        if piece_actuelle.y + len(piece_actuelle.forme) == HAUTEUR_ECRAN // HAUTEUR_BLOC or \
                any(GRILLE_JEU[piece_actuelle.y + i + 1][piece_actuelle.x + j] != NOIR for i in
                    range(len(piece_actuelle.forme)) for j in range(len(piece_actuelle.forme[0]))):
            for i in range(len(piece_actuelle.forme)):
                for j in range(len(piece_actuelle.forme[0])):
                    if piece_actuelle.forme[i][j] != 0:
                        GRILLE_JEU[piece_actuelle.y + i][piece_actuelle.x + j] = piece_actuelle.couleur
            piece_actuelle = Piece(3, 0)

        else:
            piece_actuelle.deplacer_bas()

        #Vitesse chute
        clock.tick(10)

    pygame.quit()

if __name__ == '__main__':
    main()



