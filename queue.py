# Dequeue. A double-ended queue or deque (pronounced “deck”) is a generalization
# of a stack and a queue that supports adding and removing items from either the
# front or the back of the data structure. Create a generic data type Deque that
# implements the following API:
class Item:
    def __init__(self, number):
        self.next = None
        self.prev = None
        self.value = number
    def __str__(self):
        return str(self.value)

# public class Deque<Item> implements Iterable<Item> {
class Deque:
#   // construct an empty deque
#   public Deque()
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printQueue(self):
        if self.head:
            cursor = self.head
            while cursor:
                print(cursor.value)
                cursor = cursor.next


#   // is the deque empty?
#   public boolean isEmpty()
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

#   // return the number of items on the deque
#   public int size()
    def sizeOf(self):
        return self.size

#   // add the item to the front
#   public void addFirst(Item item)
    def addFirst(self, item):
        if not self.head:
            self.head = item
            self.tail = item
            self.size += 1
        else:
            item.next = self.head
            self.head.prev = item
            self.head = item
            self.size += 1

#   // add the item to the back
#   public void addLast(Item item)
    def addLast(self, item):
        if not self.head:
            self.head = item
            self.tail = item
            self.size += 1
        else:
            item.prev = self.tail
            self.tail.next = item
            self.tail = item
            self.size += 1

#   // remove and return the item from the front
#   public Item removeFirst()
    def removeFirst(self):
        if not self.head:
            print("Deque is empty")
        else:
            self.head = self.head.next
            self.size -= 1

#   // remove and return the item from the back
#   public Item removeLast()
    def removeLast(self):
        if not self.tail:
            print("Deque is empty")
        else:
            
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1


item1 = Item(1)
item2 = Item(2)
item3 = Item(3)
item4 = Item(4)
item5 = Item(5)

deque = Deque()

deque.addLast(item1)
deque.addLast(item2)
deque.addLast(item3)
deque.addLast(item4)
deque.addLast(item5)

deque.printQueue()
deque.removeLast()

print("-------")
deque.printQueue()