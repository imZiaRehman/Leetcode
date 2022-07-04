class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window_start, longest_subarray, zero_count = 0, 0,0
        
         
        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[window_start] == 0:
                    zero_count -= 1
                window_start += 1
            longest_subarray = max(longest_subarray, window_end -  window_start)
        
        return longest_subarray
            