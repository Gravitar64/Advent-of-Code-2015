from time import perf_counter as pfc
from itertools import combinations


def load_puzzle(datei):
  with open(datei) as f:
    return [int(x) for x in f]


def solve(puzzle):
  part2 = counter = 0
  for i in range(1,len(puzzle)):
    for v in combinations(puzzle,i):
      if sum(v) != 150: continue
      counter += 1
    if not part2: part2 = counter
  return counter, part2  

puzzle = load_puzzle('Tag_17.txt')

start = pfc()
print(solve(puzzle), pfc()-start)