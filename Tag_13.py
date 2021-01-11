from time import perf_counter as pfc
import re
from collections import defaultdict
from itertools import permutations


def load_puzzle(datei):
  with open(datei) as f:
    return f.readlines()


def max_happiness(pairs,persons,best=0):
  for v in permutations(persons):
    summe = pairs[v[0]][v[-1]] + pairs[v[-1]][v[0]]
    for p1,p2 in zip(v,v[1:]):
      summe += pairs[p1][p2] + pairs[p2][p1]
    best = max(best,summe)
  return best  


def solve(puzzle):
  pairs, persons = defaultdict(dict), set()
  for zeile in puzzle:
    happiness = int(re.findall(r'[\d]+',zeile)[0])
    if 'lose' in zeile: happiness *= -1
    words = re.findall(r'\w+',zeile)
    p1,p2 = words[0], words[-1]
    pairs[p1][p2] = happiness
    persons.add(p1)
  part1 = max_happiness(pairs, persons)

  for p in persons:
    pairs[p]['me'] = pairs['me'][p] = 0
  persons.add('me')

  return part1, max_happiness(pairs, persons)
  

puzzle = load_puzzle('Tag_13.txt')
start = pfc()
print(solve(puzzle), pfc()-start)