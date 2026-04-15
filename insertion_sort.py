#insertion_sort

def sort(arr): 
    for start in range(1, len(arr)):
        j = start
        while arr[j] < arr(j - 1) and j > 0: 
            #while they're out of order and we haven't hit the edge case
            swap = arr[j]
            arr[j] = arr[j -1]
            arr[j - 1] = swap 
            j -= 1
            print("Adjusting", arr)
            print()

def main(): 
    arr = [0, 7, 4, 6, 2, 3]
    print(arr)
    sort(arr)
    print(arr)
    print("Done")