# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/944768433/

VOWELS = ['a', 'e', 'i', 'o', 'u']

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        answer = 0
        for i in range(min(k, len(s))):
            if s[i] in VOWELS:
                answer += 1
        
        current = answer

        left = 0
        right = k

        while right < len(s):
            if s[left] in VOWELS:
                current -= 1
            if s[right] in VOWELS:
                current += 1
            
            answer = max(answer, current)
            left += 1
            right += 1
    
        return answer
