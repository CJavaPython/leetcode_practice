# 20220927
"""
There are n dominoes in a line, and we place each domino vertically upright. In 
the beginning, we simultaneously push some of the dominoes either to the left or
 to the right.

After each second, each domino that is falling to the left pushes the adjacent 
domino on the left. Similarly, the dominoes falling to the right push their 
adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays 
still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino 
expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.
"""

class Solution:
    # two pointer?
    def pushDominoes(self, dominoes: str) -> str:
        left = list()
        right = list()
        result = list()
        r_power = 0
        l_power = 0
        for R in range(len(dominoes)):
            if dominoes[R]=="R":
                r_power+=1
            right.append(r_power)
        
        for L in range(len(dominoes)):
            l = len(dominoes)-1-L
            if dominoes[l]=="L":
                l_power-=1
            left.append(l_power)
        for i in range(len(dominoes)):
            if left[i]+right[i] == 0:
                result.append(".")
            elif left[i]+right[i] < 0:
                result.append("L")
            elif left[i]+right[i] > 0:
                result.append("R")

        print("left : ", left)
        print("right : ", right)
        return result

class Solution:
    # two pointer?
    def pushDominoes(self, dominoes: str) -> str:
        result=["."] * len(dominoes)
        r = -1
        l = -1
        for i in range(len(dominoes)):
            if dominoes[i]==".":
                continue
            elif dominoes[i]=="R":
                # find /
                r = i
                result[i]="R"
            elif dominoes[i]=="L":
                # if R exist
                if r != -1:
                    # ///\\\
                    if l-r - 1 % 2 == 0:
                        for j in range(l-r-1):
                            if j <= (l-r-1)//2:
                                result[j]="R"
                            else:
                                result[j]="L"
                        result[i]="L"
                        l = -1
                        r = -1
                    # //.\\
                    elif l-r - 1 % 2 == 1:
                        r_to_l = False
                        for j in range(l-r-1):
                            if j <= (l-r-1)//2:
                                result[j+1]="R"
                            elif r_to_l==False and j > (l-r-1)//2:
                                result[j+1]="."
                                r_to_l=True
                            else:
                                result[j]="L"
                        result[i]="L"
                        l = -1
                        r = -1
                # R not exist
                else:
                    result[i]="L"


        return result
        """
        dominoes = 'L' + dominoes + 'R'
        res = ""
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue
            middle = j - i - 1
            if i:
                res += dominoes[i]
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * middle
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle // 2) + '.' * (middle % 2) + 'L' * (middle // 2)
            i = j
        return res
        """




        
s = Solution()
print(s.pushDominoes(dominoes = "RR.L"))            # "RR.L"
print(s.pushDominoes(dominoes = ".L.R...LR..L.."))  # "LL.RR.LLRRLL.."
print(s.pushDominoes(dominoes = "RRR..L..."))