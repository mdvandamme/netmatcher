# -*- coding: utf-8 -*-

from netmatcher.io import readArc
from netmatcher.process import ParameterNM
from netmatcher.netmatcher import appariementDeJeuxGeo
from netmatcher.netmatcher import N1_CORRESPOND, N2_CORRESPOND


# =============================================================================
#   Import des deux réseaux

popArcs1 = readArc("../data/shp/reseau1.shp")
print ('Nombre de troncons reseau1:', len(popArcs1))

popArcs2 = readArc("../data/shp/reseau2.shp")
print ('Nombre de troncons reseau2:', len(popArcs2))


# =============================================================================
#   Paramètres par défaut
paramApp = ParameterNM()

# On ajoute les réseaux
paramApp.setPopulationsArcs1(popArcs1)
paramApp.setPopulationsArcs2(popArcs2)


# =============================================================================
#    Lancement de l'appariement
# (net1, net2, edl) = appariementDeJeuxGeo(paramApp)

appariementDeJeuxGeo(paramApp)



