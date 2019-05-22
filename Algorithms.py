












import time
class Environment:
  def solution(self, nums):
    sumV = 0
    for num in nums:
      sumV += num
    return sumV

  def test(self, cases, functionToTest):
      for i, case in enumerate(cases):
          caseInput, expected = case
          failed = functionToTest(caseInput) != expected
          if failed:
              print('Failed: test case {} of {} with:\nInput: {}\nReturned: {}\nExpected: {}'.format(i+1, len(cases), caseInput, functionToTest(caseInput), expected))
              return 

      print('Succeeded: All {} test cases passed'.format(len(cases)))
      return

cases = [
    ([-2, -7], -9),
    ([2, -2], 0) ]

env = Environment()

start = time.process_time()
env.test(cases, env.solution)
end = time.process_time()

print('Running all {} test cases took {}ms.'.format(len(cases), round((end - start)*1000, 4)))

## trie
def buildTrie(self, words):
    self.root = {}
    for word in words:
        node = self.root
        for c in word + "$":
            node = node.setdefault(c, {})

## edit distance without replacement
def editDistance(w1, w2, allowance):
    if len(w1) > len(w2):
        w1, w2 = w2, w1
    if len(w2) != len(w1) + allowance:
        return False
    
    p1 = p2 = 0
    while p1 < len(w1):
        if w1[p1] == w2[p2]:
            p1 += 1
            p2 += 1
        elif allowance == 0:
            return False
        else:
            p2 += 1
            allowance -= 1
    return True

## binarySearch
def binarySearch(array, target):
    L = 0
    R = len(array) - 1
    while L < R:
        M = (L+R) // 2
        if array[M] == target:
            return M
        elif array[M] < target:
            L = M + 1
        else:
            R = M
    return L

## sorting
def radixSort(self, num):
    for i in range(32):
        big = []
        small = []
        needle = 1 << i
        for val in num:
            if val & needle != 0:
                big.append(val)
            else:
                small.append(val)

        num = []
        num += small
        num += big

    return num

def mergeSort(self, nums: List[int]) -> List[int]:
    if len(nums) > 1:
        M = len(nums) // 2
        L = nums[:M]
        R = nums[M:]

        L = self.mergeSort(L)
        R = self.mergeSort(R)
        l = r = k = 0
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                nums[k] = L[l]
                l += 1
            else:
                nums[k] = R[r]
                r += 1
            k+=1

        while l < len(L):
            nums[k] = L[l]
            l += 1
            k += 1
        while r < len(R):
            nums[k] = R[r]
            r += 1
            k += 1
            
    return nums

## shuffle
