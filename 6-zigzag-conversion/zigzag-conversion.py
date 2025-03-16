from collections import defaultdict

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s  

        rows = defaultdict(list)
        mode = 1  
        j = 0  
        
        for char in s:
            rows[j].append(char)
            
            if j == 0:
                mode = 1  
            elif j == numRows - 1:
                mode = -1  
            
            j += mode

        
        output = []
        for k in range(numRows):
            output.extend(rows[k])

        return ''.join(output)
