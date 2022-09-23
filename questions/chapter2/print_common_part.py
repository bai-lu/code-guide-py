class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class PrintCommonPart(object):
    def printCommonPart(self,head1,head2):
        print("Common Part: ")
        while head1!=None and head2!=None:
            if head1.value<head2.value:
                head1=head1.__next__
            elif head1.value>head2.value:
                head2=head2.__next__
            else:
                print((head1.value))
                head1=head1.__next__
                head2=head2.__next__

    def printLinkedList(self,node):
        print("Linked List: ")
        while node!=None:
            print((node.value))
            node=node.__next__
        print()
    def initList(self,data1,data2):
        self.head1 = Node(data1[0])
        self.head2 = Node(data2[0])
        p = self.head1

        for i in data1[1:]:
            node = Node(i)
            p.next = node
            p = p.__next__

        p = self.head2
        for i in data2[1:]:
            node = Node(i)
            p.next = node
            p = p.__next__


l=[3,4,5,6,9]
ll=[5,6,9]
comm=PrintCommonPart()
comm.initList(l,ll)
comm.printLinkedList(comm.head1)
comm.printCommonPart(comm.head1,comm.head2)
