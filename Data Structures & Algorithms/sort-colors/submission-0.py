class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        t = 0

        for key in range(3):
            while count[key] > 0:
                nums[t] = key
                t += 1
                count[key] -= 1
      
