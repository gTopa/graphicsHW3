from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix)
scalar_mult(matrix, 3)
print_matrix(matrix)
ident(matrix)
print_matrix(matrix)
draw_lines( matrix, screen, color )
display(screen)
