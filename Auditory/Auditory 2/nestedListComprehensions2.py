"""Користејќи list comprehension дадена матрица составена од броеви
 да се промени секој елемент така што ако припаѓа во горната половина
 (индексот на редицата е помеѓу 0 и n/2) треба да се помножи со 2 а ако
 припаѓа на долната половина треба да се помножи со 3."""

def multiply(element, i, n):
    if i < n / 2:
        return element * 2
    else:
        return element * 3

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    matrix = []
    for i in range(0, n):
        matrixRow = [int(element) for element in input().split(" ")]
        matrix.append(matrixRow)
    newMatrix = [[multiply(matrix[i][j], i, n) for j in range(0, m)] for i in range(0,n)]
    print(newMatrix)
