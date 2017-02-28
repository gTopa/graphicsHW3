from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
m2=new_matrix()

matrix[0][0]=1
matrix[1][0]=1
matrix[0][1]=2
matrix[1][1]=2
print "orig\n"
print_matrix(m2)
print "scalar mult\n"
scalar_mult(m2, 3)
print_matrix(m2)
print "\nident"
ident(matrix)
print_matrix(matrix)
print "\nmatrix mult"
matrix_mult(matrix,m2)
print_matrix(m2)

add_edge(m2,100,100,1,350,350,1)
add_edge(m2,300,100,1,350,350,1)
add_edge(m2,200,100,1,350,350,1)

print "\nadded edges"
print_matrix(m2)

draw_lines(m2,screen,color)
display(screen)
