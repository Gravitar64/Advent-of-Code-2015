from time import perf_counter as pfc
import re


def load_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(puzzle):
  p1 = r"(?!.*(ab|cd|pq|xy))(?=(.*[aeiou]){3})(?=.*(\w)\3)"
  part1 = sum(1 for z in puzzle if re.match(p1,z))
  
  p2 = r'\w*(\w)\w\1'
  p3 = r'(\w\w)\w*\1'
  part2 = sum(1 for z in puzzle if re.search(p2,z) and re.search(p3,z))
  
  return part1,part2

puzzle = load_puzzle('Tag_05.txt')

start = pfc()
print(solve(puzzle), pfc()-start)