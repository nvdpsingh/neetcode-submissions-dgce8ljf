class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        l1 = heapq.nlargest(k,nums)
        return l1[k-1]