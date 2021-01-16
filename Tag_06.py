from time import perf_counter as pfc
from collections import defaultdict
import re


def load_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f]

def solve(puzzle, part1=True):
  grid = defaultdict(int)
  if part1:
    actions = {'n': lambda _:True, 'f': lambda _:False, ' ': lambda x: not x}
  else:
    actions = {'n': lambda x: x+1, 'f': lambda x: max(x-1,0), ' ': lambda x: x+2}
  
  for z in puzzle:
    x1,y1,x2,y2 = list(map(int,(re.findall(r'\d+',z))))
    f = actions[z[6]]
    for x in range(x1,x2+1):
      for y in range(y1,y2+1):
        grid[(x,y)] = f(grid[(x,y)])
  return sum(grid.values())
  

puzzle = load_puzzle('Tag_06.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve(puzzle, False), pfc()-start)