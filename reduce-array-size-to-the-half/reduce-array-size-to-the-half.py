class Solution:
    def minSetSize(self, A: List[int]) -> int:
        len_A, cnt_A = len(A), collections.Counter(A)
        sort_cnt = sorted(cnt_A.values(), reverse = True)
        sum_cnt = itertools.accumulate(sort_cnt)
        for i,v in enumerate(sum_cnt):
            if v >= len(A)//2: return i + 1

                