filename = str(input("Masukan Nama File (Nama.txt): "))         #Masukan nama file dengan format "Nama.txt"
print()
arrFile = []

#Loop masukin baris ke array arrFile
with open(filename,'r') as file:
    for line in file:
        arrFile.append(line.replace('\n', '').replace('(','').replace(')',''))

X = 0
Y = 0

Namasimpul = str("")
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


#Buat Matriks ketetanggan berbobot
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

print("list of node [Name, X, Y, {Neighbors : Bobot}]\n")   #Value bobot, key simpul neighbors
for i in range (len(ArrSimpul)):
    print("Node", i+1,  ":" ,ArrSimpul[i])

"""
print((ArrSimpul[0][3].items()))        get semua dict item
print((ArrSimpul[0][3].keys()))         get semua key
print((ArrSimpul[0][3].values()))       get semua value

print((ArrSimpul[0][3].get('B')))       kalo ketemu b return valuenya
print((ArrSimpul[0][3].get('b',"not found"))) kalo gaektemu return not found
"""