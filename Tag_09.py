from time import perf_counter as pfc
from itertools import permutations


def load_puzzle(file):
  with open(file) as f:
    return [x.strip() for x in f]


def solve(puzzle):
  tree, towns, dist = {}, set(), []
  for zeile in puzzle:
    locs, entf = zeile.split(' = ')
    l1, l2 = locs.split(' to ')
    towns.update((l1, l2))
    tree[(l1, l2)] = int(entf)
    tree[(l2, l1)] = int(entf)
    
  for perm in permutations(towns):
    dist.append(sum(map(lambda x, y: tree[(x, y)], perm[:-1], perm[1:])))
  return min(dist), max(dist)


puzzle = load_puzzle('Tag_09.txt')

start = pfc()
print(solve(puzzle), pfc()-start)
