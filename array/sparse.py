import numpy as np
from scipy.sparse import csr_matrix

row_01 = np.array([0, 0, 1, 1, 2])
col_01 = np.array([0, 1, 2, 0, 2])
data_01 = np.array([1, 4, 5, 8, 9])
sparse_matrix_01 = csr_matrix((data_01, (row_01, col_01)),shape = (3, 3)).toarray()
print("First Sparse Matrix : ", sparse_matrix_01)


row_02 = np.array([0, 0, 1, 1, 2])
col_02 = np.array([2, 1, 1, 0, 2])
data_02 = np.array([3, 4, 7, 8, 9])
sparse_matrix_02 = csr_matrix((data_02, (row_02, col_02)),shape = (3, 3)).toarray()
print("Second Sparse Matrix : ", sparse_matrix_02)

##add_matrix = sparse_matrix_01 + sparse_matrix_02
##print("Addtion of the two matrices is : ", add_matrix)

subtract_matrix = sparse_matrix_01 - sparse_matrix_02
print("Addtion of the two matrices is : ", subtract_matrix)

print("Transpose of the given matrix is ", sparse_matrix_01.transpose())