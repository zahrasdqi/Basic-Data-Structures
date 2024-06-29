class SparseMatrix:
    def __init__(self, matrix):
        self.sparse_matrix = self.create_sparse_matrix(matrix)

    def create_sparse_matrix(self, matrix):
        sparse_matrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    sparse_matrix.append((i, j, matrix[i][j]))
        return sparse_matrix

    def transpose(self):
        transposed_matrix = []
        for element in self.sparse_matrix:
            transposed_matrix.append((element[1], element[0], element[2]))
        self.sparse_matrix = transposed_matrix

    def change_element(self, address, new_value):
        for i in range(len(self.sparse_matrix)):
            if (self.sparse_matrix[i][0], self.sparse_matrix[i][1]) == address:
                self.sparse_matrix[i] = (address[0], address[1], new_value)
                break