from time import perf_counter as pfc
import math


def load_puzzle(file):
  with open(file) as f:
    return [[int(x) for x in line.split('x')] for line in f]


def solve(puzzle, sqf=0):
  for l, w, h in puzzle:
    s1, s2, s3 = l*w, w*h, h*l
    sqf += 2*(s1+s2+s3)+min(s1, s2, s3)
  return sqf


def solve2(puzzle, rbf=0):
  return sum([2*(sum(p)-max(p))+math.prod(p) for p in puzzle])


puzzle = load_puzzle('Tag_02.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve2(puzzle), pfc()-start)
