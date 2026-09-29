class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def isEqual(value: str)->dict:
            tab={}
            for i in range(len(s)):
                if value[i] in tab:
                    tab[value[i]]+=1
                else:
                    tab[value[i]]=1
            return tab          
        if len(s)!=len(t):
            return False
        else:
            return isEqual(s)==isEqual(t)

               
