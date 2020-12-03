class Color:
    black=0
    red=1
class Node:
    def __init__(self,info=None,color=None):
        self.info = info
        self.color = color
        self.lchild = None
        self.rchild = None
        self.parent = None
        self.leftnum = 0
class RBTree:
    def __init__(self):
        self.ext = Node(-1,1) # external node
        self.root = self.ext # since no elements are present
    def insert(self,val):
        temp = Node()
        ptr = self.root
        par = self.ext
        while(ptr!=self.ext):
            par = ptr
            if ptr.info > val:
                ptr.leftnum+=1 ##
                ptr = ptr.lchild
            # elif ptr.info < val:
            #     ptr = ptr.rchild
            # else:
            #     print('Duplicate Element')
            #     return
            else:
                ptr = ptr.rchild
        temp.info = val
        temp.lchild = self.ext
        temp.rchild = self.ext
        temp.color = 0
        temp.parent = par
        if par == self.ext:
            self.root = temp
        elif temp.info < par.info:
            par.leftnum+=1 ##
            par.lchild = temp
        else:
            par.rchild = temp
        self.balance_insert(temp)
    def balance_insert(self,ptr):
        while ptr.parent.color == 0:
            par = ptr.parent # parent
            grandPar = par.parent
            if par == grandPar.lchild:
                uncle = grandPar.rchild
                if uncle.color == 0:
                    par.color = 1
                    uncle.color = 1
                    grandPar.color = 0
                    ptr = grandPar
                else: # uncle black
                    if ptr == par.rchild:
                        self.rotate_left(par)
                        ptr = par
                        par = ptr.parent
                    par.Color = 1
                    grandPar.color = 0
                    self.rotate_right(grandPar)
            elif par == grandPar.rchild:
                uncle = grandPar.lchild
                if uncle.color == 0:
                    par.color = 1
                    uncle.color = 1
                    grandPar.color = 0
                    ptr = grandPar
                else: # uncle black
                    if ptr == par.lchild:
                        self.rotate_right(par)
                        ptr = par
                        par = ptr.parent
                    par.color = 1
                    grandPar.color = 0
                    self.rotate_left(grandPar)
            else:
                continue
        self.root.color = 1
    def search(self,key,return_loc=False):
        ptr = self.root
        while ptr!=self.ext:
            if ptr.info == key:
                return ptr if return_loc else 'True'
            elif ptr.info < key:
                ptr = ptr.rchild
            else:
                if return_loc:
                    ptr.leftnum -=1
                ptr = ptr.lchild
        return ptr if return_loc else 'False'
    def delete(self,val):
        ptr = self.search(val,True)
        if ptr == self.ext:
            print('Element does not exist')
            return
        if ptr.lchild != self.ext or ptr.rchild != self.ext:
            succ = self.inorder_succ(ptr)
            ptr.info = succ.info
            ptr = succ
        if ptr.lchild != self.ext:
            child = ptr.lchild
        else:
            child = ptr.rchild
        child.parent = ptr.parent
        if ptr == self.root:
            self.root = child
        elif ptr.parent.lchild == ptr:
            ptr.parent.lchild = child
        else:
            ptr.parent.rchild = child
        if child == self.root:
            child.color = 1
        elif ptr.color == 1:
            if child != self.ext:
                child.color = 1
            else:
                self.balance_delete(child)
        else:
            pass
    def balance_delete(self,ptr):
        while ptr != self.root:
            if ptr.parent.lchild == ptr:
                sib = ptr.parent.rchild # sibling
                # sibling red
                if sib.color == 0:
                    sib.color = 1
                    ptr.parent.color = 0
                    self.rotate_left(ptr.parent)
                    sib = ptr.parent.rchild # new sibling
                # both nephews black
                if sib.lchild.color == 1 and sib.rchild.color == 1:
                    sib.color = 0
                    if ptr.parent.color == 0:
                        ptr.parent.color = 1
                        return
                    ptr = ptr.parent
                # atleast one nephew black
                else:
                    # making far nephew red if it is black
                    if sib.rchild.color == 1:
                        sib.lchild.color = 1
                        sib.color = 0
                        self.rotate_right(sib)
                        sib = ptr.parent.rchild # new sibling
                    sib.color = ptr.parent.color
                    ptr.parent.color = 1
                    sib.rchild.color = 1
                    self.rotate_left(ptr.parent)
                    return
            # opposite of above condition
            else:
                sib = ptr.parent.lchild
                if sib.color == 0:
                    sib.color = 1
                    ptr.parent.color = 0
                    self.rotate_right(ptr.parent)
                    sib = ptr.parent.lchild
                if sib.lchild.color == 1 and sib.rchild.color == 1:
                    sib.color = 0
                    if ptr.parent.color == 0:
                        ptr.parent.color = 1
                        return
                    ptr = ptr.parent
                else:
                    if sib.lchild.color == 1:
                        sib.rchild.color = 1
                        sib.color = 0
                        self.rotate_left(sib)
                        sib = ptr.parent.lchild
                    sib.color = ptr.parent.color
                    ptr.parent.color = 1
                    sib.lchild.color = 1
                    self.rotate_right(ptr.parent)
                    return
    def inorder_succ(self,ptr):
        ptr = ptr.rchild
        while ptr.lchild != self.ext:
            ptr.leftnum-=1
            ptr = ptr.lchild
        return ptr
    def rotate_left(self,ptr):
        rptr = ptr.rchild # right child
        ptr.rchild = rptr.lchild
        if rptr.lchild!=self.ext:
            rptr.lchild.parent = ptr
        rptr.parent = ptr.parent
        if ptr.parent == self.ext:
            self.root = rptr
        elif ptr == ptr.parent.lchild:
            ptr.parent.lchild = rptr
        else:
            ptr.parent.rchild = rptr
        rptr.lchild = ptr
        ptr.parent = rptr
        rptr.leftnum += ptr.leftnum + 1
    def rotate_right(self,ptr):
        lptr = ptr.lchild # left child
        ptr.lchild = lptr.rchild
        if lptr.rchild!=self.ext:
            lptr.rchild.parent = ptr
        lptr.parent = ptr.parent
        if ptr.parent == self.ext:
            self.root = lptr
        elif ptr == ptr.parent.rchild:
            ptr.parent.rchild = lptr
        else:
            ptr.parent.lchild = lptr
        lptr.rchild = ptr
        ptr.parent = lptr
        ptr.leftnum -= lptr.leftnum + 1
    def nodesum(self,ptr):
        ptr=self.root
        s=0
        while ptr!=self.ext:
            s+=ptr.leftnum + 1
            ptr=ptr.rchild
        return s
    def getkth(self,k,ptr):
        # if k>self.nodesum():
        #     return None
        if k == ptr.leftnum+1:
            return ptr ##
        elif k <= ptr.leftnum:
            return self.getkth(k,ptr.lchild)
        else:
            return self.getkth(k-1-ptr.leftnum, ptr.rchild)
    def getrevkth(self,k,ptr):
        return self.getkth(self.nodesum(ptr)+1-k,ptr)
    def getmax(self,ptr):
        # if ptr == self.ext:
        #     return None
        while ptr.rchild != self.ext:
            ptr = ptr.rchild
        return ptr
    def getmin(self,ptr):
        # if ptr == self.ext:
        #     return None
        while ptr.lchild != self.ext:
            ptr = ptr.lchild
        return ptr
    def getindex(self,key,ptr):
        i=1
        ptr = self.root
        while ptr!=self.ext:
            if ptr.info == key:
                return ptr.leftnum + i
            elif ptr.info < key:
                i+=ptr.leftnum+1
                ptr = ptr.rchild
            else:
                ptr = ptr.lchild
        return 0
    def inorder(self,ptr):
        if ptr!=self.ext:
            self.inorder(ptr.lchild)
            print(ptr.info,end=' ')
            self.inorder(ptr.rchild)
    def display(self,ptr):
        print(ptr.info,'Color =',('Red' if ptr.color==1 else 'Black'), 'leftnum =',ptr.leftnum)
        if ptr.lchild != self.ext:
            print(ptr.info,'left -> ',end='')
            self.display(ptr.lchild)
        if ptr.rchild != self.ext:
            print(ptr.info,'right -> ',end='')
            self.display(ptr.rchild)
if __name__ == '__main__':
    t = RBTree()
    for i in tuple(map(lambda x:int(x),"1 2 3 3 4 5 6 7 8 9 10".split())):
        t.insert(i)
    print(t.getkth(6, t.root).info)