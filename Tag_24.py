from time import perf_counter as pfc
from itertools import combinations
import math


def load(file):
  with open(file) as f:
    return [int(x) for x in f]


def solve(puzzle, part1 = True):
  target = sum(puzzle) // 3 if part1 else sum(puzzle) // 4
  for i in range(5,len(puzzle)):
    qes = [math.prod(c) for c in combinations(puzzle,i) if sum(c) == target]
    if qes: return(min(qes))


puzzle = load('Tag_24.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve(puzzle, False), pfc()-start)
