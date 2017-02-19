from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
m2=new_matrix()
matrix[0][0]=100
matrix[1][0]=100
matrix[0][1]=200
matrix[1][1]=200
print_matrix(matrix)
draw_lines( matrix, screen, color )
scalar_mult(matrix, 3)
print_matrix(matrix)
ident(matrix)
print_matrix(matrix)
matrix_mult(matrix,m2)
print_matrix(m2)

display(screen)
