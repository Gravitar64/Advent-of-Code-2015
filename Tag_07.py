from time import perf_counter as pfc
import functools


def load_puzzle(file):
  puzzle = {}
  with open(file) as f:
    for zeile in f:
      ops, result = zeile.strip().split('->')
      puzzle[result.strip()] = ops.strip().split()
  return puzzle


@functools.lru_cache()
def solve(node):
  if node.isdigit(): return int(node)
  ops = puzzle[node]
  if "NOT" in ops:
    return ~solve(ops[1])
  if "AND" in ops:
    return solve(ops[0]) & solve(ops[2])
  elif "OR" in ops:
    return solve(ops[0]) | solve(ops[2])
  elif "LSHIFT" in ops:
    return solve(ops[0]) << solve(ops[2])
  elif "RSHIFT" in ops:
    return solve(ops[0]) >> solve(ops[2])
  else:
    return solve(ops[0])


puzzle = load_puzzle('Tag_07.txt')

start = pfc()
erg = solve('a')
print(erg, pfc()-start)

start = pfc()
solve.cache_clear()
puzzle['b'] = [str(erg)]
print(solve('a'), pfc()-start)
