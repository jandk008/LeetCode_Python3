from math import ceil
from math import log


class SegmentTree:
  def __init__(self, nums):
    self.nums = nums
    self.n = len(nums)
    self.height = ceil(log(self.n, 2))
    self.lazy = [0] * self.n
    self.tree = [0] * self.n * 2
    self.build()
    
  def build(self):
    for i, num in enumerate(self.nums):
      self.update(i, i + 1, num)
    
  def query(self, i, j):
    i, j = i + self.n, j + self.n - 1
    self.push(i)
    self.push(j)
    total = 0
    while i <= j:
      if i % 2:
        total += self.tree[i]
        i += 1
      if not j % 2:
        total += self.tree[j]
        j -= 1
      i >>= 1
      j >>= 1
    return total

  def push(self, i):
    k = 1 << (self.height - 1)
    for h in range(self.height, 0, -1):
      p = i >> h
      if self.lazy[p]:
        self.apply(p << 1, self.lazy[p], k)
        self.apply(p << 1 | 1, self.lazy[p], k)
        self.lazy[p] = 0
      k >>= 1
        
  def apply(self, i, value, k):
    self.tree[i] = value * k
    if i < self.n:
      self.lazy[i] = value
      
  def update(self, i, j, value):
    i, j = self.n + i, self.n + j - 1
    i0, j0, k = i, j, 1
    self.push(i)
    self.push(j)
    while i <= j:
      if i % 2:
        self.apply(i, value, k)
        i += 1
      if not j % 2:
        self.apply(j, value, k)
        j -= 1
      i >>= 1
      j >>= 1
      k <<= 1
    self.pull(i0)
    self.pull(j0)

  def pull(self, i):
    k = 2
    while i > 1:
      i >>= 1
      self.calculate(i, k)
      k <<= 1

  def calculate(self, i, k):
    if self.lazy[i]:
      self.tree[i] = self.lazy[i] * k
    else:
      self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
 
  # simply change apply() and calculation() to below if we need increment modification
  def apply_inc(self, i, value, k):
    self.tree[i] += value * k
    if i < self.n:
      self.lazy[i] += value
      
  def calculation_inc(self, i, k):
    self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1] + self.lazy[i] * k
     
