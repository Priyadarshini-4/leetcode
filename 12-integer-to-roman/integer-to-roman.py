class Solution:
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman = ""
        
        for i in range(len(val)):
            count = num // val[i]
            roman += symbols[i] * count
            num -= val[i] * count
            
        return roman
