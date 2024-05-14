import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()


    def creaGrafo(self,anno):
        self.grafo.add_nodes_from(DAO.getAllCountryYearNodes(anno))
        self.grafo.add_edges_from(DAO.getAllContiguityYearEdges(anno))

    def contaConnessioni(self):
        return len(list(nx.connected_components(self.grafo)))

    def contaViciniNodo(self,nodo):
        return self.grafo.degree(nodo)

