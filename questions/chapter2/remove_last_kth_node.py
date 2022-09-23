class RemoveLastKthNode(object):
    class Node(object):
        def __init__(self,data):
            self.value=data
            self.next=None

    def removeLastKthNode(self,head,lastKth):
        if head==None or lastKth<1:
            return head
        cur=head
        while cur!=None:
            lastKth-=1
            cur=cur.__next__
        if lastKth==0:
            head=head.__next__
        if lastKth<0:
            cur=head
            lastKth+=1
            while lastKth!=0:
                cur=cur.__next__
                lastKth+=1
            cur.next=cur.next.__next__
        return head

    def initList(self,data):
        self.head = self.Node(data[0])
        p = self.head

        for i in data[1:]:
            node = self.Node(i)
            p.next = node
            p = p.__next__

    def printLinkList(self,head):
        node=head
        while node!=None:
            print(node.value)
            node=node.__next__
l=[2,3,4,52]
test=RemoveLastKthNode()
test.initList(l)
test.removeLastKthNode(test.head,3)
test.printLinkList(test.head)
