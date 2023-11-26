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
        if not digits:
            return []
        
        # 使用列表模拟队列
        queue = [""]

        # 遍历数据
        for num_char in digits:
            for _ in len(range(queue)):
                queue_head = queue.pop(0)
                for letter in self.phone[num_char]:
                    queue.append(queue_head + letter)

        return queue