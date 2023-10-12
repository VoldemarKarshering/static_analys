import csv
from math import log2

def reading(file_name):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=';')
        matrix = []
        for row in reader:
            matrix.append(row)
        return matrix

def task(matrix):
    res = 0.
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if int(matrix[i][j]):
                res -= int(matrix[i][j]) / (len(matrix) - 1) *  log2(int(matrix[i][j]) / (len(matrix) - 1))
    return res

if __name__ == "__main__":
    file_name = input()
    matrix = reading(file_name)
    print(task(matrix))