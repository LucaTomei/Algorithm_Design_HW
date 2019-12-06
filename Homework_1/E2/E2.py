import networkx as nx, matplotlib.pyplot as plt
from networkx.algorithms import tree

#punto1
#CREAZIONE GRAFO E ARCHI 
G = nx.Graph()
tupleList = [(0, 2, 49), (0,4,43), (1, 3, 31), (1, 2, 56)]
for tuple in tupleList: G.add_edge(tuple[0], tuple[1], weight=tuple[2])


#CREAZIONE MINIMUM SPANNING TREE, LISTA DEGLI ARCHI ORDINE CRESCENTE
edgelist = list(tree.minimum_spanning_edges(G, algorithm='kruskal', data=True))

#CREAZIONE GRAFO COMPLETO CON PESO ARCHI A NONE
G_complete=nx.complete_graph(5)

NewGraph = nx.Graph()

#ASSEGNAZIONE DEL PESO DEGLI ARCHI DEL MST AL GRAFO COMPLETO
for i in edgelist:
    a=int(i[0])
    b=int(i[1])
    G_complete[a][b]['weight']=i[2].get("weight")

#LISTA DEGLI ARCHI ORDINE DECRESCENTE
print("List of Edges: ", edgelist)

nodi=G.nodes
lista_nodi = [];
for nodo in nodi:
    lista_nodi.append(nodo)
print("List of Nodes:", lista_nodi)


lista_nuvole = [];
for nodo in lista_nodi: 
    nuvola = []
    nuvola.append(nodo)
    lista_nuvole.append(list(nuvola))
print("List of Clouds: " , lista_nuvole)



for i in edgelist:
    node1=int(i[0])
    node2=int(i[1])
    nuvola1 = nuvola2 = []
    for nuv in lista_nuvole:
        if node1 in nuv :   nuvola1 = nuv 
        if node2 in nuv :   nuvola2 = nuv
    peso= i[2].get("weight")
    for n1 in nuvola1:
        for n2 in nuvola2:
            if(not(n1 == node1 and n2 == node2)) :
                peso1=G_complete.get_edge_data(n1,n2).get("weight")
                if(not peso1):
                    NewGraph.add_edge(n1, n2, weight=peso+1)
                    G_complete[n1][n2]['weight']=peso+1
                else:   NewGraph.add_edge(n1, n2, weight=peso)
                
    nuvola3 = nuvola1.extend(nuvola2)
    nuvola1 = nuvola3
    lista_nuvole.remove(nuvola2)



#punto 2
#SCORRE TUTTA LA LISTA DEGLI ARCHI DEL GRAFO SOMMANDONE IL PESO AL CONTATORE SUMM
summ=0
for i in G_complete.edges:  summ += G_complete.get_edge_data(i[0],i[1]).get("weight")
print("The sum is: " + str(summ))

#VERIFICA DI CORRETTEZZA DEL MST CHE SI CREA DAL GRAFO GENERATO NEL PUNTO 1
edgelist = list(tree.minimum_spanning_edges(G_complete, algorithm='kruskal', data=True))
M = nx.Graph()
M.add_edges_from(edgelist)
nx.draw(M, with_labels=True, font_weight='bold')
plt.title('Figure 1', y=-0.01)
plt.show()
    
nx.draw(G_complete, with_labels=True, font_weight='bold')
plt.title('Figure 2', y=-0.01)
plt.show()
