class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if nums[i] == 0:
                can = False
                j = i
                while 0 <= j:
                    if j+nums[j] >= len(nums) -1 or j + nums[j] > i:
                        can = True
                        break
                    j -= 1
                if can == False:
                    return False
        return True
                    
                  