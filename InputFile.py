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

connected = []
# for i in range(jmlNode+1, len(arrFile)):
#     tempangka = 0
#     tempbobot = []
#     stringTempCoor = str("")
#     for j in range(len(arrFile[i])):
#         if (arrFile[i][j] != ' '):
#             tempangka = int(stringTempCoor)
#             stringTempCoor = ""
#         elif (arrFile[i][j] != ' ' and arrFile[i][j] != '0'):
#             stringTempCoor = stringTempCoor+arrFile[i][j]
#     connected.append(tempbobot)
# for l in range (5):
#     for k in range (3):
#         print(arrFile[l][k])
        # if (arrFile[i][k] != '0' or arrFile[i][k] != ' '):
        #     connected.append([ArrSimpul[k][0], arrFile[i][k]])
print()

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
        elif (arrFile[i][j] == ' '):
            NilaiBobot = int(stringTempCoor)
            MatriksAdjacency[k][l] = NilaiBobot
            stringTempCoor = ""
            l = l+1
        elif (arrFile[i][j] != '[' and arrFile[i][j] != ' ' and arrFile[i][j] != ']'):
            stringTempCoor = stringTempCoor+arrFile[i][j]
        
    k = k+1
        


print(ArrSimpul)    
print(connected)
print(MatriksAdjacency)
#for i in range(len(MatriksAdjacency)):
#    for j in range (len(MatriksAdjacency)):
#        print(MatriksAdjacency[i][j],end ="")
#    print() 
# print(ArrSimpul[0][0]) 
# print(ArrSimpul[0][1]) 
# print(ArrSimpul[0][2])  