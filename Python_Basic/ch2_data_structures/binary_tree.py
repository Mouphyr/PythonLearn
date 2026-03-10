class Node:
    def __init__(self, val=-1,lchild=None,rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue=[] #辅助队列

    def level_built_tree(self,node:Node):
        if self.root is None:
            self.root=node
            self.help_queue.append(node)
        else: #左孩子为空，则变为左孩子；否则变为右孩子，并将该结点出队
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild=node
            else:
                self.help_queue[0].rchild=node
                self.help_queue.pop(0)

    def pre_order(self,cur_node:Node): # 前序遍历（深度优先遍历）
        if cur_node is None:
            return
        print(cur_node.val,end=' ')
        self.pre_order(cur_node.lchild)
        self.pre_order(cur_node.rchild)

    def in_order(self, cur_node: Node):  # 中序遍历
        if cur_node is None:
            return
        self.in_order(cur_node.lchild)
        print(cur_node.val, end=' ')
        self.in_order(cur_node.rchild)

    def post_order(self, cur_node: Node):  # 后序遍历
        if cur_node is None:
            return
        self.post_order(cur_node.lchild)
        self.post_order(cur_node.rchild)
        print(cur_node.val, end=' ')

    def level_order(self, cur_node: Node): #层序遍历（广度优先遍历）
        help_queue=[]
        help_queue.append(cur_node)
        while help_queue:
            cur_node=help_queue.pop(0)
            print(cur_node.val,end=' ')
            if cur_node.lchild:
                help_queue.append(cur_node.lchild)
            if cur_node.rchild:
                help_queue.append(cur_node.rchild)

if __name__ == '__main__':
    tree=BinaryTree()
    for i in range (1,11):
        tree.level_built_tree(Node(i)) #将结点放入树中
    tree.pre_order(tree.root) #对完全二叉树进行前序遍历
    print()
    tree.in_order(tree.root)
    print()
    tree.post_order(tree.root)
    print()
    tree.level_order(tree.root)
    print()