### Note: You must not use any built-in BigInteger library or convert the inputs to integer directly. ###
## str함수는 괜찮은듯?

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numbers = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        int_num1 = 0
        int_num2 = 0
        for num in num1:
            int_num1 = int_num1 * 10 + numbers[num]
        for num in num2:
            int_num2 = int_num2 * 10 + numbers[num]
        return str(int_num1 * int_num2)

s = Solution()


print(s.multiply("123", "456"))