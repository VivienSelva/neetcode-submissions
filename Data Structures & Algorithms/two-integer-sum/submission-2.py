class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab={}
        for i in range(len(nums)):
            if target < nums[i]:
                pass 
            value=target-nums[i]
            if nums[i] in tab:
                return [tab[nums[i]],i]
            tab[value]=i