from time import perf_counter as pfc
import re
from string import ascii_lowercase

def load_puzzle(datei):
  with open(datei) as f:
    return list(f.read().strip())

def rekur(puzzle,pos):
  a = ord(puzzle[pos])+1
  if a in forbidden: a += 1
  if a > 122: 
    a = 97
    puzzle[pos] = chr(a)
    rekur(puzzle, pos-1)
  else:
    puzzle[pos] = chr(a)  
  return puzzle


def solve(puzzle):
  while True:
    puzzle = rekur(puzzle,-1)
    if not bool(re.search(r'(\w)\1.*(\w)\2', "".join(puzzle))): continue
    if not any(''.join(puzzle[i:i+3]) in ascii_lowercase for i in range(len(puzzle)-2)): continue
    return ''.join(puzzle)


puzzle = load_puzzle('Tag_11.txt')
forbidden = {105,108,111}

start = pfc()
print(solve(puzzle), pfc()-start)

start = pfc()
print(solve(puzzle), pfc()-start)