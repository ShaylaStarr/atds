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
        return self.list.pop(-1)
    
    def is_empty(self): 
        if len(self.list) == 0:
            return True
        else: 
            return False

class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None

    def get_data(self): 
        return self.data 
    
    def get_next(self): 
        return self.next
    
    def set_data(self, newData):
        self.data = newData

    def set_next(self, newNext): 
        self.next = newNext

    def __repr__(self): 
        return "Node (data = " + self.data + ", next = " + str(self.next) + ")"
    
class UnorderedListStack():
    ''''''
    def __init__(self): 
        self.uls = UnorderedList()

    def push(self, item): 
        self.uls.add(item)

    def pop(self): 
        self.uls.pop(0)
    
    def peek(self):
        item = self.uls.pop(0)
        self.uls.push(item)

        return item

    def size(self):
        self.uls.length()

    def is_empty(self): 
        self.uls.is_empty()


def main(): 
    pass
    

    

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

        while (current != None):
            if current.get_data() == item: 
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    return
            else:
                previous = current
                current = current.get_next
    
    def search(self, item): 
        current_node = self.head

        while(current_node != None):
            if item == current_node.get_data():
                return True
            current_node = current_node.get_next()
            
        return False 
    
    def is_empty(self): 
        if self.head == None: 
            return True 
        return False
    
    def length(self):
        node_count = 0                  
        current = self.head     
        while current != None:         
            current = current.get_next()     
            node_count += 1                
        return node_count

    def append(self, item):
        current_node = self.head
        previous = None
        new_node = Node(item)

        while(current_node != None): 
            previous = current_node
            current_node = current_node.get_next() 
        
        previous.set_next(new_node)
    
    def index(self, item):
        node_count = 0 
        current = self.head
        while(current != None):
            if current.get_data() == item: 
                return node_count
            else: 
                current = current.get_next() 
            node_count += 1
    
    def insert(self, pos, item):
        current_node = self.head
        preivous = None
        node_count = 0
        new_node = Node(item)

        while(current_node != None): 
            if node_count == pos: 
                if pos == 0:
                    self.add(item)
                    break
                elif self.length() - 1 == pos: 
                    self.append(item)
                    break
                else:
                    preivous.set_next(new_node)
                    new_node.set_next(current_node) 
                    break

            previous = current_node
            current_node = current_node.get_next()
            node_count += 1

    
    def pop(self):
        current_node = self.head
        previous_node = None
        return_node  = None

        if self.length() <= 1:
            return_node = self.head
            self.head = None
            return return_node
        
        current_node = current_node.get_next() 
        while(current_node != None):
            previous_node = current_node
            current_node = current_node.get_next()

        return_node = previous_node.get_next()
        previous_node.set_next(None)
        return return_node


    def pop(self, pos):
        current_node = self.head
        previous_node = None
        return_node  = None
        node_count = 0

        
        while(current_node != None): 
            if node_count == pos: 
                if pos == 0: 
                    return_node = current_node
                    self.head = current_node.get_next() 
                    return return_node
                elif self.length() - 1 == pos: 
                    return self.pop()
                else:
                    return_node = current_node
                    previous_node.set_next(current_node.get_next())
                    return return_node
            
            previous_node = current_node 
            current_node = current_node.get_next()
            node_count += 1 

'''class LinearCearcher(object): 
    def search(self, arr : list, target : int) -> int:
            value = 0
            lower = len
            if value > arr[middle]: 
                return value
            elif value < arr[middle]:
                higher = middle - 1
            else: 
                lower = middle + 1 
        return None '''
            
'''
class BinarySearcher (object): 

   def __init__(self): 
       pass 
   def search(self, arr, value): 
       middle = len(arr)//2
       if arr[middle] == value: 
           return middle
       elif value < arr[middle]: 
           return self.seach(arr[middle], value)
       else: 
           return self.search(arr[middle], value)

        
def main(): 
    ls = LinearSearcher()
    ls.find[[4,5,3,1,9,8,8,235]]






if current.get_data() == item: 
    if previous == None: 
        self.head = current.get_next()
        else: 
            previous.set_next(current.get_next())
        return 
    
    else: 
        previous = current 
        current = current.get_next '''


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
            self.length += 1
        else: 
            self.tail.next = new_node
            self.tail = new_node 
            self.length += 1 
        
    def dequeue(self): 
        remove_node = self.head
        self.head = remove_node.next
        remove_node.next = None 
        self.length -= 1 
        return remove_node.data
    
    def peek(self): 
        return self.head
    
    def size(self): 
        return self.length
    
    def is_empty(self): 
        if self.length == 0: 
            return True 
        else: 
            return False

class Deque(object): 

    def __init__(self):
        self.deque = []
    
    def add_front(self, item):
        self.deque.insert(0, item)
    
    def add_rear(self, item):
        self.deque.append(item)

    def peak_front(self): 
        if len(self.deque) > 0: 
            return self.deque[0]
        
    def peek_rear(self): 
        if len(self.deque) > 0: 
            return self.deque[-1]
        
    def remove_front(self): 
        if len(self.deque) > 0: 
            self.deque.pop(0)

    def remove_rear(self):
        if len(self.deque) > 0: 
            self.deque.pop(-1)
    
    def size(self): 
        return len(self.deque)
    
    def is_empty(self): 
        if len(self.deque) == 0: 
            return True
        else: 
            return 
        
class HashTable(object):

    def __init__(self, m): 
        self.m = m
        self.size = 0 
        self.keys = m * [None]
        self.values  = m * [None]

    def hash_function(self, key, m): 
        return key % m 

    def put(self, key, value): 
        hash = self.has_function(key, self.m)
        while self. key[hash] != None: 
            hash = (hash + 1) % self.m
        self.keys[hash] = key 
        self.values[hash] = value 
        self.entires += 1 
    
 '''   def get(self, key): 
        hash = self.hash_function(key, self.m)
        while self.key[hash] != None and self.keys
        [hash] != key: 

    
    def __repr__(self): 
        return self.keys + "\n" + self.values 
    '''
     

    

        

#!/usr/bin/env python3
'''
hash_table_tester.py
This program imports the HashTester class and uses it to store a range 
of key-value pairs.
@author Richard White
@version 2026-04-06, updated from 2017-04-04 
'''


from atds import *

def main():
    tests_passed = 0
    print("\nTEST: Creating HashTable(11)...")
    try:
        h = HashTable(11)
        tests_passed += 1
        print("SUCCESS. Table created.")
    except:
        print("FAIL. Table not created.")
    
    print("\nTEST: Using put function to store key-value pairs in table...")
    try:
        h.put(1, "a")
        h.put(6, "e")
        h.put(10, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")
    
    print("\nTEST: Trying to print the current state of table...")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, None, 10]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, None, 'f']")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")
    
    print("\nTEST: Using put() for a function at the end of the table to see if it wraps around...")
    try:
        h.put(21, "g")
        if h.get(21) == "g":
            print("SUCCESS. .put() correctly wrapped in the table.")
            tests_passed += 1
        else:
            print("FAIL. .put() wraparound didn't work.")
        print(h)
    except:
        print("FAIL. .put() didn't correctly wrap the table in linear probe.")
    
    print("\nTEST: Checking the number of values in the hash table...")
    try:
        l = len(h)
        if l == 6:
            print("SUCCESS. len(h) is 6.")
            tests_passed += 1
        else:
            print("FAIL. len(h) should have been 5 -- solution is to write a __len__ method.")
    except:
        print("FAIL. Problem with len() method.")
    
    print("\nTEST: Looking for original hash in table...")
    try:
        result = h.get(10)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nTEST: Replacing original hash {1, 'a'} in table with {1, 'z'}...")
    try:
        h.put(1, "z")
        result = h.get(1)
        if result == "z":
            print("SUCCESS. New value put and found.")
            tests_passed += 1
        else:
            print("FAIL. New value not put/found.")
    except:
        print("FAIL. Problem with replacing an old key.")
    
    print("\nTEST: Looking for key-collision in table...")
    try:
        result = h.get(23)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "c":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() finding a key-collision.")
    
    print("\nTEST: Looking for a hash that's not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nTEST: Looking for collision not in table...")
    try:
        result = h.get(45)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent collision not found.")
        else:
            print("FAIL. Non-existent collision found.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nResults:")
    print(tests_passed,"/ 12 tests passed")


if __name__ == "__main__":
    main()
