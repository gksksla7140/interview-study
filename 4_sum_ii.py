class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        first = collections.defaultdict(int)
        second = collections.defaultdict(int)
        counter = 0
        for a in A:
            for b in B:
                first[a + b] += 1
        
        for c in C:
            for d in D:
                second[c + d] += 1
        for fir in first:
            if 0 - fir in second:
                counter += first[fir] * second[0 - fir]
        
        return counter 