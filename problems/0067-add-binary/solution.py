class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Find the longer list
        longer, shorter = (a, b) if len(a) >= len(b) else (b, a)
        len_l = len(longer)

        # define a method that sums up chars and returns T/F based on whether to carry forward or not
        def add_chars(fst, snd):
            match (fst, snd):
                case "0", "0":
                    return "0", False
                case ("1", "0") | ("0", "1"):
                    return "1", False
                case "1", "1":
                    return "0", True

        # Output value
        out = ""
        # If the next pass should include +1
        carry_forward = False

        for i in range(len_l):
            # until we can iterate over both values
            if i < len(shorter):
                # sum them up
                new, new_carry_forward = add_chars(
                    longer[len_l - 1 - i], shorter[len(shorter) - 1 - i]
                )
                # check if previous carry_forward needs to be included
                if carry_forward:
                    # get final values
                    new, carry_forward = add_chars(new, "1")
                    carry_forward = carry_forward or new_carry_forward
                else:
                    carry_forward = new_carry_forward
                # updated output
                out = new + out
            else:
                # if we can only iterate over the rest of the longer number
                if carry_forward:
                    # if there is a leftover carry_forward value, make sure to include it
                    new, carry_forward = add_chars(longer[len_l - 1 - i], "1")
                else:
                    # only repeat the number until it's done
                    new = longer[len_l - 1 - i]
                out = new + out

        # case for last number needing a carry_forward
        if carry_forward:
            out = "1" + out
        return out
