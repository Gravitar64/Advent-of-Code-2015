from time import perf_counter as pfc
import re


def load_puzzle(datei):
  with open(datei) as f:
    return f.readlines()


def solve(puzzle):
  rentiers, dist = {}, {}
  for zeile in puzzle:
    rentiers[zeile.split()[0]] = list(map(int,re.findall(r'\d+',zeile)))
  for ren, (kms, s1, s2) in rentiers.items():
    dist[ren] = 2503 // (s1+s2) * (kms*s1) + min(s1, 2503 % (s1+s2))*kms
  part1 = max(dist.values())

  points = {ren:0 for ren in rentiers}
  for i in range(1,2504):
    for ren, (kms, s1, s2) in rentiers.items():
      dist[ren] = i // (s1+s2) * (kms*s1) + min(s1, i % (s1+s2))*kms
    maximum = max(dist.values())
    for ren, value in dist.items():
      if value == maximum:
        points[ren] += 1
  return part1, max(points.values())      
      

puzzle = load_puzzle('Tag_14.txt')
start = pfc()
print(solve(puzzle), pfc()-start)