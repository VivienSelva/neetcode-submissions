class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        word1=strs[0]
        for i in range(len(word1)):
            for words in strs[1:]:
                if i == len(words) or word1[i]!=words[i]:
                    return res
                    break
            else:
                res+=word1[i]
                continue
        return res