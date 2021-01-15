from time import perf_counter as pfc
import numpy as np
from collections import defaultdict

def solve():
  N = 10_000_000
  target = 33_100_000
  houses_a, houses_b = np.zeros(N), np.zeros(N)
  for elf in range(1, N//10):
    houses_a[elf::elf] += 10 * elf
    houses_b[elf:(elf+1)*50:elf] += 11 * elf
  return np.argmax(houses_a >= target), np.argmax(houses_b >= target)

start = pfc()
print(solve(), pfc()-start)