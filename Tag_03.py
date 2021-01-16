from time import perf_counter as pfc
import math


def load_puzzle(file):
  with open(file) as f:
    return f.read().strip()


def solve(puzzle, x=0, y=0):
  locations1, locations2 = set(), set()
  sx = sy = rx = ry = 0
  santa = True
  dirs = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
  for char in puzzle:
    dx, dy = dirs[char]
    x, y = x+dx, y+dy
    locations1.add((x, y))
    if santa:
      sx, sy = sx+dx, sy+dy
      locations2.add((sx, sy))
    else:
      rx, ry = rx+dx, ry+dy
      locations2.add((rx, ry))
    santa = not santa
  return len(locations1), len(locations2)


puzzle = load_puzzle('Tag_03.txt')

start = pfc()
print(solve(puzzle), pfc()-start)