class Solution:
    def alternatingSubarray(self, nums) -> int:
        def left_to_right_alternating_subarray_length(numbers):
            a = -1
            for i in range(1, len(numbers)):
                if numbers[i] - numbers[i-1] == (-1) ** (i + 1):
                    a = i + 1
                else:
                    break
            return a
        
        result = -1
        while result < len(nums) and len(nums) > 0:
            new_result = left_to_right_alternating_subarray_length(nums)
            if new_result > result:
                result = new_result
            nums.pop(0)
        
        return result

s = Solution()
print(s.alternatingSubarray([2,3,4,3,4]))
print(s.alternatingSubarray([42,43,44,43,44,43,44,45,46]))
