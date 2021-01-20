from time import perf_counter as pfc
import random as rnd
import math


def load(file):
  with open(file) as f:
    return [int(x) for x in f]


def solve(puzzle, part1=True):
  target = sum(puzzle) // 3 if part1 else sum(puzzle) // 4
  fwst = 100
  for n in range(30_000):
    rnd.shuffle(puzzle)
    p, v = puzzle.copy(), []
    while True:
      v.append(p.pop())
      if (delta := target - sum(v)) in p:
        v.append(delta)
        if len(v) < fwst:
          fwst = len(v)
          sqe = math.prod(v)
        elif len(v) == fwst:
          sqe = min(sqe, math.prod(v))
        break  
      if sum(v) > target:
        break
  return sqe


puzzle = load('Tag_24.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve(puzzle, False), pfc()-start)
