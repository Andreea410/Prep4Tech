# (* Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length *)  
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        vowels = set("aeiou")
        s = list(s)
        maximum = 0
        left , right = 0 , k-1
        count = 0
        for i in range(left , right+1):
            if s[i] in vowels:
                count+=1
        if count == k:
            return k
        if count > maximum:
            maximum = count

        while right < len(s)-1:
            if s[left] in vowels:
                count -=1
            left +=1
            right +=1
            if s[right] in vowels:
                count+=1
            if count == k:
                return k
            if count > maximum:
                maximum = count
        
        return maximum

        
        
