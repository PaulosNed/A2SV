#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        left_child = (2 * i) + 1
        right_child = (2 * i) + 2
        smallest = i
        
        if right_child < n and arr[right_child] < arr[smallest]:
            smallest = right_child
            
        if left_child < n and arr[left_child] < arr[smallest]:
            smallest = left_child
            
            
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n-1, -1, -1):
            self.heapify(arr, n, i)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, len(arr))
        final = []
        while arr:
            final.append(arr[0])
            arr[0] = arr[-1]
            arr.pop()
            self.heapify(arr, len(arr), 0)
        for item in final:
            arr.append(item)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends