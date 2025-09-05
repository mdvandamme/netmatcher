# -*- coding: utf-8 -*-

'''

'''

class EnsembleDeLiens:
    """Class to represent a set of links"""

    def __init__(self, nom):
        # Nom du l'ensemble des liens d'appariement.
        #     ex:"Appariement des routes par la méthode XX"
        self.nom = nom

        self.liens = list()



    def addLien(self, lien):
        self.liens.append(lien)


    def __len__(self):
        return len(self.liens)