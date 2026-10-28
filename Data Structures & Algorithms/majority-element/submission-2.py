class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        MaxSize=len(nums)//2
        dict=defaultdict(int)
        for val in nums:
            dict[val]+=1
            if dict[val]> MaxSize:
                return val 