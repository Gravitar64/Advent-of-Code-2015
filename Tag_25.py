from time import perf_counter as pfc


def solve(start, col, row):
  for _ in range(sum(range(row + col -1)) + col - 1):
    start = (start * 252533) % 33554393
  return start


puzzle = (3029,2947)

start = pfc()
print(solve(20151125, *puzzle), pfc()-start)

