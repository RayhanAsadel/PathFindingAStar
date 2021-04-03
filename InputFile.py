print("Halo Test")


print()
filename = str(input("Masukan Nama File (Nama.txt): "))         #Masukan nama file dengan format "Nama.txt"
print()
arrFile = []

with open(filename,'r') as file:
    for line in file:
        arrFile.append(line.replace('\n', '').replace('(','').replace(')',''))
        print(line,end="")
     
            #if line.startswith('-'):
            #    continue
            ##else:
            ##    ListKiri.append(line.replace(',','').replace(' ','').replace('C','').replace('\n',' '))
X = 0
Y = 0
Namasimpul = str("")
ArrSimpul = []
for i in range (1, int(arrFile[0])+1):
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

    ArrSimpul.append((NamaSimpul,X,Y))
print(ArrSimpul)    
print(ArrSimpul[0][0]) 
print(ArrSimpul[0][1]) 
print(ArrSimpul[0][2])  