class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        i = 1
        while(i < len(nums)):
            if(nums[i] != nums[index-1]):
                nums[index] =  nums[i]
                index = index + 1
            i += 1
        return index
       
