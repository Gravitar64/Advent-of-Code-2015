from time import perf_counter as pfc


def load_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(puzzle):
  part1 = sum(len(z) - len(eval(z)) for z in puzzle)
  part2 = sum(2+z.count('\\')+z.count('"') for z in puzzle)
  return part1, part2


puzzle = load_puzzle('Tag_08.txt')

start = pfc()
print(solve(puzzle), pfc()-start)
