class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Input: [1,1,2,3,3,4,4,8,8]
        Output: 2

        """
        l,r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)/2
            if mid % 2 == 0:
                if nums[mid] != nums[mid -1]:
                    # we know left side is all good 
                    l = mid
                else:
                    r = mid 
            else:
                if nums[mid] == nums[mid - 1]:
                    l= mid + 1
                else:
                    r = mid - 1
        return nums[l]
            

        
        