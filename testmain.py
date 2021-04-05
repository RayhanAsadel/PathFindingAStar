#File gabungan
from os import name
from InputFile import ArrSimpul
import math

#Parsing file menjadi array of node, format : [Name, X, Y, {Neighbors : Bobot}]
def inputFile(filename):
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
    MatriksAdjacency = [ [ -1 for i in range(jmlNode) ] for j in range(jmlNode) ]
    for i in range (1, jmlNode+1):
        #print(arrFile[i])
        stringTempCoor = str("")
        for j in range (len(arrFile[i])):

            if (arrFile[i][j] == ','):
                X = int(stringTempCoor)
                stringTempCoor = ""

            elif (arrFile[i][j] == ' '):
                Y = int(stringTempCoor)
                stringTempCoor = ""
            elif (arrFile[i][j] != ',' and arrFile[i][j] != ' '):
                stringTempCoor = stringTempCoor+arrFile[i][j]
                NamaSimpul = stringTempCoor
        ArrSimpul.append([NamaSimpul,X,Y])

    NilaiBobot = int(0)
    k = int(0)
    l = int(0)

    for i in range (jmlNode+1, len(arrFile)):
        #print(arrFile[i])
        stringTempCoor = str("")
        l = 0
        for j in range (len(arrFile[i])):
            if (arrFile[i][j] == '[' and arrFile[i][j] == "]"):
                continue
            elif (arrFile[i][j] == ' ' or arrFile[i][j] ==']'):
                NilaiBobot = int(stringTempCoor)
                MatriksAdjacency[k][l] = NilaiBobot
                stringTempCoor = ""
                l = l+1
            elif (arrFile[i][j] != '[' and arrFile[i][j] != ' ' and arrFile[i][j] != ']'):
                stringTempCoor = stringTempCoor+arrFile[i][j]
            
        k = k+1
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

    # print("list of node [Name, X, Y, {Neighbors : Bobot}]\n")
    # for i in range (len(ArrSimpul)):
    #     print("Node", i+1,  ":" ,ArrSimpul[i])
    return (ArrSimpul)

class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str, x:int, y:int, neightbor:dict):
        self.name = name
        self.parent = parent
        self.neightbor = neightbor
        self.x = x # Coordinat X
        self.y = y # Coordinat Y
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other:str):
        return self.name == other
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return (self.name)

def Heuristic(node1:Node, node2:Node):
    x1 = node1.x
    x2 = node2.x
    y1 = node1.y
    y2 = node2.y
    d = math.sqrt((math.pow((x2-x1), 2))+(math.pow((y2-y1), 2)))
    return d

class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

# A* search
def astar_search(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

def main():
    filename = str(input("Masukan Nama File (Nama.txt): "))         #Masukan nama file dengan format "Nama.txt"
    file = inputFile(filename)
    # print(file)
    arrNode = []
    for i in range (len(file)):
        arrNode.append(Node(file[i][0], None, file[i][1], file[i][2], file[i][3]))
    # print(arrNode)z
    # print(Heuristic(arrNode[4], arrNode[1]))
    # print(Heuristic(arrNode[1], arrNode[4]))
    graph = Graph()
    heuristic = {} #dihitung dari node 1
    for i in range (len(arrNode)):
        heuristic[arrNode[i].name] = Heuristic(arrNode[0], arrNode[i]) 
    print(heuristic)

    for i in range (len(arrNode)):
        for j in arrNode[i].neightbor:
            print (arrNode[i].name, "connected to", j, "with distace", arrNode[i].neightbor[j])
            graph.connect(arrNode[i].name, j, arrNode[i].neightbor[j])

    inputNode1 = str(input("Node Asal : "))
    inputNode2 = str(input("Node Tujuan : "))

    # for i in range (len(arrNode)):
    #     for j in range (len(arrNode)):
    #         if (arrNode[i].name == inputNode1 and arrNode[j].name == inputNode2):
    #             path = astar_search(graph, heuristic, arrNode[i], arrNode[j], filename)
    #         else:
    #             path = None
    # print("Path :", path)

if __name__ == "__main__": main()