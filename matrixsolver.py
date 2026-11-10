
def multrow(matrix: list, row: int ,mult: float):
    n=0
    for i in matrix[row-1]:
        matrix[row-1][n] = i*mult    
    
    return matrix

#Sums row2 into row1
def sumrows(matrix: list, row1: int, row2: int):
    n=0
    for i in matrix[row1-1]:
        matrix[row1-1][n] = i + matrix[row2-1][n]
        n+=1
    return matrix


def checkpivots(matrix: list):
#Matrix (m x n) --> eg[n][m]
#len(eg)--> nº de columnas // len(eg[x])--> nº de filas
    pivinfo=[] #nº de fila (i), nº de columna (_)
    firstpivot=True
    #Pivot must be non-zero
    for _ in range(len(matrix)):
        n=0
        for i in range(len(matrix[0])):
            #We check the matrix in descending order going by columns
            num = matrix[i][_] 
            #Pivot must be non-zero and if it isnt the first pivot it must be on a lower row and and to the right
            if (num!=0) and ((firstpivot) or ((i>pivinfo[0]) and (_ > pivinfo[1]))):
               #print(num)
               #print(i, _, n-1)
               #We store the indexes of the number in order to check later
               pivinfo = [i, _]
               firstpivot=False
               if n-1 != i:
                   changerows(matrix, n, i+1)
            n+=1

    return matrix


def changerows(matrix: list, row1: int, row2: int):
    row1, row2 = row1-1, row2-1
    temp=matrix[row1]
    matrix[row1]=matrix[row2]
    matrix[row2]=temp    
    return matrix


# Cambiar el pivot más cercano a la primera row: print(changepivot(eg,1,(findpivot(eg)[2]+1)))

# Checkeamos la matriz y lo ponemos en orden dependiendo de los ceros y de los primeros pivots 

eg = [[1,0,4],
      [0,0,1],
      [0,1,1]]

print(checkpivots(eg))