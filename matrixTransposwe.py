eg = [[1,2,0],
      [0,1,0],
      [2,0,1]]


def transpose_matrix(m: list):
    n=[]
    for i in range(len(eg[0])):
        n.append([])


    for i in m: #Columnas i=1: [1,0,0] i=2: [0,1,0] i=3: [0,0,1]
        c=0
        for t in i: #Rows
            n[c].append(t)
            c+=1
    print(n)
    
    return None

transpose_matrix(eg)