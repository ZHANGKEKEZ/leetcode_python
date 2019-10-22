# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:return []
        nums=[i+1 for i in range(n)]
        def helper(nums):
            if not nums:             
                return [None]
            trees=[]
            for i in range(len(nums)):
                lefttrees=helper(nums[:i])
                righttrees=helper(nums[i+1:])                
                for l in lefttrees:
                    for r in righttrees:
                        root=TreeNode(nums[i])
                        root.left=l
                        root.right=r
                        trees.append(root)                
            return trees
        res=helper(nums)
        return res
/*
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/        
