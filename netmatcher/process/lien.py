# -*- coding: utf-8 -*-

'''
Resultat de l'appariement : 
    lien entre des objets homologues de deux bases de données. 
Un lien a aussi une géométrie qui est sa représentation graphique.

'''

class Lien:
    """Class to represent a link"""

    def __init__(self):

        # Texte libre pour décrire le nom du procesus d'appariement.
        #nom = ""

        # Texte libre pour décrire le lien d'appariement.
        #commentaire = ""

        # Estimation de la qualité du lien d'appariement. Entre 0 et 1 en général
        #evaluation = -1.0

        # Liste d'indicateurs utilisés pendant les calculs d'appariement.
        #indicateurs = list()

        # Les objets d'une BD pointés par le lien.
        #objetsRef = list()

        # Les objets de l'autre BD pointés par le lien.
        #objetsComp = list()

        # Texte libre pour décrire le type d'appariement (ex. "Noeud-Noeud").
        #matchType = ""

        # Les Noeud1 pointés par le lien
        self.noeuds1 = list()

        # Les Noeud2 pointés par le lien
        self.noeuds2 = list()

        # Les Arc2 pointés par le lien
        self.arcs2 = list()

        # Les Arc1 pointés par le lien
        self.arcs1 = list()




    def getNoeuds1(self):
        return self.noeuds1
    def setNoeuds1(self, nodes):
        self.noeuds1 = nodes
    def addNoeuds1(self, node):
        self.noeuds1.append(node)


    def getNoeuds2(self):
        ''' @return Les Noeud2 pointés par le lien '''
        return self.noeuds2
    def setNoeuds2(self, nodes):
        ''' @param noeuds Les Noeud2 pointés par le lien '''
        self.noeuds2 = nodes
    def addNoeuds2(self, node):
        ''' @param noeud Noeud2 pointé par le lien '''
        self.noeuds2.append(node)


    def getArcs2(self):
        ''' @return Les Arc2 pointés par le lien '''
        return self.arcs2
    def setArcs2(self, arcs):
        ''' @param arcs Les Arc2 pointés par le lien '''
        self.arcs2 = arcs
    def addArcs2(self, arc):
        ''' @param arc Arc2 pointé par le lien '''
        self.arcs2.append(arc)


    def getArcs1(self):
        ''' @return Les Arc1 pointés par le lien '''
        return self.arcs1
    def setArcs1(self, arcs):
        ''' @param arcs Les Arc1 pointés par le lien '''
        self.arcs1 = arcs
    def addArcs1(self, arc):
        ''' @param arc Arc1 pointé par le lien '''
        self.arcs1.append(arc)



