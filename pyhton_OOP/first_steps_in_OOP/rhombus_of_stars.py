def print_rhombus(figure_size, curr_row):
    print(" " * (figure_size - curr_row), end="")
    for col in range(1, curr_row + 1):
        print("* ", end="")
    print()



n = int(input())

for row in range(1, n + 1):
    print_rhombus(n, row)

for row in range(n - 1, -1, -1):
    print_rhombus(n, row)
