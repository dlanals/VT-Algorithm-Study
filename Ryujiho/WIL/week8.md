# [128](https://leetcode.com/problems/find-median-from-data-stream/)	Longest Consecutive Sequence	Graph	Medium
### Solution 1 
- 리스트 정렬을 사용하지 않아도 가장 최소인 값을 시작으로, 연속적인 값이 배열에 있는지 체크하여 가장 긴 연속된 길이를 구할 수 있다. 

### Solution 2
- 리스트 정렬을 하고, 다음 연속 값을 체크하는 방법을 시도했는데 time out 이 났다. -> 정렬했으므로 또 while문을 안 돌아도 될 것 같은데 이 부분에서 실수한 것 같다.. 아래 코드로 하면 잘 된다!
```
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        num_set = sorted(set(nums))
        cnt = 1
        maxLen = 1
        for i in range(len(num_set)-1):
                if num_set[i+1] == num_set[i]+1:
                    cnt += 1
                    maxLen = max(cnt, maxLen)
                else:
                    cnt = 1

        return maxLen
```

# [295](https://leetcode.com/problems/find-median-from-data-stream/)	Find Median from Data Stream	Heap	Hard
### Solution 1. heap (runtime: 534 ms)
**Two Condition**
- the median of an odd-sized list is a largest number of the first half of its elements.
- the median of an even-sized list is a (largest number of the first half of its elements + smallest number of the second half of its elements) / 2

**Two data structure**
- one that stores the first half of its elements (first_half, lower half) => Retrieve largest number (Use Max-Heap)
- one that stores the second half of its elements (second_half, larger half) => Retrieve lowest number (Use Min-Heap)

**Implementaion step**
1. Use 2 heap: min-heap / max-heap
2. When we add number, consider median value and balance two heap
3. Since each heap has lower half and larger half, finding median is simple
``` 
class MedianFinder:
    def __init__(self):
        self.max_heap = []  # the smaller half to use the largest number
        self.min_heap = []  # the larger half to use the smallest number

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        else: # len(max_heap) < len(min_heap)
            heappush(self.max_heap, -heappushpop(self.min_heap, num))
        
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return float(self.min_heap[0] - self.max_heap[0]) / 2.0
        else:
            return float(self.min_heap[0])
 ```
 **Reference**
  - https://leetcode.com/problems/find-median-from-data-stream/solutions/1497698/python-two-heap-easy-to-understand/ 
  - https://leetcode.com/problems/find-median-from-data-stream/solutions/2492199/python-3-min-heap-and-max-heap-approach-explained/?languageTags=python3&topicTags=heap-priority-queue
  **What I Learned**
  - How to use heapq
  - In python 3 , I can type return type like `-> float`
  
### Solution 2. List (Runtime: 3146 ms)
```
class MedianFinder(object):
    def __init__(self):
        self.arr = []

    def addNum(self, num):
        self.arr.append(num)
        

    def findMedian(self):
        self.arr.sort() # TC: O(nlogn)

        mid = len(self.arr)//2
        if len(self.arr)%2 == 1:
            # middle value
            return float(self.arr[mid])
        else:
            # mean of the two middle values.
            return float(self.arr[mid-1]+self.arr[mid])/2
        
        
```
