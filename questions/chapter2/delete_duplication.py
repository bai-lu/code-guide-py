# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        new_head=pHead
        tmp=new_head
        pHead=pHead.__next__
        while pHead!=None:
            if tmp.val==pHead.val:
                tmp.next=pHead.__next__
                pHead=pHead.__next__
            else:
                tmp.next=pHead
            tmp=tmp.__next__
            pHead=pHead.__next__
        return new_head
    def deleteDuplicationAll(self, pHead):
        if pHead==None:
            return None
        flag=0
        l=[pHead]    # 借助栈实现
        tmp=pHead
        pHead=pHead.__next__
        while pHead!=None:
            if pHead.val==tmp.val:
                if flag==0:
                    tmp=l.pop()
                    flag=1
            else:
                l.append(pHead)
                tmp=l[-1]
                flag=0
            pHead=pHead.__next__
        if len(l)==0:    #防止链表全为同一元素的情况
            return None
        head=l[0]
        tmp=head
        for i in l[1:]:    # 重构链表
            tmp.next=i
            tmp=tmp.__next__
        tmp.next=None
        return head


    def print_List(self,head):
        while head!=None:
            print((head.val))
            head=head.__next__

# 1 2 2 3 3 5
head=ListNode(2)
head.next=ListNode(2)
head.next.next=ListNode(2)
head.next.next.next=ListNode(2)
# head.next.next.next.next=ListNode(3)
# head.next.next.next.next.next=ListNode(5)
s=Solution()
#new_head=s.deleteDuplication(head)
# s.print_List(new_head)
# 1 2 3 5
new_head=s.deleteDuplicationAll(head)
s.print_List(new_head)

