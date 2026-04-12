class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums1 = nums
        heapq.heapify(nums)
        while len(self.nums1)> k:
            heapq.heappop(self.nums1)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums1,val)
        if len(self.nums1)>self.k:
            heapq.heappop(self.nums1)
        return self.nums1[0]        
