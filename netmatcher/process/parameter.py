# -*- coding: utf-8 -*-


class ParameterNM:

    def __init__(self):
        # =====================================================================
        # PARAMETRES SPECIFIANT QUELLE DONNEES SONT TRAITEES

        # Liste des classes d'arcs de la BD 1 (la moins détaillée)
        #    concernés par l'appariement
        self.populationsArcs1 = None

        # Liste des classes de noeuds de la BD 1 (la moins détaillée)
        #    concernés par l'appariement
        self.populationsNoeuds1 = None

        # Liste des classes d'arcs de la BD 2 (la plus détaillée)
        #    concernés par l'appariement
        self.populationsArcs2 = None

        # Liste des classes de noeuds de la BD 2 (la plus détaillée)
        #    concernés par l'appariement
        self.populationsNoeuds2 = None

        # Prise en compte de l'orientation des arcs sur le terrain
        #    (sens de circulation).
        #    Si true : on suppose tous les arcs en double sens.
        #    Si false: on suppose tous les arcs en sens unique, celui défini par la géométrie.
        # NB: ne pas confondre cette orientation 'géographique réelle', avec
        #    l'orientation de la géométrie.

        self.populationsArcsAvecOrientationDouble1 = True
        self.populationsArcsAvecOrientationDouble2 = True
        self.attributOrientation1 = "orientation"
        self.attributOrientation2 = "orientation"
        # public Map<Object, Integer> orientationMap1 = null;
        # public Map<Object, Integer> orientationMap2 = null;



        # ///////////////////////////////////////////////////////////////////////////////
        # /////////////// TAILLES DE RECHERCHE ///////////////////////
        # /////////////// Ecarts de distance autorisés ///////////////////////
        # /////////////// CE SONT LES PARAMETRES PRINCIPAUX ///////////////////////
        # ///////////////////////////////////////////////////////////////////////////////

        # Distance maximale autorisée entre deux noeuds appariés.
        self.distanceNoeudsMax = 150

        # Distance maximum autorisée entre les arcs des deux réseaux. La distance est
        # définie au sens de la "demi-distance de Hausdorf" des arcs du réseau 2 vers
        # les arcs du réseau 1.
        self.distanceArcsMax = 100

        # Distance minimum sous laquelle l'écart de distance pour divers arcs du
        # réseaux 2 (distance vers les arcs du réseau 1) n'a plus aucun sens. Cette
        # distance est typiquement de l'ordre de la précision géométrique du réseau
        # le moins précis.
        self.distanceArcsMin = 30



    def setPopulationsArcs1(self, populationsArcs1):
        self.populationsArcs1 = populationsArcs1
    def getPopulationsArcs1(self):
        return self.populationsArcs1

    def setPopulationsArcs2(self, populationsArcs2):
        self.populationsArcs2 = populationsArcs2
    def getPopulationsArcs2(self):
        return self.populationsArcs2



    def getDistanceNoeudsMax(self):
        return self.distanceNoeudsMax
    def getDistanceArcsMax(self):
        return self.distanceArcsMax
    def getDistanceArcsMin(self):
        return self.distanceArcsMin;







