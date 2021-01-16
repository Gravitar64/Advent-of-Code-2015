from time import perf_counter as pfc
from itertools import groupby


def load_puzzle(datei):
  with open(datei) as f:
    return f.read().strip()


def solve(puzzle, anz):
  for _ in range(anz):
    puzzle = ''.join(str(len(list(g))) + k for k,g in groupby(puzzle))
  return len(puzzle)  

puzzle = load_puzzle('Tag_10.txt')

start = pfc()
print(solve(puzzle,40), pfc()-start)

start = pfc()
print(solve(puzzle,50), pfc()-start)