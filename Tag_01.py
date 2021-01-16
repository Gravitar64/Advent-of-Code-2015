from time import perf_counter as pfc

def load_puzzle(file):
  with open(file) as f:
    return f.read().strip()

def solve(puzzle):
  a = puzzle.count('(')
  return a-(len(puzzle)-a)

def solve2(puzzle, floor = 0):
  for i,char in enumerate(puzzle):
    floor += 1 if char == '(' else -1
    if floor < 0:
      return i+1

puzzle = load_puzzle('Tag_01.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve2(puzzle), pfc()-start)