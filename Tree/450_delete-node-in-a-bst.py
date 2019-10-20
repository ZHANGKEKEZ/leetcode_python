# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if not root.left :           
            return root.right

        if not root.right :            
            return root.left

        #既有左子树，又有右子树
        #找到左子树中最大的叶子
        predecessor = self.__maximum(root.left)
        root.val=predecessor.val
        #删除左子树中最大的叶子
        root.left = self.__remove_max(root.left)
        return root

    def __remove_max(self, node):
        if not node.right:            
            return node.left
        node.right = self.__remove_max(node.right)
        return node

    def __maximum(self, node):
        while node.right:
            node = node.right
        return node

/*
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

    首先找到需要删除的节点；
    如果找到了，删除它。

说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
