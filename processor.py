import math

class Matrix:

    def __init__(self):
        self.nm = list(input().split())
        self.rows, self.cols = map(int, self.nm)
        self.mat = [input().split() for _ in range(int(self.nm[0]))]
        self.e_mat = [n for row in self.mat for n in row]

    def transposed_main(self):
        main = list(map(list, zip(*self.mat)))
        return main

    def transposed_side(self):
        side = [[self.mat[j][i] for j in reversed(range(len(self.mat)))] for i in reversed(range(len(self.mat)))]
        return side

    def transposed_vertical(self):
        vertical = [[self.mat[i][j] for j in reversed(range(len(self.mat)))] for i in range(len(self.mat))]
        return vertical

    def transposed_horizontal(self):
        hor = [[self.mat[i][j] for j in range(len(self.mat))] for i in reversed(range(len(self.mat)))]
        return hor


def matrix_determinant(matrix):
    row = len(matrix)
    col = len(matrix[0])
    if row == 1:
        return matrix[0][0]
    if row == 2:
        return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])
    else:
        determinant = 0
        for i in range(row):
            minor = [[matrix[k][j] for j in range(col) if j != i] for k in range(1, row)]
            determinant += float(matrix[0][i]) * matrix_determinant(minor) * (-1)**(1+i+1)
        return determinant


def matrix_addition(matrix_a, matrix_b):
    return list(map(lambda x, y: float(x) + float(y), matrix_a, matrix_b))


def matrix_multiplier(extracted_matrix, multiplier):
    return [float(item) * float(multiplier) for item in extracted_matrix]


def matrices_multiplication(matrix_a, matrix_b):
    return [[sum(float(a) * float(b) for a, b in zip(row_a, col_b)) for col_b in zip(*matrix_b)] for row_a in matrix_a]


def matrix_recostituent(extracted_matrix, cols):
    re_mat = [extracted_matrix[x:x + cols] for x in range(0, len(extracted_matrix), cols)]
    return re_mat


def matrix_printer(matrix):
    print("The result is:")
    for list_ in matrix:
        print(*list_)


def menu_1():
    print("1. Add matrices\n"
          "2. Multiply matrix by a constant\n"
          "3. Multiply matrices\n"
          "4. Transpose matrices\n"
          "5. Calculate a determinant\n"
          "6. Inverse matrix\n"
          "0. Exit")


def menu_2():
    print("\n1. Main diagonal\n"
          "2. Side diagonal\n"
          "3. Vertical line\n"
          "4. Horizontal line")


while True:
    menu_1()
    choice = int(input())

    if choice not in [0, 1, 2, 3, 4, 5]:
        print("Sorry unknown selection")
    elif choice == 1:
        matrix_1 = Matrix()
        matrix_2 = Matrix()
        if matrix_1.nm != matrix_2.nm:
            print("The operation cannot be performed.")
        else:
            new_matrix = matrix_addition(matrix_1.e_mat, matrix_2.e_mat)
            re_matrix = matrix_recostituent(new_matrix, matrix_1.cols)
            matrix_printer(re_matrix)
    elif choice == 2:
        matrix_1 = Matrix()
        result = matrix_multiplier(matrix_1.e_mat, float(input()))
        re_matrix = matrix_recostituent(result, matrix_1.cols)
        matrix_printer(re_matrix)
    elif choice == 3:
        matrix_1 = Matrix()
        matrix_2 = Matrix()
        if matrix_1.cols != matrix_2.rows:
            print("The operation cannot be performed.")
        else:
            result = matrices_multiplication(matrix_1.mat, matrix_2.mat)
            matrix_printer(result)
    elif choice == 4:
        menu_2()
        new_choice = int(input())
        matrix_1 = Matrix()
        if new_choice not in [1, 2, 3, 4]:
            print("Sorry unknown selection")
        elif new_choice == 1:
            matrix_printer(matrix_1.transposed_main())
        elif new_choice == 2:
            matrix_printer(matrix_1.transposed_side())
        elif new_choice == 3:
            matrix_printer(matrix_1.transposed_vertical())
        elif new_choice == 4:
            matrix_printer(matrix_1.transposed_horizontal())
    elif choice == 5:
        matrix_1 = Matrix()
        print(matrix_determinant(matrix_1.rows, matrix_1.cols, matrix_1.mat))
        print()
    elif choice == 0:
        break
