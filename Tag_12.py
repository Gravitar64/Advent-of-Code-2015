from time import perf_counter as pfc
import re
import json

def load_puzzle(datei):
  with open(datei) as f:
    return f.read()

def solve(puzzle):
  return sum(map(int,re.findall(pattern,puzzle)))

def solve2(puzzle):

  def hook(obj):
    return {} if 'red' in obj.values() else obj

  puzzle = str(json.loads(puzzle, object_hook = hook))
  return sum(map(int,re.findall(pattern,puzzle)))
      

puzzle = load_puzzle('Tag_12.txt')
pattern = r'[\d-]+'

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve2(puzzle), pfc()-start)