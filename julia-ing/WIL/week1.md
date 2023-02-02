## 1. two sum

### 🔮 My solution

- 첫번째로 시도한 코드는 brute force 방식
- 시간 복잡도: O(N^2)

```python
def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

### 🦦 Optimization (other solutions)

brute force 방식은 제곱 시간 복잡도를 가지기 때문에 최적화된 코드를 위해 구글링..

- 파이썬 내장 함수 **in** 을 사용하면 시간 복잡도를 O(N) 으로 줄일 수 있음!

    ```python
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            second = target - num
            if second in nums[i+1:]:
                return [i, nums[i+1:].index(second) + i + 1]
    ```
  enumerate() 을 사용하면 인덱스와 데이터를 같이 뽑을 수 있다. 
target 를 만들기 위해 필요한 값을 second 변수에 저장한 후, 만약 그 값이 아직 돌지 않은 nums 리스트 뒷부분에 존재한다면
그 값의 인덱스를 찾아 i 와 함께 리턴해준다.


- **Hash Table (dictionary)**
    ```python
    def twoSum(self, nums, target):
        hashTable = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in hashTable:  # 나머지 값이 맵에 있으면
                return sorted([i, hashTable[second]])  # 저장된 인덱스를 불러옴
            hashTable[nums[i]] = i  # 숫자와 인덱스를 맵에 저장
    ```
    해당 방법도 시간 복잡도는 O(N) 이며 maybe 이 문제의 최적 코드일 듯 하다. 
위 방식과 동일하게 나머지 값을 second 변수에 저장해두고 딕셔너리에 저장되어있는지 확인한다. 
만약 있으면 second 데이터에 해당하는 인덱스를 i와 함께 리턴해준다. 참고로 sorted는 없어도 문제 통과하기는 한다..
그리고 위에서 리턴되지 않는다면 해시테이블 즉 딕셔너리에 값을 저장한다. (key는 nums[i] 즉 데이터, value는 인덱스)

### 👊 문제 회고

개인적으로 처음부터 최적의 코드를 짜는건 아직 어렵다. 이 문제도 구글링 전까지는 쉽게 떠오르는 풀이가 brute force 밖에 없었기 때문에.. 아직 갈 길이 먼 것 같다 ^0^
해당 문제에서 인상깊었던 것은 해시테이블을 이용한 3번 풀이였는데,
딕셔너리를 잘 활용하면 원하는 값을 바로 찾아올 수 있고 시간복잡도도 줄일 수 있다는 사실을 잊지 말자!

## 2. longest increasing subsequence

### 🔮 My solution

- 첫번째로 시도한 코드는 common한 dynamic programming 방식
- 시간 복잡도: O(N^2)
  - 예시:
    - nums = [10,9,2,5,3,7,101,18]
    - dp 
      - i = 0: [1,1,1,1,1,1,1,1]
      - i = 1: [1,1,1,1,1,1,1,1]
      - i = 2: [1,1,1,1,1,1,1,1]
      - i = 3: [1,1,1,2,1,1,1,1]
      - i = 4: [1,1,1,2,2,1,1,1]
      - i = 5: [1,1,1,2,2,3,1,1]
      - i = 6: [1,1,1,2,2,3,4,1]
      - i = 7: [1,1,1,2,2,3,4,4]
      - result : max 4

```python
def lengthOfLIS(self, nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

### 🦦 Optimization (other solutions)

- **binary search**

이진탐색을 이용하면 시간복잡도를 O(NlogN) 으로 만들 수 있음!
**bisect_left** ? - 참고: [bisect_left, biseft_right](https://folivora.tistory.com/83)

예시: nums = [10,9,2,5,3,7,101,18]
1. tmp = [10]
2. for loop
   1. x = 9, tmp = [9]
   2. x = 2, tmp = [2]
   3. x = 5, tmp = [2,5]
   4. x = 3, idx = 1, tmp = [2,3]
   5. x = 7, tmp = [2,3,7]
   6. x = 101, tmp = [2,3,7,101]
   7. x = 18, idx = 3, tmp = [2,3,7,18]
3. return length 4

```python
def lengthOfLIS(self, nums):
    tmp = [nums[0]]
    for x in nums[1:]:
        if tmp[-1] < x:  # x가 리스트 마지막 요소보다 크면
            tmp.append(x)
        else:
            idx = bisect_left(tmp, x)  # x를 삽입할 위치를 찾아 해당 위치의 값을 갈아 끼운다
            tmp[idx] = x
    return len(tmp)
```

### 👊 문제 회고
문제를 보고 DP 를 사용해야겠다고 생각해 다이나믹으로 풀었지만, 역시 보다 좋은 풀이가 있었다.
리스트를 bisect_left를 사용해 갈아끼우는 방식으로 최적화하는 방법이었는데,
앞으로 리스트 관련 최적화를 고민할 때 binary를 하나의 수단으로 잘 떠올렸으면 좋겠다!
