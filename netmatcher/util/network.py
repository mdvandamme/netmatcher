# -*- coding: utf-8 -*-


from tracklib import Network, Node
from tracklib import compare, MODE_COMPARISON_HAUSDORFF


class NetworkNM():

    @staticmethod
    def filtreDoublons(network, tolerance):
        '''
        /**
        * Filtrage des noeuds doublons (plusieurs noeuds localisés au même endroit).
        * <ul>
        * <li>NB: si cela n'avait pas été fait avant, la population des noeuds est
        * indexée dans cette méthode (dallage, paramètre = 20).
        * <li>Cette méthode gère les conséquences sur la topologie, si celle-ci a été
        * instanciée auparavant.
        * <li>Cette méthode gère aussi les conséquences sur les correspondants (un
        * noeud gardé a pour correspondants tous les correspondants des doublons).
        * </ul>
        * @param tolerance Le paramètre tolérance spécifie la distance maximale pour
        *          considérer deux noeuds positionnés au même endroit.
        */
        '''
        print ("         Double nodes filtering")

        aJeter = list()
        selection = None



        '''
        
        for (Noeud noeud : this.getPopNoeuds()) {
          if (aJeter.contains(noeud)) {
            continue;
          }
          selection = this.getPopNoeuds().select(noeud.getCoord(), tolerance);
          selection.remove(noeud);
          for (Noeud doublon : selection) {
            // on a trouvé un doublon à jeter
            // on gère les conséquences sur la topologie et les
            // correspondants
            aJeter.add(doublon);
            noeud.addAllCorrespondants(doublon.getCorrespondants());
            for (Arc a : new ArrayList<Arc>(doublon.getEntrants())) {
              noeud.addEntrant(a);
            }
            for (Arc a : new ArrayList<Arc>(doublon.getSortants())) {
              noeud.addSortant(a);
            }
          }
        }
        this.getPopNoeuds().removeAll(aJeter);
        '''

    @staticmethod
    def creeTopologieArcsNoeuds(edges, cptNode, tolerance):
        '''
        Instancie la topologie de réseau d'une Carte Topo, en se basant sur la
        géométrie 2D des arcs et des noeuds. Autrement dit: crée les relations
        "noeud initial" et "noeud final" d'un arc.
        
        - ATTENTION: cette méthode ne rajoute pas de noeuds. Si un arc
          n'a pas de noeud localisé à son extrémité, il n'aura pas de noeud initial
          (ou final).
        - DE PLUS si plusieurs noeuds sont trop proches (cf. param tolérance), 
          alors un des noeuds est choisi au hasard pour la relation arc/noeud, 
          ce qui n'est pas correct.
        - IL EST DONC CONSEILLE DE FILTRER LES DOUBLONS AVANT SI NECESSAIRE.
        - NB: si cela n'avait pas été fait avant, la population des noeuds est
          indexée dans cette méthode (dallage, paramètre = 20).
        
        @param tolerance Le paramètre "tolerance" spécifie la distance maximale
               acceptée entre la position d'un noeud et la position d'une
               extrémité de ligne, pour considérer ce noeud comme extrémité (la
               tolérance peut être nulle).
        '''

        print ("         Construction of the topology between edges and nodes")

        network = Network()

        # Crée un nouveau noeud à l'extrémité de chaque arc si il n'y en a pas.
        # La topologie arcs/noeuds est instanciée au passage
        for edge in edges:

            if edge.geom.size() < 2:
                # warning: Edge has only 1 or 0 point and was ignored
                print ('warning: Edge has only 1 or 0 point and was ignored')
                continue

            # Source node
            idNoeudIni = str(cptNode)
            p1 = edge.geom.getFirstObs().position
            candidates = selectNodes(network, Node("0", p1), 0.5)
            if len(candidates) > 0:
                c = candidates[0]
                idNoeudIni = c.id
            else:
                cptNode += 1
            noeudIni = Node(idNoeudIni, p1)

            # Target node
            idNoeudFin = str(cptNode)
            p2 = edge.geom.getLastObs().position
            candidates = selectNodes(network, Node("0", p2), 0.5)
            if len(candidates) > 0:
                c = candidates[0]
                idNoeudFin = c.id
            else:
                cptNode += 1
            noeudFin = Node(idNoeudFin, p2)

            network.addEdge(edge, noeudIni, noeudFin)

        return (network, cptNode)



def selectNodes(network, node, distance):
    """Selection des autres noeuds dans le cercle dont node.coord est le centre,
    de rayon distance

    :param node: le centre du cercle de recherche.
    :param distance: le rayon du cercle de recherche.

    :return: tableau de NODES liste des noeuds dans le cercle
    """
    NODES = []

    if network.spatial_index is None:
        for key in network.getIndexNodes():
            n = network.NODES[key]
            if n.coord.distance2DTo(node.coord) <= distance:
                NODES.append(n)
    else:
        print ('INDEX !!!!!!')
        vicinity_edges = network.spatial_index.neighborhood(node.coord, unit=1)
        for e in vicinity_edges:
            source = network.EDGES[network.getEdgeId(e)].source
            target = network.EDGES[network.getEdgeId(e)].target
            if source.coord.distance2DTo(node.coord) <= distance:
                NODES.append(source)
            if target.coord.distance2DTo(node.coord) <= distance:
                NODES.append(target)

    return NODES


def selectEdges(network, line, distance):
    '''
    liste des arcs de la collection dans un voisinnage de tolerance de line

    Parameters
    ----------
    self.nodes : TYPE
        DESCRIPTION.
    edge.startPoint() : TYPE
        DESCRIPTION.
    tolerance : TYPE
        DESCRIPTION.

    Returns
    -------
    list : liste de noeuds

    '''

    selections = list()

    if network.spatial_index is None:
        for edge in network:
            track = edge.geom
            if compare(track, line, mode=MODE_COMPARISON_HAUSDORFF, verbose=False) <= distance:
                selections.append(edge)
    else:
        print ('INDEX !!!!!!')
        network.spatial_index.neighborhood(line, unit=1)

    return selections




