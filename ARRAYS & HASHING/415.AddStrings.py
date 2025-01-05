class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1 , s2 = len(num1)-1 , len(num2)-1
        num1 = list(num1)
        num2 = list(num2)
        s1 , s2 = len(num1)-1 , len(num2)-1
        output = []
        carry = 0
        while s1 >= 0 and s2 >= 0:
            output.append( str((int(num1[s1]) + int(num2[s2])+carry)%10))
            carry = (int(num1[s1]) + int(num2[s2])+carry)//10
            s1 -= 1
            s2 -= 1
        
        while s1 >= 0:
            output.append(str((int(num1[s1]) +carry)%10))
            carry = (int(num1[s1]) +carry)//10
            s1 -= 1

        while s2 >= 0:
            output.append(str((int(num2[s2]) +carry)%10))
            carry = (int(num2[s2]) +carry)//10
            s2 -= 1

        if carry:
            output.append(str(carry))
        
        output.reverse()

        return ''.join(output)

