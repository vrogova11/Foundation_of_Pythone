class Matrix:

    def __init__(self, num):
        self.num = num
        pass

    def __str__(self):
        return '\n'.join('\t'.join(map(str, line)) for line in self.num)

    def __add__(self, other):
        new_sum = [[self.num[i][j] + other.num[i][j] for j in range(len(self.num[0]))] for i in range(len(self.num))]
        return new_sum


matrix1 = Matrix([[1, 2, 3], [3, -4, 4], [5, 6, -5], [7, 8, 6]])
matrix2 = Matrix([[9, -10, 9], [11, 12, 13], [13, 14, 15], [-15, 16, 17]])
matrix3 = Matrix(matrix1 + matrix2)
print('Матрица 1:')
print(matrix1)
print('Матрица 2:')
print(matrix2)
print(f'Матрица 1 + матрица 2:')
print(matrix3)


