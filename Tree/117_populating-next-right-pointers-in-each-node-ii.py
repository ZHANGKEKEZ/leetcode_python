"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return root
        if root.left:
            if root.right:
                root.left.next=root.right                
            else:
                root.left.next=self.findnext(root.next)
        if root.right:
            root.right.next=self.findnext(root.next)
        #先右子树，后左子树，应为findnext方法里面是从左往右找的，需要先把右边构造好
        self.connect(root.right)
        self.connect(root.left)
        #最后返回root
        return root
    
    
    def findnext(self,node):
        while node:
            if node.left:return node.left
            if node.right:return node.right
            node=node.next        
        return None
/*
给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

提示：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/      
