'''
author: Shayla Starr 
date: 2.14.2026 
hello there 
'''
 
class Stack: 
    def __init__(self): 
        self.list = []
 
    def push(self, item):
        self.list.append(item)
    
    def peek(self): 
        if self.is_empty(): 
            return None
        else:
            return self.list[-1]
    
    def size(self): 
        return len(self.list) 
    
    def pop(self): 
        if self.is_empty():
            return None
        return self.list.pop()
    
    def is_empty(self): 
        return len(self.list) == 0
 
 
class BinaryTree: 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None
 
    def get_root_val(self): 
        return self.key 
 
    def set_root_val(self, new_val): 
        self.key = new_val
 
    def get_left_child(self): 
        return self.left 
    
    def get_right_child(self):
        return self.right
    
    def insert_left(self, new_left): 
        new_tree = BinaryTree(new_left)
 
        if self.left is None: 
            self.left = new_tree
        else: 
            new_tree.left = self.left 
            self.left = new_tree
 
    def insert_right(self, new_right): 
        new_tree = BinaryTree(new_right)
 
        if self.right is None: 
            self.right = new_tree
        else: 
            new_tree.right = self.right
            self.right = new_tree
 
 
class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None
 
    def get_data(self): 
        return self.data 
    
    def get_next(self): 
        return self.next
    
    def set_next(self, newNext): 
        self.next = newNext
 
 
class UnorderedListStack():
    def __init__(self): 
        self.uls = UnorderedList()
 
    def push(self, item): 
        self.uls.add(item)
 
    def pop(self): 
        return self.uls.pop(0)
    
    def peek(self):
        item = self.uls.pop(0)
        self.uls.add(item)
        return item
 
    def size(self):
        return self.uls.length()
 
    def is_empty(self): 
        return self.uls.is_empty()
 
 
class UnorderedList(object): 
    def __init__(self): 
        self.head = None
 
    def add(self,item): 
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def remove(self, item):
        current = self.head
        previous = None
 
        while current != None:
            if current.get_data() == item: 
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            previous = current
            current = current.get_next()   # FIXED
    
    def search(self, item): 
        current_node = self.head
 
        while current_node != None:
            if item == current_node.get_data():
                return True
            current_node = current_node.get_next()
            
        return False 
    
    def is_empty(self): 
        return self.head == None
    
    def length(self):
        node_count = 0                  
        current = self.head     
        while current != None:         
            current = current.get_next()     
            node_count += 1                
        return node_count
 
    def append(self, item):
        new_node = Node(item)
 
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while current_node.get_next() != None: 
            current_node = current_node.get_next()
        
        current_node.set_next(new_node)
    
    def index(self, item):
        node_count = 0 
        current = self.head
 
        while current != None:
            if current.get_data() == item: 
                return node_count
            current = current.get_next()
            node_count += 1
    
    def insert(self, pos, item):
        new_node = Node(item)
 
        if pos == 0:
            self.add(item)
            return
 
        current = self.head
        previous = None
        count = 0
 
        while current != None:
            if count == pos:
                previous.set_next(new_node)
                new_node.set_next(current)
                return
 
            previous = current
            current = current.get_next()
            count += 1
 
    def pop(self, pos=None):
        if pos is None:
            current = self.head
            previous = None
 
            if current is None:
                return None
 
            while current.get_next() != None:
                previous = current
                current = current.get_next()
 
            if previous is None:
                self.head = None
            else:
                previous.set_next(None)
 
            return current.get_data()
 
        current = self.head
        previous = None
        count = 0
 
        while current != None:
            if count == pos:
                if pos == 0:
                    self.head = current.get_next()
                    return current.get_data()
                previous.set_next(current.get_next())
                return current.get_data()
 
            previous = current
            current = current.get_next()
            count += 1
 
 
 
class LinearSearcher:
 
    def search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return None
 
 
class BinarySearcher:
    def search(self, arr, target):
        low = 0
        high = len(arr) - 1
 
        while low <= high:
            mid = (low + high) // 2
 
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
 
        return None
    
 
 
 
 
class Queue: 
    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0
 
    def enqueue(self, item):
        new_node = Node(item)
 
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
 
        self.tail = new_node
        self.length += 1
        
    def dequeue(self): 
        if self.head is None:
            return None
        remove_node = self.head
        self.head = remove_node.next
        self.length -= 1
        return remove_node.data
 
 
 
class Deque(object): 
    def __init__(self):
        self.deque = []
 
    def add_front(self, item):
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)
 
    def peek_front(self): 
        if len(self.deque) > 0: 
            return self.deque[0]
        
    def peek_rear(self): 
        if len(self.deque) > 0: 
            return self.deque[-1]
 
 
 
class HashTable(object):
 
    def __init__(self, m): 
        self.m = m
        self.size = 0 
        self.keys = m * [None]
        self.values  = m * [None]
 
    def hash_function(self, key): 
        return key % self.m
 
    def put(self, key, value): 
        index = self.hash_function(key)
    
        while self.keys[index] != None: 
            if self.keys[index] == key: 
                self.values[index] = value
                return 
            index = (index + 1) % self.m
        
        self.keys[index] = key
        self.values[index] = value 
        self.size += 1
 
    def get(self, key): 
        index = self.hash_function(key)
        start = index
 
        while self.keys[index] is not None: 
            if self.keys[index] == key: 
                return self.values[index]
            
            index = (index + 1) % self.m
 
            if index == start: 
                break
 
        return None
    
    def __len__(self): 
        return self.size
    
    def __repr__(self): 
        return "Keys:\n" + str(self.keys) + "\nValues:\n" + str(self.values)

class BinaryHeap():
    """The BinaryHeap class implements the Binary Heap Abstract 
    Data Type as a list of values, where the index p of a parent
    can be calculated from the index c of a child as c // 2.
    """
    def __init__(self):
        self.heap_list = [0]  # not used. Here just to make parent-
                             # child calculations work nicely.
        # Note that current size of heap = len(self.heapList) - 1

    def insert(self,value):
        """Inserts a value into the heap by:
        a. adding it to the end of the list, and then
        b. "percolating" it up to an appropriate position
        """
        pass

    def percolate_up(self, i):
        """Beginning at i, check to see if parent above is greater than
        value at i. If so, percolate i upwards to parent's position.
        """
        pass 

    def del_min(self):
        """This is a bit trickier. It's easy to return the minimum item,
        the first item on the list, but how do we readjust the heap then?
        """
        pass

    def percolate_down(self,i):
        """Moves the item at i down to a correct level in the heap. To
        work correctly, needs to identify the minimum child for parent i.
        """
        pass

    def find_min(self):
        """Returns the minimum item in the heap, without removing it.
        """
        return self.heap_list[1]

    def is_empty(self):
        return len(self.heap_list) - 1 == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_keys):
        """Returns a new heap based on a pre-existing list of key 
        values."""
        pass

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)

def main():
    print("Demonstrating minHeap binary tree")
    bh = BinaryHeap()
    bh.insert(5)
    print(bh)
    '''
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(1)
    bh.insert(50)
    bh.insert(15)
    print(bh)
    print(bh.find_min())
    print(bh.del_min())
    print(bh)
    '''

if __name__ == "__main__":
    main()
 
    
 
def test_linear_searcher():
    print("Testing LinearSearcher...")
    passed = True
    searcher = LinearSearcher()
    arr = [10, 20, 30, 40, 50]
 
    if searcher.search(arr, 30) == 2:
        print("PASS: Found 30 at index 2")
    else:
        print("FAIL: Did not find 30 correctly")
        passed = False
 
    if searcher.search(arr, 10) == 0:
        print("PASS: Found 10 at index 0")
    else:
        print("FAIL: Did not find 10 correctly")
        passed = False
 
    if searcher.search(arr, 60) is None:
        print("PASS: 60 not found as expected")
    else:
        print("FAIL: 60 should not be found")
        passed = False
 
    print()
    return passed
 
 
def test_binary_searcher():
    print("Testing BinarySearcher...")
    passed = True
    searcher = BinarySearcher()
    arr = [1, 3, 5, 7, 9, 11]
 
    if searcher.search(arr, 7) == 3:
        print("PASS: Found 7 at index 3")
    else:
        print("FAIL: Did not find 7 correctly")
        passed = False
 
    if searcher.search(arr, 1) == 0:
        print("PASS: Found 1 at index 0")
    else:
        print("FAIL: Did not find 1 correctly")
        passed = False
 
    if searcher.search(arr, 12) is None:
        print("PASS: 12 not found as expected")
    else:
        print("FAIL: 12 should not be found")
        passed = False
 
    print()
    return passed
 
 
def test_queue():
    print("Testing Queue...")
    passed = True
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
 
    if q.dequeue() == 1:
        print("PASS: Dequeued 1")
    else:
        print("FAIL: Did not dequeue 1 correctly")
        passed = False
 
    if q.dequeue() == 2:
        print("PASS: Dequeued 2")
    else:
        print("FAIL: Did not dequeue 2 correctly")
        passed = False
 
    if q.dequeue() == 3:
        print("PASS: Dequeued 3")
    else:
        print("FAIL: Did not dequeue 3 correctly")
        passed = False
 
    if q.dequeue() is None:
        print("PASS: Queue empty correctly")
    else:
        print("FAIL: Queue should be empty")
        passed = False
 
    print()
    return passed
 
 
def test_deque():
    print("Testing Deque...")
    passed = True
    d = Deque()
    d.add_front(1)
    d.add_rear(2)
    d.add_front(0)
 
    if d.peek_front() == 0:
        print("PASS: Front is 0")
    else:
        print("FAIL: Front should be 0")
        passed = False
 
    if d.peek_rear() == 2:
        print("PASS: Rear is 2")
    else:
        print("FAIL: Rear should be 2")
        passed = False
 
    print()
    return passed
 
 
def test_hash_table():
    print("Testing HashTable...")
    passed = True
    ht = HashTable(5)
    ht.put(1, "one")
    ht.put(6, "six")  # Collision
    ht.put(11, "eleven")  # Another collision
 
    if ht.get(1) == "one":
        print("PASS: Found key 1 correctly")
    else:
        print("FAIL: Key 1 not found")
        passed = False
 
    if ht.get(6) == "six":
        print("PASS: Found key 6 correctly")
    else:
        print("FAIL: Key 6 not found")
        passed = False
 
    if ht.get(11) == "eleven":
        print("PASS: Found key 11 correctly")
    else:
        print("FAIL: Key 11 not found")
        passed = False
 
    if ht.get(2) is None:
        print("PASS: Key 2 correctly not found")
    else:
        print("FAIL: Key 2 should not exist")
        passed = False
 
    print()
    return passed
 
 
# ===== MAIN =====
if __name__ == "__main__":
    if test_linear_searcher():
        print("LinearSearcher tests: ALL PASS")
    else:
        print("LinearSearcher tests: SOME FAIL")
 
    if test_binary_searcher():
        print("BinarySearcher tests: ALL PASS")
    else:
        print("BinarySearcher tests: SOME FAIL")
 
    if test_queue():
        print("Queue tests: ALL PASS")
    else:
        print("Queue tests: SOME FAIL")
 
    if test_deque():
        print("Deque tests: ALL PASS")
    else:
        print("Deque tests: SOME FAIL")
 
    if test_hash_table():
        print("HashTable tests: ALL PASS")
    else:
        print("HashTable tests: SOME FAIL")
 
    print("All tests completed!")
