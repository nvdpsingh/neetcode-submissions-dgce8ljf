class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def backtrack(i,path_sum):
                #base case
                if path_sum==target:
                    res.append(sol[:])
                    return
                #prune
                if path_sum > target or i == len(nums):
                    return

                #dont pick
                backtrack(i+1,path_sum)

                #pick
                sol.append(nums[i])
                backtrack(i,path_sum+nums[i])
                sol.pop()
        backtrack(0,0)
        return res