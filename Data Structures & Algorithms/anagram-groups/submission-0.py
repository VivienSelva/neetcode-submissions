class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for word in strs:
            num=[0]*26
            for letters in word:
                num[ord(letters)-ord("a")]+=1
            dict[tuple(num)].append(word)
        return list(dict.values())