class newNode:
    def __init__(self,item):
        self.key=item
        self.left=self.right=None
        self.parent=None
def insert(node, key):
    if node == None:
        return newNode(key)

    if key < node.key:
        lchild = insert(node.left, key)
        node.left = lchild

        lchild.parent = node
    elif key > node.key:
        rchild = insert(node.right, key)
        node.right = rchild

        rchild.parent = node

    return node

def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.key, end = "")
        inorder(root.right)

def postorder(root):
    if (root != None):
        inorder(root.right)
        inorder(root.left)
        print(root.key, end = "")

def preorder(root):
    if (root != None):
        print(root.key, end = "")
        inorder(root.left)
        inorder(root.right)

def maxmin(root):
    while ((root.right)!=None):
        root=root.right
    print("max",root.right)
    root=root
    while((root.left)!=None):
        root=root.left
    print("min",root.left)

if __name__ == '__main__':
    root=None
    while True:
        print("\n 1. insert\n 2. inorder\n 3. postorder\n 4. preorder\n 5. max and min  \n 0. exit")
        a=int(input("enter your coice : "))
        if a==1:
            i=int(input("enter the element to be inserted : "))
            insert(root,i)
        elif a==0:
            exit()
        elif a==2:
            inorder(root)
        elif a==3:
            postorder(root)
        elif a==4:
            preorder(root)
        elif a==5:
            maxmin(root)

        else:
            print("\n wrong choice..!!")
