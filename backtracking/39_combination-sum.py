class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(s,path):
            if s>=target:
                path.sort()
                if s==target and path not in res:
                    res.append(path)
                return
            for i in range(len(candidates)):                
                helper(s+candidates[i],path+[candidates[i]])
        helper(0,[])
        return res
