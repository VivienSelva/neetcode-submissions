class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        dict=defaultdict(int)
        total=0
        i=0
        sublist=[]
        for j in range(len(nums)):
            if nums[i]!=nums[j]:
                total=0
                i=j
            total+=1
            dict[nums[i]]=total
        for key,value in dict.items():
            sublist.append([value, key])
                
        sublist.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(sublist[i][1])

        return result
 


                