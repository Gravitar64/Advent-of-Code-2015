from time import perf_counter as pfc
from collections import Counter
from itertools import product


def load_puzzle(datei):
  with open(datei) as f:
    return {(x,y) for y,zeile in enumerate(f) for x,char in enumerate(zeile) if char == '#'}


def get_neighb(puzzle):
  neighbors = []
  for x,y in puzzle:
    for dx,dy in product(range(-1,2), repeat=2):
      if dx == dy == 0: continue
      x2,y2 = x+dx, y+dy
      if 0 <= x2 < 100 and 0 <= y2 < 100: neighbors.append((x2,y2))
  return Counter(neighbors)     


def solve(puzzle, part2=False):
  for _ in range(100):
    puzzle = {pos for pos,anz in get_neighb(puzzle).items() if anz == 3 or (anz ==2 and pos in puzzle)}
    if part2: puzzle.update([(0,0), (99,0), (99,99), (0,99)])
  return len(puzzle)

puzzle = load_puzzle('Tag_18.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve(puzzle, True), pfc()-start)