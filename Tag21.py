from time import perf_counter as pfc
import re

def load(file):
  with open(file) as f:
    return f.read()


def get_var(items):
  for wi in range(5):
    for ai in range(-1, 5):
      for ri1 in range(-1, 6):
        for ri2 in range(-1, 6):
          v = items['w'][wi]
          if ai > -1:
            v = [a+b for a, b in zip(v, items['a'][ai])]
          if ri1 > -1 and ri1 != ri2:
            v = [a+b for a, b in zip(v, items['r1'][ri1])]
          if ri2 > -1 and ri1 != ri2:
            v = [a+b for a, b in zip(v, items['r2'][ri2])]
          yield v


def solve(puzzle, shop):
  items = {}
  boss = list(map(int, re.findall(r'\d+', puzzle)))
  shop = shop.split('\n')
  
  items['w'] = [[int(v) for v in re.findall(r'\d+', shop[i])] for i in range(1,6)]
  items['a'] = [[int(v) for v in re.findall(r'\d+', shop[i])] for i in range(8,13)]
  items['r1'] = [[int(v) for v in re.findall(r'\d+', shop[i])[1:]] for i in range(15,21)]
  items['r2'] = [[int(v) for v in re.findall(r'\d+', shop[i])[1:]] for i in range(15,21)]
  
  min_invest, max_invest = 99999, 0
  for status in get_var(items):
    pd = max(status[1]-boss[2], 1)
    bd = max(boss[1]-status[2], 1)
    if pd >= bd and status[0] < min_invest:
      min_invest = status[0]
    if pd < bd and status[0] > max_invest:
      max_invest = status[0]
  return min_invest, max_invest


puzzle = load('Tag_21.txt')
shop = load('Tag_21a.txt')

start = pfc()
print(solve(puzzle, shop), pfc()-start)
