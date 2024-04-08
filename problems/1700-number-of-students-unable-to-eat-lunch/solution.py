from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """Brute force (O(n*m))"""
        students = deque(students)

        has_more_students = True
        while has_more_students:
            if sandwiches[0] == students[-1]:
                sandwiches.pop(0)
                students.pop()
                has_more_students = len(students) > 0
            else:
                max_rotations = len(students)
                found = False
                for _ in range(max_rotations):
                    if students[-1] == sandwiches[0]:
                        found = True
                        break
                    else:
                        students.appendleft(students.pop())

                has_more_students = found

        return len(sandwiches)

    def countStudents2(self, students: List[int], sandwiches: List[int]) -> int:
        """O(n)"""
        students_per_sandwich = [0, 0]
        for student in students:
            students_per_sandwich[student] += 1

        for i, sandwich in enumerate(sandwiches):
            students_per_sandwich[sandwich] -= 1
            if students_per_sandwich[sandwich] < 0:
                return len(sandwiches) - i

        return 0
