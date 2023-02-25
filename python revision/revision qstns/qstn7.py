"""Transpose of a matrix using list comprehension"""
#Transpose of a matrix is the interchanging of rows and columns
matrix = [[1,2],
          [3,4],
          [5,6],
          [7,8]]
trans_matrix = [[row[i] for row in matrix]for i in range(2)]
print(trans_matrix)