from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def traverse(
            dist_counter,
            node,
            prev,
            min_distance,
            max_distance,
            first_local_extrema,
            last_local_extrema,
        ):
            if node is None:
                if first_local_extrema == last_local_extrema:
                    return -1, -1
                return min_distance, max_distance

            if (
                prev is not None
                and node.next is not None
                and (
                    (prev.val < node.val and node.val > node.next.val)
                    or (prev.val > node.val and node.val < node.next.val)
                )
            ):
                # is local extrema
                if first_local_extrema is None:
                    return traverse(
                        dist_counter + 1,
                        node.next,
                        node,
                        min_distance,
                        max_distance,
                        dist_counter,
                        dist_counter,
                    )
                else:
                    max_distance = max(max_distance, dist_counter - first_local_extrema)
                    min_distance = min(
                        min_distance, max_distance, dist_counter - last_local_extrema
                    )
                    return traverse(
                        dist_counter + 1,
                        node.next,
                        node,
                        min_distance,
                        max_distance,
                        first_local_extrema,
                        dist_counter,
                    )
            else:
                return traverse(
                    dist_counter + 1,
                    node.next,
                    node,
                    min_distance,
                    max_distance,
                    first_local_extrema,
                    last_local_extrema,
                )

        return list(traverse(0, head, None, 10e5, 0, None, None))
