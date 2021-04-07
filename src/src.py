#Main.py
from os import name
import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import math
import pandas as pd

#Parsing file menjadi array of node, format : [Name, X, Y, {Neighbors : Bobot}]
def inputFile():
    print()
    filename = str(input("Masukan Nama File (Nama.txt): ")) 
    arrFile = []

    #Loop masukin baris ke array arrFile
    with open(filename,'r') as file:
        for line in file:
            arrFile.append(line.replace('\n', '').replace('(','').replace(')',''))

    X = 0
    Y = 0
    NamaSimpul = str("")
    ArrSimpul = []      #Arr berisi list (Nama, X, Y) dari simpul
    jmlNode = int(arrFile[0])
    MatriksAdjacency = [ [ 0 for i in range(jmlNode) ] for j in range(jmlNode) ]

    #loop mengisi ArrSimpul berisi list (Nama, X, Y) dari simpul
    for i in range (1, jmlNode+1):
        #print(arrFile[i])
        stringTempCoor = str("")
        for j in range (len(arrFile[i])):

            if (arrFile[i][j] == ','):
                X = float(stringTempCoor)
                stringTempCoor = ""

            elif (arrFile[i][j] == ' '):
                Y = float(stringTempCoor)
                stringTempCoor = ""
            elif (arrFile[i][j] != ',' and arrFile[i][j] != ' '):
                stringTempCoor = stringTempCoor+arrFile[i][j]
                NamaSimpul = stringTempCoor
        ArrSimpul.append([NamaSimpul,X,Y])

    NilaiBobot = float(0)
    k = int(0)
    l = int(0)

    #Mengisi matriks adjacency dengan bobot sesuai inputfile
    for i in range (jmlNode+1, len(arrFile)):
        #print(arrFile[i])
        stringTempCoor = str("")
        l = 0
        for j in range (len(arrFile[i])):
            if (arrFile[i][j] == '[' and arrFile[i][j] == "]"):
                continue
            elif (arrFile[i][j] == ' ' or arrFile[i][j] ==']'):
                NilaiBobot = float(stringTempCoor)
                MatriksAdjacency[k][l] = NilaiBobot
                stringTempCoor = ""
                l = l+1
            elif (arrFile[i][j] != '[' and arrFile[i][j] != ' ' and arrFile[i][j] != ']'):
                stringTempCoor = stringTempCoor+arrFile[i][j]
        k = k+1
    # print("Matriks Adjacency")
    # print(MatriksAdjacency)
    
    #Memasukan dictionary ketetanggan pada arr simpul, menjadi list (Nama, X, Y, {Simpul : bobot}) dari simpul
    arrNodeName = []
    for i in range (len(ArrSimpul)):
        arrNodeName.append(ArrSimpul[i][0])       
    for i in range(len(ArrSimpul)):
        temp = {}
        k = 0
        for j in range (len(MatriksAdjacency[i])):
            temp[arrNodeName[k]] = MatriksAdjacency[i][j]
            k+=1
        neightbors = {}
        for l in temp.keys():
            if (temp[l] != 0):
                neightbors[l] = temp[l]
        (ArrSimpul[i]).append(neightbors)
    
    return (ArrSimpul)

class Node:
    def __init__(self, name:str, parent:str, x:float, y:float, neightbor:dict):
        self.name = name
        self.parent = parent
        self.neightbor = neightbor
        self.x = x # koordinat X
        self.y = y # koordinat Y
        self.g = 0 # jarak dari simpul asal
        self.h = 0 # jarak ke simpul tujuan
        self.f = 0 # Total jarak
    # Compare
    def __eq__(self, other:str):
        return self.name == other
    # Sort
    def __lt__(self, other):
         return self.f < other.f
    # Print
    def __repr__(self):
        return (self.name)

def Haversine(node1:Node, node2:Node):
    lon1 =  math.radians(node1.x)
    lon2 =  math.radians(node2.x)
    lat1 =  math.radians(node1.y)
    lat2 =  math.radians(node2.y)
    R = 6373000
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    def connect(self, A, B, distance = 1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        neighbor = self.graph_dict.setdefault(a, {})
        if b is None:
            return neighbor
        else:
            return neighbor.get(b)

def make_ArrayofNode():
    file = inputFile()
    arrNode = []
    for i in range (len(file)):
        arrNode.append(Node(file[i][0], None, file[i][1], file[i][2], file[i][3]))
    return arrNode
  
# A* search
def Astar(graph, heuristics, start, end, arrayOfNode):
    openList = [] # Simpul hidup
    closedList = [] # Simpul yang sudah dikunjungi
    # Inisiasi simpul start dan goal
    start_node = Node(start, None, None, None, None)
    goal_node = Node(end, None, None, None, None)
    # Masukkan simpul start ke openList
    openList.append(start_node)
    
    # Loop hingga openList kosong
    while len(openList) > 0:
        openList.sort()
        current_node = openList.pop(0) # Node dengan jarak terkecil
        closedList.append(current_node) # Masukkan ke closedList
        if current_node == goal_node: # Jika node yang di cek adalah simpul tujuan
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            return path[::-1] #return reversed path
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key,value in neighbors.items():
            for i in range (len(arrayOfNode)):
                if (arrayOfNode[i].name == key):
            # Inisiasi node neighbor dengan parent current_node
                    neighbor = Node(key, current_node, arrayOfNode[i].x, arrayOfNode[i].y, arrayOfNode[i].neightbor)
            # Check apakah neighbor di dalam closedList
            if(neighbor in closedList):
                continue # Abaikan
            # Hitung f(n)
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Check apakah neighbor harus dimasukkan ke openList
            if(CheckAddNode(openList, neighbor) == True):
                openList.append(neighbor)
    return None # Tidak terdapat lintasan

def CheckAddNode(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

def main():
    arrNode = make_ArrayofNode()
    graph = Graph()
  
    haversine = {}
    for i in range (len(arrNode)):
        haversine[arrNode[i].name] = Haversine(arrNode[0], arrNode[i]) 
    
    for i in range (len(arrNode)):
        for j in arrNode[i].neightbor:
            graph.connect(arrNode[i].name, j, arrNode[i].neightbor[j])

    print("Daftar tempat/persimpangan jalan : ")
    for i in range (len(arrNode)):
        print(str(i+1)+ '.', arrNode[i])
    print()
    print("Masukkan Lokasi!")
    inputNode1 = str(input("Lokasi Awal : "))
    inputNode2 = str(input("Lokasi Tujuan : "))

    path = Astar(graph, haversine, inputNode1, inputNode2, arrNode)
    print()
    print("Lintasan :", path)
    # print(haversine)

    
    arraynamanode = []
    temp =""
    j
    for i in range (len(path)):
        j =0
        temp =""
        while (path[i][j]!=":"):
            temp = temp+ str(path[i][j])
            j=j+1
        
        arraynamanode.append(temp)

    arrayBobot = []
    tempbobot =""
    for i in range (len(path)):
        j = 0
        tempbobot =""
        while (path[i][j]!=' '):
            j=j+1
        j += 1
        while (j != len(path[i])):
            tempbobot = tempbobot+ str(path[i][j])
            j=j+1
        arrayBobot.append(float(tempbobot))

    print("Total jarak terpendek antara", inputNode1, "dan", inputNode2, "adalah", arrayBobot[len(arrayBobot)-1], "meter")

    G = nx.Graph()
    for i in range(len(path)):
        for j in range (len(arrNode)):
            if (arraynamanode[i]==arrNode[j].name):
                G.add_node(i,pos=(float(arrNode[j].x),float(arrNode[j].y)))
    i = 0
    j = 1
    while (j<len(path)):
        G.add_edge(i,j,weight=arrayBobot[j]-arrayBobot[i])
        i = j
        j = j+1

    raw_labels = arraynamanode
    lab_node = dict(zip(G.nodes, raw_labels))
    pos=nx.get_node_attributes(G,'pos')
    #nx.draw(G,pos)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edges(G, pos, edge_color='g',arrows=False)
    nx.draw_networkx_nodes(G, pos, node_color='r',node_size=500)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels,font_size=8)
    nx.draw_networkx_labels(G, pos, labels=lab_node, font_size=10, font_family="DejaVu Sans")
    plt.show()
   

if __name__ == "__main__": main()