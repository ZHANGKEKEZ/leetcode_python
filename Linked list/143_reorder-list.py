# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            #计数
            count=0
            node=head
            while node:
                count+=1
                node=node.next
            #把链表分成两节   
            n=count//2-1
            two=head
            while n:
                two=two.next
                n-=1
            med=two.next
            two.next=None
            #反转第二节链表
            pre=None
            cur=med
            while cur:
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            #合并两节链表
            while head and pre:
                temp1=head.next
                temp2=pre.next
                head.next=pre
                if temp1:
                    pre.next=temp1
                head=temp1
                pre=temp2
            
