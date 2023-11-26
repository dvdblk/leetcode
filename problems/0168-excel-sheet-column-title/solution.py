class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            # Subtract 1 because the base26 is moved by one
            columnNumber -= 1
            # Get the next nr and current remainder
            a = columnNumber // 26
            b = columnNumber % 26

            # Update letter
            res = chr(ord("A")+b) + res

            columnNumber = a

        return res