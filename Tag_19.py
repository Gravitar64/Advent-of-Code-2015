from time import perf_counter as pfc


def load_puzzle(datei):
  with open(datei) as f:
    return f.read().split('\n\n')


def get_replacements(starting, von, zu):
  mols, pos = set(), 0
  while True:
    pos = starting.find(von,pos)
    if pos == -1: return mols
    mols.add(starting[:pos] + zu + starting[pos+len(von):])
    pos += 1
  return mols  

def solve(puzzle):
  dist_mols = set()
  starting = puzzle[1]
  for zeile in puzzle[0].split('\n'):
    von,zu = zeile.split(' => ')
    dist_mols.update(get_replacements(starting, von, zu))
  return len(dist_mols)

puzzle = load_puzzle('Tag_19.txt')

start = pfc()
print(solve(puzzle), pfc()-start)