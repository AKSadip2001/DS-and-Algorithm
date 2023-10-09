class Queue:
    def __init__(self):
        self.queue = []
        self.n=100

    def enqueue(self, int):
        if(len(self.queue)==self.n):
            print("Queue is full")
            return
        self.queue.append(int)
        print(str(int)+" added to Queue")
    
    def dequeue(self):
        if(len(self.queue)==0):
            print("No elements in queue to remove")
            return
        print(str(self.queue.pop(0))+" removed from the queue")
    
    def printQueue(self):
        if(len(self.queue)==0):
            print("No elements in queue")
            return
        for elem in self.queue:
            print(elem, end=" ")
        print()


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.printQueue()

queue.dequeue()

queue.printQueue()
