class TreeNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

class BST:
    def __init__(self):
        self.root=None
    def insert(self,num):
        if self.root is None:
            self.root=TreeNode(num)
        else:
            self._insert(self.root,num)
    def _insert(self,node,num):
        if num<=node.val:
            if node.left is None:
                node.left=TreeNode(num)
            else:
                self._insert(node.left,num)
        else:
            if node.right is None:
                node.right=TreeNode(num)
            else:
                self._insert(node.right,num)
def inorder(root):
        if root: 
            inorder(root.left)
            print(root.val,end=" ")
            inorder(root.right)
def preorder(root):
        if root: 
            print(root.val,end=" ")
            preorder(root.left)
            preorder(root.right)
def postorder(root):
        if root: 
            postorder(root.left)
            postorder(root.right)
            print(root.val,end=" ")
def create_bst_from_input():
    bst=BST()
    elements=input("Enter elements to insert into BST, seperated by space ").split()
    elements=list(map(int,elements))
    for i in elements:
        bst.insert(i)
    print("Inorder is: ",end=" ")
    inorder(bst.root) 
    print("Preorder is: ",end=" ")
    preorder(bst.root)
    print("Postorder is: ",end=" ")
    postorder(bst.root)
    print("Height of BST is: ",end=" ")
    print(height(bst.root))
    key=int(input("Enter the number to search: "))
    if _search(bst.root,key):
        print("Element is found ")
    else:
        print("Element is not found ")
    return bst
def height(root):
    if root is None:
        return 0
    leftheight=height(root.left)
    rightheight=height(root.right)
    return (max(leftheight,rightheight)+1)
def _search(root,num):
    if root is None:
        return None
    if num==root.val:
            return root
    if num<root.val:
            return _search(root.left,num)
    else:
        return _search(root.right,num)
create_bst_from_input()
