from time import perf_counter as pfc
import random as rnd
import copy

class Spell:
  def __init__(self, mana, damage, heal, armor, mana_add, duration):
    self.mana = mana
    self.damage = damage
    self.heal = heal
    self.armor = armor
    self.mana_add = mana_add
    self.duration = duration

  def __add__(self, other):
    return Spell(0, self.damage + other.damage, self.heal + other.heal, self.armor + other.armor, self.mana_add + other.mana_add, 0)

  def __eq__(self, other):
    return self.mana == other.mana

def solve(part2=False):
  min_invest = 99999
  for n in range(20_000):
    active_spells = []
    boss = [51,9]
    player = [50,500]
    invest, players_turn, status = 0, True, Spell(0,0,0,0,0,0)
    buys = []
    while player[0] >= 0:
      if players_turn:
        if part2:
          player[0] -= 1
          if player[0] <= 0:
            break
        valid_spells = [s for s in spells if s.mana <= player[1] and s not in active_spells]
        if not valid_spells: break
        sp = rnd.choice(valid_spells)
        player[-1] -= sp.mana
        invest += sp.mana 
        active_spells.append(copy.deepcopy(sp))
        buys.append(sp.mana)
      status = sum(active_spells,Spell(0,0,0,0,0,0))
      player[0] += status.heal
      player[1] += status.mana_add
      boss[0] -= status.damage
      if not players_turn:
        player[0] -= max(1, boss[1] - status.armor)
      for s in active_spells:
        s.duration -= 1
      active_spells = [s for s in active_spells if s.duration > 0]
      if boss[0] <=0  and invest < min_invest:
        min_invest = invest
        break        
      players_turn = not players_turn
  return min_invest    

spells = [Spell(53,4,0,0,0,1), Spell(73,2,2,0,0,1), Spell(113,0,0,7,0,6), Spell(173,3,0,0,0,6), Spell(229,0,0,0,101,5)]

start = pfc()
print(solve(), pfc()-start)

start = pfc()
print(solve(True), pfc()-start)