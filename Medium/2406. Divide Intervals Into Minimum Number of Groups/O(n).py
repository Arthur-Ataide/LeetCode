from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        final, grupos = 0, 0

        for start in start_times:
            if start > end_times[final]:
                final += 1
            else:
                grupos += 1

        return grupos