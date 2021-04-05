
# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt



def inputFile():
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
    # Initialize the class
    def __init__(self, name:str, parent:str, x:float, y:float, neightbor:dict):
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

file = inputFile()
arrNode = []
for i in range (len(file)):
    arrNode.append(Node(file[i][0], None, file[i][1], file[i][2], file[i][3]))



G = nx.Graph()

for i in range (len(arrNode)):
        for j in arrNode[i].neightbor:
            # print (arrNode[i].name, "connected to", j, "with distace", arrNode[i].neightbor[j])
            G.add_edge(arrNode[i].name, j, weight=arrNode[i].neightbor[j])

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility


# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

ax = plt.gca()
ax.margins(0.08)
plt.axis("on")
plt.tight_layout()
plt.show()