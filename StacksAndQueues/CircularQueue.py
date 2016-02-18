class My_Queue:
    def __init__(self, max_len):
        self.buffer = [-1]*max_len
        self.max_len = max_len
        self.front = (int)(max_len/2)
        self.rear = (int)(max_len/2)

    def insert(self, data):
        if(self.isFull()):
            print("Can't do this your buffer's full")
        print("insert "+str(data) + " ")    
        self.rear = (self.rear + 1)%self.max_len
        self.buffer[self.rear] = data

    def delete(self):
        #check for emptiness condition
        if(self.isEmpty()):
            print("Can't delete from empty queue")
        #Remove the front element
        print("delete front from the queue", self.buffer[self.front])
        self.buffer[self.front] = -1
        self.front = (self.front + 1)%self.max_len

    def isFull(self):
        if self.front==(self.rear+1)%self.max_len:
            return True
        self.buffer[self.front] = -1
        return False

    def isEmpty(self):
        if self.buffer[self.front]==-1:
            return True
        return False

    def get_front(self):
        if self.front==-1:
            return None
        return self.buffer[self.front]

    def get_rear(self):
        if self.rear==-1:
            return None
        return self.buffer[len(self.rear)]

def main():
    myQueue = My_Queue(3)
    myQueue.insert(1)
    myQueue.insert(2)
    myQueue.insert(3)
    myQueue.insert(4)
    myQueue.delete()    
    myQueue.delete()    
    myQueue.delete()

if __name__ == '__main__':
	main()
