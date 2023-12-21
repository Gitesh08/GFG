from typing import List

class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        meeting = [[i+1, S[i], F[i]] for i in range(N)]
        meeting.sort(key = lambda i:i[2])
        temp, res = meeting[0], [meeting[0][0]]
        for i in meeting[1:]:
            if temp[2]<i[1]: temp, res = i, res+[i[0]]
        return sorted(res)
