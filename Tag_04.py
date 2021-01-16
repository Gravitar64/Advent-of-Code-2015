from time import perf_counter as pfc
import hashlib


def load_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(puzzle, zeros=5):
  for sk in puzzle:
    i = 0
    while True:
      sk1 = sk + str(i)
      hash = hashlib.md5(sk1.encode())
      if hash.hexdigest()[:zeros] == '0'*zeros:
        return i
      i += 1


puzzle = load_puzzle('Tag_04.txt')

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve(puzzle, 6), pfc()-start)
