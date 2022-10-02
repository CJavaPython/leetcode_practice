#20221001
"""
A message containing letters from A-Z can be encoded into numbers using the 
following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back 
into letters using the reverse of the mapping above (there may be multiple 
ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 
'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Mapping method find != unsequenced mapping
"""
print(str([i for i in range(27)]))
class Solution:
    def __init__(self):
        self.alphabet_nums = str([i for i in range(10,27)])
    def numDecodings(self, s: str) -> int:
        # if there if no search space
        if len(s)==0:
            print("len0")
            return 0
        # start with 0 (ex : 06)
        elif s[0]=="0":
            print("0 start")
            return 0
        # only one space left
        elif len(s)==1:
            print("len1")
            return 1

        # search one and two
        print("ones")
        print(s[0:1])
        ones=self.numDecodings(s[1:])
        print("ones result : ", ones, " ", s[1:])
        if s[0:2] in self.alphabet_nums:
            print("twos")
            print(s[0:2])
            twos=self.numDecodings(s[2:])
            print("twos result : ", twos, " ", s[2:])
            return ones+twos
        return ones

s = Solution()
print(s.numDecodings(s = "226"))
#print(s.numDecodings(s = "12"))


"""

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

2^100 or dp

"""


class Solution:
    def __init__(self):
        self.alphabet_nums = str([i for i in range(10,27)])
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s) + [1]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if 1 <= int(s[i:j+1])<=26:
                    dp[i]+=dp[j+1]
                else:
                    break
        return dp[0]