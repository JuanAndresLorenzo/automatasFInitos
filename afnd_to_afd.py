def crearFila(estados, AFND):
    res = []
    t=0
    for estado in estados:
        h=0
        if(t==0):
            res = AFND[estado].copy()
        else:
            while(h<len(AFND[estado])):
                res[h] = res[h].union(AFND[estado][h])
                h+=1
        t=1
    return res

def isInSetList(inSet, setList):
    for sets in setList:
        if inSet == sets:
            return True
    return False
    

def afnd_to_afd(AFND):
    existentes = [{0}]
    AFD = []
    AFD.append(crearFila({0}, AFND))
    i=0
    while(i<len(AFD)):
        j=0
        while(j<len(AFD[0])):
            if not isInSetList(AFD[i][j], existentes):
                existentes.append(AFD[i][j].copy())
                AFD.append(crearFila(AFD[i][j], AFND))
            j+=1
        i+=1
    return AFD

afnd1 = input() 

# fila = afnd_to_afd(afnd1)
fila = afnd_to_afd(afnd1)

print("fila: ")
x=0
while(x<len(fila)):  
    print(fila[x])
    x+=1

