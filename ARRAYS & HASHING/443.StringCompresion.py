class Solution:
    def compress(self, chars: List[str]) -> int:
        write_pos = 0
        count = 0

        i = 0
        while i < len(chars):
            count = 0
            c = chars[i]

            while i < len(chars) and chars[i] == c:
                count += 1
                i += 1
            
            chars[write_pos] = c
            write_pos += 1

            if count > 1:
                for char in str(count):
                    chars[write_pos] = char
                    write_pos += 1

        return write_pos  
        


