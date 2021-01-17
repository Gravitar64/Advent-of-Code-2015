from time import perf_counter as pfc
from itertools import product
import re


def load(file):
  with open(file) as f:
    return f.read()


class Status:
  def __init__(self, cost, damage, armor):
    self.cost = int(cost)
    self.damage = int(damage)
    self.armor = int(armor)

  def __add__(self, other):
    return Status(self.cost + other.cost, self.damage + other.damage, self.armor + other.armor)


def get_var(items):
  for w,a,r1,r2 in product(items['w'],items['a'],items['r'],items['r']):
    yield w+a+r1+r2 if r1 != r2 else w+a


def solve(puzzle, shop):
  boss = Status(*re.findall(r'\d+', puzzle))
  shop = shop.split('\n')
  
  items = {}
  items['w'] = [Status(*re.findall(r'\d+', shop[i])) for i in range(1, 6)]
  items['a'] = [Status(*re.findall(r'\d+', shop[i])) for i in range(8, 13)]+[Status(0,0,0)]
  items['r'] = [Status(*re.findall(r'\d+', shop[i])[1:]) for i in range(15, 21)]+[Status(0,0,0)]
    
  min_invest, max_invest = 99999, 0
  for player in get_var(items):
    runden_boss = boss.cost // max(player.damage - boss.armor, 1)
    runden_player = 100 // max(boss.damage - player.armor, 1)
    if runden_player >= runden_boss and player.cost < min_invest:
      min_invest = player.cost
    if runden_player < runden_boss and player.cost > max_invest:
      max_invest = player.cost
  return min_invest, max_invest


puzzle = load('Tag_21.txt')
shop = load('Tag_21a.txt')

start = pfc()
print(solve(puzzle, shop), pfc()-start)