"""Користејќи list comprehension дадена матрица составена од броеви
 да се промени секој елемент така што ќе се помножи со 2. Секој елемент
  на матрицата се чита од тастатура така што прво се читаат N и M
  (број на редици и колони) а потоа во секој ред се читаат елементите
  одделени со празно место"""

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    matrix = []
    for i in range(0, n):
       matrixRow = [int(element) for element in input().split(" ")]
       matrix.append(matrixRow)
    print(matrix)

    newMatrix = []
    for i in range(0, n):
        newMatrixRow = [element * 2 for element in matrixRow]
        newMatrix.append(newMatrixRow)
    print(newMatrix)
