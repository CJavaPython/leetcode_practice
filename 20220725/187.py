from typing import List
# 187.Repeated DNA Sequences
# A, C, G, T
# repeat at least two times = repeated DNA
# return : all repeated DNA (nucleotide) sequence
        # HASH direct implement?
        # 소수로 지정
        # 결과값 소수로 찾기 == 천재.
        # 최적화의 신
        # 소수 값 차이는 크게.
        # rolling hash?
class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = list()
        #if len(s)<10: # exception
        dna = {}
        tf = False
        for i in range(len(s)-9):
            tenseq = s[i:i+10]
            tenseq = ''.join(tenseq)
            dna[tenseq] = dna.get(tenseq, 0) + 1
        for key in dna:
            if dna[key]>=2:
                result.append(key)
        return result
s = Solution()
print(s.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
