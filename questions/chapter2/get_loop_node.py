class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

def GetLoopNode(head):
    if head==None or head.__next__==None or head.next.__next__==None:
        return None
    n1=head.__next__
    n2=head.next.__next__
    while n1!=n2:
        if n2.__next__==None or n2.next.__next__==None:
            return None
        n2=n2.next.__next__
        n1=n1.__next__
    n2=head
    while n1!=n2:
        n1=n1.__next__
        n2=n2.__next__
    return n1

#1->2->3->4->5->6->7->4...
head1 = Node(1)
head1.next =Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next = head1.next.next.__next__

print(GetLoopNode(head1).value)


