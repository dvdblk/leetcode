class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

    def countSegments2(self, s: str) -> int:
        # use a flag to indicate whether we are inside a segment
        n_segments = 0
        inside_segment = False
        for ch in s:
            if ch != " ":
                if not inside_segment:
                    inside_segment = True
            else:
                if inside_segment:
                    inside_segment = False
                    n_segments += 1

        # check if we should add segment if last character wasn't a space
        if inside_segment:
            n_segments += 1

        return n_segments