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
        print("value not in list")

    def mergeTwoLists(self, curr1, curr2):
        while curr1!=None and curr2!=None:
            return

def main():
    #insert into list 1
    l1 = List(-1)
    for i in range(0,9,2):
        l1.insert_sorted(i)
    l2 = List(-2)
    for i in range(1,9,2):
        l2.insert_sorted(i)
    l1.mergeTwoLists(l1.head, l2.head)
    #insert into list 2

if __name__ == '__main__':
    main()
