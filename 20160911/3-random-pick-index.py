class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.c = collections.Counter(nums)
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        q = 0
        c = self.c[target]
        n = random.randint(1, c)
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                q += 1
                if q == n: return i

