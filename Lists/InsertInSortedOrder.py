#Insert into linked list in sorted order

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):

    def __init__(self, val):
        if val==None:
            self.head = None
        else:
            self.head = ListNode(val)

    def insert(self, data):
        noder = ListNode(data)
        print("about to insert"+str(noder.val))

        if self.head == None:
            self.head = noder
        else:
            noder.next = self.head
            self.head = noder

    def get_head(self):
        return self.head
    
    def print_list(self):
        curr = self.head
        if curr == None:
          print("Empty list")
          return
        while curr!=None:
            print(str(curr.val), end=" ")
            curr = curr.next
        print()

    def remove_val(self, val):
        prev = self.head
        cur = self.head.next

        if prev == None:
            print("Deletion from empty list not allowed")

        if val == prev.val:
            self.head=self.head.next
            return

        while(prev.next!=None):
            if cur.val == val:
                prev.next = cur.next
                return
            prev = prev.next
            cur = prev.next                

    def insert_sorted(self, val):
        temp = ListNode(val)
        curr = self.head
        if val<=curr.val:
            temp.next = curr
            self.head = temp
            return

        prev = curr
        while prev.next!=None:
            if prev.val < temp.val and temp.val <= curr.val:
                temp.next = curr
                prev.next = temp
                return
            prev = prev.next
            curr = prev.next

        if prev!=None:
            prev.next = temp
        return
    
    def isListSorted(self):
        curr = self.head
        prev = self.head
        while curr!=None:
            if prev.val > curr.val:
                print("Out of place")
                return False
            prev = curr
            curr = curr.next
        return True

def main():
    lister = List(None)
    lister.print_list()
    
    #Test 1
    #insert 1, 2
    #print: 2 1
    lister.print_list()
    
    #Test 2
    #for i in 1 to 10
    #print list
    for i in range(10,0,-1):
        lister.insert(i)
    lister.print_list()

    print(lister.isListSorted())
    lister.insert_sorted(10)
    lister.insert_sorted(3)
    lister.insert_sorted(1)
    lister.print_list()

    testList1= List(None)
    testList1.insert(1)
    testList1.insert_sorted(0)
    assert(testList1.isListSorted()==True)

    testList2= List(None)
    testList2.insert(1)
    testList2.insert_sorted(2)
    assert(testList2.isListSorted()==True)

if __name__ == '__main__':
	main()
