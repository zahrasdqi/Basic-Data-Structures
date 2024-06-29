import Sparsematrix
normal_matrix = [[0,2,0],[1,0,0],[0,0,3]]

sparse_matrix = Sparsematrix.SparseMatrix(normal_matrix)
print(sparse_matrix.sparse_matrix)

sparse_matrix.transpose()
print(sparse_matrix.sparse_matrix)

sparse_matrix.change_element((2,2),4)
print(sparse_matrix.sparse_matrix)