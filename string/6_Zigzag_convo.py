class Solution:
    def convert(self, s: str, numRows: int) -> str:


        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows

        current = 0
        direction = 1
        
        for char in s :
            rows[current] += char

            if current == 0:
                direction = 1
            elif current == numRows -1:
                direction = -1
            current += direction
        return "".join(rows)
