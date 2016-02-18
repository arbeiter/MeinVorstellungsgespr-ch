'''ListOperations.py
'''
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

    def insert(sel6 f, data):
        noder = ListNode(data)
        print("about to insert"+str(noder.val))
        if self.head == None:
            self.head = noder
        else:
            noder.next = self.head
            self.head = noder

    def find_Cycles(self):
        first_ptr = self.head
        #iterate
        # 1 -> 3 -> 5 -> 8 ->   10
        #                       V
        #      ^ .      .. .<-  9     
        return

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
        print("value not in list")

def main():

    lister = List(None)
    lister.print_list()
    
    #Test 1
    #insert 1, 2
    #print: 2 1
    lister.insert(1)
    lister.print_list()
    
    #Test 2
    #for i in 1 to 10
    #print list
    for i in range(10):
        lister.insert(i)
    lister.print_list()
    #insert into value

    for i in range(10):
        lister.remove_val(i)
    lister.print_list()

if __name__ == '__main__':
    main()
