from atds import * 
import time 
import matplotlib.pyplot as plt 

uls = UnorderedListStack()

def testStackPush(s : Stack, n : int) -> float: 
    start = time.time()
    for i in range(s): 
        s.push(i)
    stop = time.time()
    return stop - start

    
def main(): 
    s = Stack

    if __name__ == "__main__": 
        main()
