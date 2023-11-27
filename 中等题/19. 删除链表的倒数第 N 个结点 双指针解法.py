from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 长度的指针，用于计算具体需要遍历到第几个
        len_node = ListNode(next=head)
        for _ in range(n):
            len_node = len_node.next
        
        # 获取到长度的指针后，通过同时遍历计算长度的指针与头结点，获取到需要删除的节点的位置
        res_node = fin_res = ListNode(next=head)
        while len_node.next:
            len_node = len_node.next
            res_node = res_node.next

        res_node.next = res_node.next.next

        return fin_res.next