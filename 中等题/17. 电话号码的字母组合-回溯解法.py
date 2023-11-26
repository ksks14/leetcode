from typing import List

# 时间复杂度 O(3^m*4^n)

class Solution:

    def __init__(self) -> None:
        self.phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        def circle(current_str: str, num: str):
            if not num:
                res.append(current_str)
            else:
                for char in self.phone[num[0]]:
                    circle(current_str + char, num[1:])

        circle('', digits)
        return res

