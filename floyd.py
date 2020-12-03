N = 4
M = 0xfffffff
edge = [[0,2,6,4],[M,0,3,M],[7,M,0,1],[5,M,12,0]]
A = edge[:]
path = [[0 for _ in range(N)] for _ in range(N)]
def Floyd():
    for i in range(N):
        for j in range(N):
            if(edge[i][j] != M and edge[i][j] != 0):
                path[i][j] = i
    print ('init:')
    print (A,'\n',path)
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if(A[b][a]+A[a][c]<A[b][c]):
                    A[b][c] = A[b][a] + A[a][c]
                    path[b][c] = path[a][c]
    print ('result:')
    print (A,'\n',path)
if __name__ == "__main__":
    Floyd()