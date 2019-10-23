class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        dp=[[sys.maxsize]*(n+1) for _ in range(m+1)]
        dp[0][1]=0
        dp[1][0]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        return dp[-1][-1]
     
/*
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/        
