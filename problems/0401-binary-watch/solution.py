class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Filter all times
        return [f"{h}:{mm:02d}" for h in range(12) for mm in range(60) if h.bit_count() + mm.bit_count() == turnedOn]