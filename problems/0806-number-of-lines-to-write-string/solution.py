class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        n_lines = 1
        line_length = 0

        for char in s:
            char_width = widths[ord(char)-97]

            if line_length + char_width > 100:
                line_length = char_width
                n_lines += 1
            else:
                line_length += char_width

        return n_lines, line_length