class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)

def Sortlist(T,L):
    if T.isLeaf:
        for i in range(len(T.item)):
            L.append(T.item[i])#leaf
    else:
        for j in range(len(T.item)):
            Sortlist(T.child[j], L)
            L.append(T.item[j])#the node
        Sortlist(T.child[len(T.item)], L)#all the leaf
    return L

def MinAtDepth(T, d): 
    if T.isLeaf and d != 0:
        return False
    elif d == 0:
        return T.item[0]
    else:
        return MinAtDepth(T.child[0], d-1)

def MaxAtDepth(T,d): 
    if T.isLeaf and d != 0:
        return False
    elif d == 0:
        return T.item[-1]
    else:
        return MaxAtDepth(T.child[-1], d-1)


def NumOfNodes(T,d):
    if T.isLeaf and d != 0:
        return False
    elif d == 0:
        return 0
    elif d != 0:
        for i in range(len(T.item)+1):
            return PrintHeight(T.child[i],d-1)+1



def PrintHeight(T,d):
    if T.isLeaf and d != 0:
        return False
    elif d == 0:
        print(T.item)
    elif d == 1:
        for i in range(len(T.item)+1):
            print(T.child[i].item)
    elif d != 0 or d != 1:
        for i in range(len(T.item)+1):
            PrintHeight(T.child[i],d-1)

"""              
def NumofNode(T):   
    if IsFull(T):
        return 0
    else:
        for i in range(len(T.item)):
            return NumofNode(T.child[i]) + 1

"""

def NumofNode(T): 
    if T.isLeaf:
        return 0
    else:
        count = 0
        for i in range(len(T.item)):
            count += 1+NumofNode(T.child[i])
        return count


def NumofLeaves1(T):
    if T.isLeaf:
        return 1
    else:
        for i in range(len(T.item)):
            return NumofLeaves(T.child[len(T.item)])


def KeyAtDepth(T, k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return 1 + KeyAtDepth(T.child[len(T.item)], k)



#L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11, 3, 4, 5, 105, 115, 200, 2, 45, 6]
L = [20,50,78,23,54,95,7,55,23,44,15,74,110,120,152,236,204,153,54,78,91]
#L = [20,50,78,23,54]
T = BTree()
for i in L:
    #print('Inserting', i)
    Insert(T, i)
    #PrintD(T, '')
    #Print(T)
    #print('\n####################################')
Print(T.child[0])

print(T.child[0].child[0].item)

for i in range(len(T.item)+1):
    print(T.child[i].item)
    
print('height', height(T))
list = []
print(Sortlist(T, list))
print('minimum', MinAtDepth(T,1))
print('maximum ', MaxAtDepth(T,1))
#print(NumOfNodes(T,2))
PrintHeight(T,2)
print(NumofNode(T))
print(NumofLeaves(T))
print(KeyAtDepth(T,3))

