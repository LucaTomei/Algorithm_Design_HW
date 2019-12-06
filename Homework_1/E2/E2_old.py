import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree


#punto1
#CREAZIONE GRAFO E ARCHI 
G = nx.Graph()
G.add_edge(0, 2, weight=49)
G.add_edge(0, 4, weight=43)
G.add_edge(1, 3, weight=31)
G.add_edge(1, 2, weight=56)

#CREAZIONE MINIMUM SPANNING TREE, LISTA DEGLI ARCHI ORDINE CRESCENTE
mst = tree.minimum_spanning_edges(G, algorithm='kruskal', data=True)
print("tipo", type(mst))
edgelist = list(mst)

#CREAZIONE GRAFO COMPLETO CON PESO ARCHI A NONE
G_complete=nx.complete_graph(5)

GrafoDioCane = nx.Graph()

#ASSEGNAZIONE DEL PESO DEGLI ARCHI DEL MST AL GRAFO COMPLETO
for i in edgelist:
    a=int(i[0])
    b=int(i[1])
    G_complete[a][b]['weight']=i[2].get("weight")

#LISTA DEGLI ARCHI ORDINE DECRESCENTE
print(edgelist)

#METODO A: PRENDE IN INPUT (LISTA DI TUTTI I PERCORSI CHE COLLEGANO N1->N2 DOVE OGNI SINGOLO PERCORSO è RAPPRESENTATO DALLA LISTA NEI NODI CHE VENGONO ATTRAVERSATI IN ORDINE,
#                           NODO_ORIGINE,
#                           NODO_DESTINAZIONE,
#                           PESO ARCO CHE COLLEGA N1->N2 NEL MST)
#ALGORITMO REALIZZATO CUT PROPERTY
#IMPLEMENTAZIONE NEL METODO: SCORRE LA LISTA DEI PERCORSI, DI OGNI PERCORSO VISITA TUTTI GLI ARCHI E SE HANNO PESO 'NONE', SETTA SOLO IL PESO DEL PRIMO ARCO CON PESO NONE A QUELLO DELL'ARCO ASSOCIATO NEL MST +1 
#
#METODO A: RESTITUISCE IN OUTPUT, TRAMITE SIDE-EFFECT, IL GRAFO COMPLETO CON I PESI DEGLI ARCHI CHE SONO PRESENTI UN QUALSIASI PERCORSO CHE COLLEGA N1->N2 ASSEGNATI AL PESO DELL'ARCO DEL MST+1
def a(node1,node2,nuv1,nuv2,peso):
    '''for i in range(0, :
        lungh=len(i)-1
        for k in range(0,lungh):
            #print(i[:2])
            peso1=G_complete.get_edge_data(i[0],i[1]).get("weight")
            if(peso1==None):
                G_complete[i[0]][i[1]]['weight']=peso+1
            #print(peso)
            i.pop(0)'''
    for n1 in nuv1:
        for n2 in nuv2:
            if(not(n1 == node1 and n2 == node2)) :
                peso1=G_complete.get_edge_data(n1,n2).get("weight")
                print(peso1, "bravo")
                if(peso1==None):
                    print(n1, n2)
                    G_complete[i[0]][i[1]]['weight']=peso+1
                    
                print(G_complete[i[0]][i[1]]['weight'])








#SCORRE LA LISTA DI TUTTI GLI ARCHI IN ORDINE DECRESCENTE E PRIMA DI CHIAMARE IL METODO A, CREA LA LISTA DI TUTTI I POSSIBILI PERCORSI CHE COLLEGANO I NODI ADIACENTI ALL'ARCO PRESO IN CONSIDERAZIONE NELL'ITERAZIONE
#lista_nuvole = G.nodes()
nodi=G.nodes
lista_nodi = [];
for nodo in nodi:
    lista_nodi.append(nodo)
print(lista_nodi)


lista_nuvole = [];
for nodo in lista_nodi: 
    nuvola = []
    nuvola.append(nodo)
    print(type(nuvola))
    lista_nuvole.append(list(nuvola))
print(lista_nuvole)



for i in edgelist:
    node1=int(i[0])
    node2=int(i[1])
    nuvola1 = []
    nuvola2 = []
    for nuv in lista_nuvole:
        if node1 in nuv :
            nuvola1 = nuv 
        if node2 in nuv :
            nuvola2 = nuv
    print(node1, node2, nuvola1, nuvola2, i[2].get("weight"))
    #a(node1, node2, nuvola1, nuvola2, i[2].get("weight"))
    peso= i[2].get("weight")
    for n1 in nuvola1:
        for n2 in nuvola2:
            if(not(n1 == node1 and n2 == node2)) :
                peso1=G_complete.get_edge_data(n1,n2).get("weight")
                print(peso1, "bravo")
                if(peso1==None):
                    print(n1, n2)
                    tmp = peso+1
                    GrafoDioCane.add_edge(n1, n2, weight=tmp)
                    G_complete[n1][n2]['weight']=peso+1
                    print(G_complete[n1][n2]['weight'], "eccolo")
                else:
                    GrafoDioCane.add_edge(n1, n2, weight=peso)
                print(G_complete[n1][n2]['weight'])
                
    nuvola3 = nuvola1.extend(nuvola2)
    nuvola1 = nuvola3
    lista_nuvole.remove(nuvola2)
    print(lista_nuvole)
    #a(all_paths,node1,node2,i[2].get("weight"))





print("------------------------------------")
    
for item in GrafoDioCane:
    print(item)

print("------------------------------------")


    

#punto 2
#SCORRE TUTTA LA LISTA DEGLI ARCHI DEL GRAFO SOMMANDONE IL PESO AL CONTATORE SUMM
summ=0
count = 0
for i in G_complete.edges:
    print(i, G_complete.get_edge_data(i[0],i[1]).get("weight"), "PORCOP DIO")
    summ += G_complete.get_edge_data(i[0],i[1]).get("weight")
print(summ)

#VERIFICA DI CORRETTEZZA DEL MST CHE SI CREA DAL GRAFO GENERATO NEL PUNTO 1
mst = tree.minimum_spanning_edges(G_complete, algorithm='kruskal', data=True)
edgelist = list(mst)
M = nx.Graph()
M.add_edges_from(edgelist)
nx.draw(M, with_labels=True, font_weight='bold')
plt.show()
    
nx.draw(G_complete, with_labels=True, font_weight='bold')
plt.show()
