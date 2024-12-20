import doctest

def generer_grille_vide(nb_col, nb_lig):
    """
    la fonction generer_grille_vide a pour paramètres:
        - nb_col est un entier positif qui est le nombre de colonnes de la grille
        - nb_lig est un entier positif qui est le nombre de lignes de la grille
    et elle retourne
        - un tableau de tableaux d'entiers de valeur 0 qui représente une grille vide

    >>> generer_grille_vide(7,5)
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    >>> generer_grille_vide(3,2)
    [[0, 0, 0], [0, 0, 0]]

    >>> generer_grille_vide(4,5)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """

    grille_vide = []
    ligne_vide = []
    for c in range(0, nb_col):
        ligne_vide.append(0)
    for ligne in range(0, nb_lig):
        grille_vide.append(list(ligne_vide))
    return grille_vide




def affiche_grille(grille):
    """
     la fonction affiche_grille a pour paramètres:
        - grille de type tableay de tableaux d'entiers de valeur 0, 1 ou 2
     elle affiche la représentation d'une grille à l"écran:
         - 1 est représenté par X
         - 2 est représenté par O
         - O est représenté par un espace

    >>> affiche_grille([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],\
        [0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]])
    +-+-+-+-+-+-+-+
    | | | | | | | |
    +-+-+-+-+-+-+-+
    | |X|O|X| | | |
    +-+-+-+-+-+-+-+
    | |X|O|O| | | |
    +-+-+-+-+-+-+-+
    | |O|X|X| |X|O|
    +-+-+-+-+-+-+-+
    |O|X|O|O|X|O|O|
    +-+-+-+-+-+-+-+
    |X|X|O|X|O|X|X|
    +-+-+-+-+-+-+-+
     0 1 2 3 4 5 6

    >>> affiche_grille([[2,1,2,2,1,2],[0,2,1,1,0,1],\
        [0,1,2,2,0,0],[0,1,2,1,0,0]])
    +-+-+-+-+-+-+
    | |X|O|X| | |
    +-+-+-+-+-+-+
    | |X|O|O| | |
    +-+-+-+-+-+-+
    | |O|X|X| |X|
    +-+-+-+-+-+-+
    |O|X|O|O|X|O|
    +-+-+-+-+-+-+
     0 1 2 3 4 5

    >>> affiche_grille([[2,1,2,2],\
        [0,1,2,2],[0,1,2,1]])
    +-+-+-+-+
    | |X|O|X|
    +-+-+-+-+
    | |X|O|O|
    +-+-+-+-+
    |O|X|O|O|
    +-+-+-+-+
     0 1 2 3
    """

    grille.reverse()
    print('+' + '-+' * len(grille[0]))
    for ligne in range(len(grille)):
        print('|', end='')
        for c in range(len(grille[ligne])):
            if grille[ligne][c] == 0:
                print(" ", end='')
            elif grille[ligne][c] == 1:
                print("X", end='')
            else:
                print("O", end='')
            print('|', end='')
        print("")
        print('+' + '-+' * len(grille[0]))
    for c in range(len(grille[0])):
        print(" " + str(c), end="")
    print()
    grille.reverse()



def peut_jouer(grille, colonne):
    """
    la fonction peut_jouer a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
        - colonne de type entier qui correspond à la colonne jouée
    elle retourne un booléen de valeur:
        - True si il y a une case de valeur 0 dans la colonne de la grille
        - False si numéro de colonne non valide ou si il n'y a pas de case de valeur 0 dans la colonne de la grille

    >>> peut_jouer([[2, 1, 2], [0, 1, 2], [0, 1, 2]], 2)
    False

    >>> peut_jouer([[2,1,2,2,1,2],[0,2,1,1,0,1], [0,1,2,0,0,1],[0,1,2,0,1,0]],6)
    False

    >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[2,2,1,1,0,1,2],[1,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0]],0)
    True
    """

    if colonne < 0 or colonne > len(grille[0]) - 1:
        return False
    elif grille[len(grille)-1][colonne] == 0:
        return True
    else:
        return False
    pass

def joue(grille, colonne, joueur):
    """
    la fonction joue a pour paramètres:
        - grille de type tableay de tableau d'entiers de valeur 0, 1 ou 2
        - colonne de type entier qui correspond à la colonne jouée
    -    joueur de type entier qui correspond au numéro du joueur
    elle modifie:
        - le paramètre grille à la première ligne avec valeur 0 de la colonne jouée par la valeur du numéro du joueur

    >>> joue([[2, 1, 2], [0, 1, 2], [0, 1, 0]], 2, 1)

    >>> joue([[2,1,2,2,1,2],[0,2,1,1,0,1], [0,1,2,0,0,1],[0,1,2,0,1,0]],3,2)

    >>> joue([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[2,2,1,1,0,1,2],[1,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0]],0,1)
    """

    for ligne in range(len(grille)):
        if grille[ligne][colonne] == 0:
            grille[ligne][colonne] = joueur
            return



def a_gagne_vert(grille, joueur):
    """
    la fonction a_gagne_vert a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
        - joueur de type entier qui correspond au numéro du joueur
    elle retourne un booléen de valeur:
        - True si il y a 4 cases successives avec la valeur du numéro du joueur sur une des colonnes de la grille
        - False sinon

    >>> a_gagne_vert([[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]], 1)
    True

    >>> a_gagne_vert([[1, 1, 1, 1, 1, 1, 1], [1, 0, 2, 0, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], 1)
    False

    >>> a_gagne_vert([[1, 2, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2], [1, 2, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1]], 2)
    True
    """
    for c in range(len(grille[0])):
        nb_jetons=0
        for ligne in range(len(grille)):
            if grille[ligne][c] == joueur:
                nb_jetons = nb_jetons + 1
                if nb_jetons == 4:
                    return True
            else:
                nb_jetons = 0
    return False




def a_gagne_hor(grille, joueur):
    """
    la fonction a_gagne_hor a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
        - joueur de type entier qui correspond au numéro du joueur
    elle retourne un booléen de valeur:
        - True si il y a 4 cases successives avec la valeur du numéro de joueur sur une des lignes de la grille
        - False sinon

    >>> a_gagne_hor([[1, 1, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
    True

    >>> a_gagne_hor([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
    False

    >>> a_gagne_hor([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 2, 2, 1], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 2)
    True
    """

    for ligne in range(len(grille)):
        nb_jetons = 0
        for c in range(len(grille[ligne])):
            if grille[ligne][c] == joueur:
                nb_jetons = nb_jetons + 1
                if nb_jetons == 4:
                    return True
            else:
                nb_jetons = 0
    return False




def a_gagne_diag1(grille, joueur):
    """
     la fonction a_gagne_diag1 a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
        - joueur de type entier qui correspond au numéro du joueur
     elle retourne un booléen de valeur:
         - True si il y a 4 cases successives avec la valeur du numéro de joueur sur une diagonale montante
         - False sinon

     >>> a_gagne_diag1([[1, 1, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 1, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
     True

     >>> a_gagne_diag1([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
     False

     >>> a_gagne_diag1([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 2, 2, 1], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 2)
     False
     """

    nb_colonnes = len(grille[0])
    nb_lignes = len(grille)
    for c_principale in range(nb_colonnes-3):
        nb_jetons = 0
        ligne = 0
        c_diagonale = c_principale
        while ligne < nb_lignes and c_diagonale < nb_colonnes:
            if grille[ligne][c_diagonale] == joueur:
                nb_jetons = nb_jetons + 1
                if nb_jetons == 4:
                    return True
            else:
                nb_jetons = 0
            ligne = ligne + 1
            c_diagonale = c_diagonale + 1

    for l_principale in range(nb_lignes - 3):
        nb_jetons = 0
        colonne = 0
        l_diagonale = l_principale
        while l_diagonale < nb_lignes and colonne < nb_colonnes:
            if grille[l_diagonale][colonne] == joueur:
                nb_jetons = nb_jetons + 1
                if nb_jetons == 4:
                    return True
            else:
                nb_jetons = 0
            colonne = colonne + 1
            l_diagonale = l_diagonale + 1
    return False



def a_gagne_diag2(grille, joueur):
    """
    la fonction a_gagne_diag2 a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
        - joueur de type entier qui correspond au numéro du joueur
     elle retourne un booléen de valeur:
         - True si il y a 4 cases successives avec la valeur du numéro de joueur sur une diagonale descendante
         - False sinon

     >>> a_gagne_diag2([[1, 1, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
     False

     >>> a_gagne_diag2([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 1, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
     True

     >>> a_gagne_diag2([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 2, 2, 1], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 2)
     False
     """

    nb_colonnes = len(grille[0])
    nb_lignes = len(grille)
    for c_principale in range(nb_colonnes-3):
        nb_jetons = 0
        ligne = nb_lignes
        c_diagonale = c_principale
        while ligne > 0 and c_diagonale < nb_colonnes:
            if grille[ligne-1][c_diagonale] == joueur:
                nb_jetons = nb_jetons + 1
                if nb_jetons == 4:
                    return True
            else:
                nb_jetons = 0
            ligne = ligne - 1
            c_diagonale = c_diagonale + 1

    for l_principale in range(3, nb_lignes-1):
        nb_jetons = 0
        colonne = 0
        l_diagonale = l_principale
        while l_diagonale > 0 and colonne < nb_colonnes:
            if grille[l_diagonale][colonne-1] == joueur:
                nb_jetons = nb_jetons + 1
                if nb_jetons == 4:
                    return True
            else:
                nb_jetons = 0
            colonne = colonne + 1
            l_diagonale = l_diagonale - 1
    return False

def a_gagne(grille, joueur):
    """
    la fonction a_gagne a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
        - joueur de type entier qui correspond au numéro du joueur
    elle retourne un booléen de valeur:
        - True si une des fonctions a_gagne_vert, a_gagne_hor, a_gagne_diag1 ou a_gagne_diag2 retourne True pour ce numéro de joueur
        - False sinon

      >>> a_gagne([[1, 1, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
      True

      >>> a_gagne([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 1)
      False

      >>> a_gagne([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 1, 2, 2, 1], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0],[0, 1, 2, 1, 0, 0, 0], [1, 1, 1, 0, 1, 0, 1]], 2)
      False
      """

    if a_gagne_vert(grille, joueur) or a_gagne_hor(grille, joueur) or a_gagne_diag1(grille, joueur) or a_gagne_diag2(grille, joueur):
        return True
    else:
        return False



def grille_pleine(grille):
    """
    la fonction grille_pleine a pour paramètres:
        - grille de type tableau de tableaux d'entiers de valeur 0, 1 ou 2
    elle retourne un booléen de valeur:
        - False si une case de la grille a une valeur 0
        - True sinon

     >>> grille_pleine([[2, 1, 2], [0, 1, 2], [0, 1, 0]])
     False

     >>> grille_pleine([[1, 2, 1, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [1, 2, 1, 1, 2, 1, 1], [1, 2, 1, 1, 2, 1, 1],[1, 2, 1, 1, 2, 1, 1],[1, 2, 1, 1, 2, 1, 1]])
     True

     >>> grille_pleine([[1, 2, 1, 2, 2, 1, 2], [2, 1, 1, 1, 2, 2, 1]])
     True
     """

    for ligne in range(len(grille)):
        for c in range(len(grille[ligne])):
            if grille[ligne][c] == 0:
                return False
    return True



def boucle_principale():
    grille = generer_grille_vide(7, 6)
    joueur_courant = 1
    while not grille_pleine(grille):
        affiche_grille(grille)
        print("joueur ", joueur_courant, " à toi de jouer:", end='')
        numero_colonne = int(input())
        while not peut_jouer(grille, numero_colonne):
            print("erreur de saisie du numéro de colonne")
            affiche_grille(grille)
            print("joueur ", joueur_courant, " à toi de jouer:", end='')
            numero_colonne = int(input())
        joue(grille, numero_colonne, joueur_courant)
        if a_gagne(grille, joueur_courant):
            affiche_grille(grille)
            print("victoire de joueur ", joueur_courant)
            return
        if joueur_courant == 1:
            joueur_courant = 2
        else:
            joueur_courant = 1
    print("match nul")

if __name__ == "__main__":
    doctest.testmod()
    boucle_principale()
