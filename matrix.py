import math


def print_matrix( matrix ):
    for x in matrix:
        row=""
        for y in x:
            row+= str(y) + " "
        print row

def ident( matrix ):
    for x in range(4):
        for y in range(4):
            if(x==y):
                matrix[x][x]=1
            else:
                matrix[x][y]=0

def scalar_mult( matrix, s ):
    for x in range(4):
        for y in range(len(matrix[0])):
            matrix[x][y]=matrix[x][y]*s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 1 )
    return m
