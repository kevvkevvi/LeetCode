class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        output = 0
        prev = 1000
        for rom in s:
            if table[rom] <= prev:
                output += table[rom]
            else:
                output += table[rom] - 2*prev
            prev = table[rom]
        return output