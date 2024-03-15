from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip_addresses = []

        def helper(s, ip_addr, dots_left):
            # base case
            if dots_left == 0:
                if len(s) == 0:
                    new_ip = ip_addr.rstrip(".")
                    if new_ip not in ip_addresses:
                        ip_addresses.append(new_ip)
                return

            branches_left = 3
            while branches_left > 0:

                i = s[:branches_left]
                new_s = s[branches_left:]
                branches_left -= 1

                # ip address range validity check [0, 255]
                if i == "" or (i[0] == "0" and len(i) > 1) or int(i) > 255:
                    continue

                new_ip_addr = f"{ip_addr}{i}."
                helper(new_s, new_ip_addr, dots_left - 1)

        helper(s, "", 4)
        return ip_addresses
