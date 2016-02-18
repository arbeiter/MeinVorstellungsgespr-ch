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
