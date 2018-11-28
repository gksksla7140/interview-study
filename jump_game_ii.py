class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or nums[0] == 0 or len(nums) == 1:
            return 0
        
        i, ans = 0, 0
        while i < len(nums)-1:
            # If we can jump to the end from this position directly, return ans+1
            if i + nums[i] >= len(nums)-1:
                return ans+1
            
            # Select next position based on the expected position idx+nums[idx]
            curr_idx, tmp_max = 0, 0
            for idx, n in enumerate(nums[i:i+nums[i]+1]):
                if n+idx >= tmp_max:
                    curr_idx, tmp_max = idx, n+idx
            
            if curr_idx == 0:
                i += nums[i]
            else:
                i += curr_idx
            ans += 1
        return ans