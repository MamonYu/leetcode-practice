class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        self.nums = nums
        self.target = target
        i = 0
        j = 1

        for x in nums:
            if nums[i] + nums[j] == target:
                return nums[i , j]
            else if nums[i += 1] + nums[j += 1] == target:
                return nums[i += 1 , j += 1]
        
sol = Solution()     
