class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = len(nums)
        current_index = x-1
        square = [0 for x in range(x)]
        
        start_ptr, end_ptr = 0, x-1
        for i in range(x):
            if(nums[start_ptr] * nums[start_ptr] > nums[end_ptr]*nums[end_ptr]):
                square[current_index] = nums[start_ptr] * nums[start_ptr]
                start_ptr += 1
            else:
                square[current_index] = nums[end_ptr]*nums[end_ptr]
                end_ptr -= 1
            current_index -= 1
        
        return square
