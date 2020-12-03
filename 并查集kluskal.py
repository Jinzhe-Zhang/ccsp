
def kru(tree,n):
    #union为并查集,并设初值为-1
    union=[i for i in range(n+1)]
    #首先按照权值大小由小到大对tree排序
    tree.sort(key=lambda x:x[2])
    #先将权值最小的加入到并查集中去
    union[tree[0][0]]=tree[0][1]
    length=len(tree)
    max_leaf=-1
    for i in range(1,length):
        #首先找到两个节点的根在哪里
        posi_i=tree[i][0]
        posi_j=tree[i][1]
        while(union[posi_i]!=posi_i):
            posi_i=union[posi_i]
        while(union[posi_j]!=posi_j):
            posi_j=union[posi_j]
        #如果两节点根相同，代表形成了回路。故不选择这两个节点
        if posi_i==posi_j:
            continue
        #按照节点大小来排序，这样不会出现冲突（所有的点的顺序都是一个方向的）
        elif posi_i>posi_j:
            union[posi_j]=posi_i
        else :
            union[posi_i]=posi_j
        if tree[i][2]>max_leaf:
                max_leaf=tree[i][2]
        #如果union的长度等于n-1，代表最小生成树已经构建完成了。
        if len(union)==n-1:
            return max_leaf
    return max_leaf
#主函数
n=int(input())
m=int(input())
root=int(input())-1
#创建一个m行，3列的数组，并且初值全部为0
tree=[tuple(map(lambda x:int(x),input().split())) for j in range(m)]
#读入信息，存入到tree中去
if n==0:
    print(0)
else:
    print(kru(tree,n))
