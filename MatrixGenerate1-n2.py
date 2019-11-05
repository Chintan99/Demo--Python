#Python program to generate (given an integer n) a square matrix filled with elements from 1 to n2 in spiral order.

def generateMatrix(n):
        if n<=0:
            return [] 

        matrix=[row[:] for row in [[0]*n]*n]
        
        row_st=0
        row_ed=n-1
        
        col_st=0
        col_ed=n-1
        current=1
        
        while (True):
            if current>n*n:
                break
            for c in range (col_st, col_ed+1):
                matrix[row_st][c]=current
                current+=1
            row_st+=1
            for r in range (row_st, row_ed+1):
                matrix[r][col_ed]=current
                current+=1
            col_ed-=1
            for c in range (col_ed, col_st-1, -1):
                matrix[row_ed][c]=current
                current+=1
            row_ed-=1
            for r in range (row_ed, row_st-1, -1):
                matrix[r][col_st]=current
                current+=1
            col_st+=1
        return matrix


def main():
    STDIN = int(input())
    STDOUT= generateMatrix(STDIN)
    for row in STDOUT:
        print (" ".join(map(str,row)))
    #for i in range(len(STDOUT)):
        #print (STDOUT[i[0:3]], sep=",")

main()
