class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s_list = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and s_list[left] not in letters:
                left += 1
            while right > left and s_list[right] not in letters:
                right -= 1
            s_list[left] , s_list[right] = s_list[right], s_list[left]
            right -= 1
            left += 1
        
        return ''.join(s_list)
