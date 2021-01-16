from time import perf_counter as pfc
import re

def load(file):
  with open(file) as f:
    return f.read()

class Status:
  def __init__(self,cost,damage,armor):
    self.cost = int(cost)
    self.damage = int(damage)
    self.armor = int(armor)

  def __add__(self, other):
    return Status(self.cost+other.cost, self.damage+other.damage, self.armor + other.armor)
    


def get_var(items):
  for wi in range(5):
    for ai in range(-1, 5):
      for ri1 in range(-1, 6):
        for ri2 in range(-1, 6):
          v = items['w'][wi]
          if ai > -1: 
            v += items['a'][ai]
          if ri1 > -1 and ri1 != ri2:
            v += items['r1'][ri1]
          if ri2 > -1 and ri1 != ri2:
            v += items['r2'][ri2]
          yield v


def solve(puzzle, shop):
  items = {}
  boss = list(map(int, re.findall(r'\d+', puzzle)))
  shop = shop.split('\n')
  
  items['w'] = [Status(*re.findall(r'\d+', shop[i])) for i in range(1,6)]
  items['a'] = [Status(*re.findall(r'\d+', shop[i])) for i in range(8,13)]
  items['r1'] = [Status(*re.findall(r'\d+', shop[i])[1:]) for i in range(15,21)]
  items['r2'] = [Status(*re.findall(r'\d+', shop[i])[1:]) for i in range(15,21)]
  
  min_invest, max_invest = 99999, 0
  for player in get_var(items):
    runden_boss = boss[0] / max(player.damage - boss[2], 1)
    runden_player = 100 / max(boss[1]-player.armor, 1)
    if runden_player >= runden_boss and player.cost < min_invest:
      min_invest = player.cost
    if runden_player < runden_boss and player.cost > max_invest:
      max_invest = player.cost
  return min_invest, max_invest


puzzle = load('Tag_21.txt')
shop = load('Tag_21a.txt')

start = pfc()
print(solve(puzzle, shop), pfc()-start)