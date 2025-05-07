def anti_daig(matrix):
    n = len(matrix)
    for col in range(n):
        i,j = 0, col
        while j>=0:
            print(matrix[i][j], end="")
            i +=1
            j -=1
        print()
    for row in range(1,n):
            i,j = row, n-1
            while i<n:
                print(matrix[i][j],end=" ")
                i +=1
                j -=1
            print()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        print("anti daiagonals of the matrix")
        anti_daig(matrix)