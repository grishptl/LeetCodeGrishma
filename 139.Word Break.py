"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        #dp of last char alz remains true
        dp[len(s)] = True
        
        #start from reverse string
        for i in range(len(s)-1, -1, -1):
            print(dp)
            #traverse each word in worddict
            for w in wordDict:
                #string from i to len(word) == word in dictionary
                if (len(w)+i) <= len(s) and s[i:len(w)+i] == w:
                    dp[i] = dp[i+len(w)]
                #No need to check further dictionary words if dp[i] becomes true
                if dp[i] == True:
                    break
        return dp[0]
