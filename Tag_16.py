from time import perf_counter as pfc


def load_puzzle(datei):
  with open(datei) as f:
    return f.readlines()


def check(name,value):
  return ticker[name] == int(value)


def check2(name,value):
  value = int(value)
  if name in ('cats', 'trees'): return value > ticker[name]
  if name in ('pomeranians', 'goldfish'): return value < ticker[name]
  return ticker[name] == value


def solve(puzzle):
  part1 = part2 = ''
  for zeile in puzzle:
    aunt = zeile.split(':')[0]
    props = zeile[len(aunt)+2:].split(', ')
    if not part1 and all([check(*p.split(': ')) for p in props]): part1 = aunt
    if not part2 and all([check2(*p.split(': ')) for p in props]): part2 = aunt
    if part1 and part2: return part1, part2


puzzle = load_puzzle('Tag_16.txt')
ticker = dict(children=3, cats=7, samoyeds=2, pomeranians=3, akitas=0, vizslas=0, goldfish=5, trees=3, cars=2, perfumes=1)

start = pfc()
print(solve(puzzle), pfc()-start)