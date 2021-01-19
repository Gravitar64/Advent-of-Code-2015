from time import perf_counter as pfc
import random as rnd
import copy

class Actor:
  def __init__(self, hp, damage, mana):
    self.hp = hp
    self.damage = damage
    self.mana = mana

class Spell:
  def __init__(self, cost, damage, heal, armor, mana_add, timer):
    self.cost = cost
    self.damage = damage
    self.heal = heal
    self.armor = armor
    self.mana_add = mana_add
    self.timer = timer

  def __add__(self, other):
    return Spell(0, self.damage + other.damage, self.heal + other.heal, self.armor + other.armor, self.mana_add + other.mana_add, 0)

  def __eq__(self, other):
    return self.cost == other.cost

def solve(part2=False):
  min_invest = 99999
  for n in range(20_000):
    boss, player = Actor(51,9,0), Actor(50,0,500)
    invest, players_turn, active_spells  = 0, True, []
    while player.hp >= 0:
      if players_turn:
        if part2:
          player.hp -= 1
          if player.hp <= 0:
            break
        valid_spells = [s for s in spells if s.cost <= player.mana and s not in active_spells]
        if not valid_spells: break
        sp = copy.deepcopy(rnd.choice(valid_spells))
        player.mana -= sp.cost
        invest += sp.cost 
        active_spells.append(sp)
      status = sum(active_spells,Spell(0,0,0,0,0,0))
      player.hp += status.heal
      player.mana += status.mana_add
      boss.hp -= status.damage
      if not players_turn:
        player.hp -= max(1, boss.damage - status.armor)
      for s in active_spells:
        s.timer -= 1
      active_spells = [s for s in active_spells if s.timer > 0]
      if boss.hp <=0  and invest < min_invest:
        min_invest = invest
        break        
      players_turn = not players_turn
  return min_invest    

spells = [Spell(53,4,0,0,0,1), Spell(73,2,2,0,0,1), Spell(113,0,0,7,0,6), Spell(173,3,0,0,0,6), Spell(229,0,0,0,101,5)]

start = pfc()
print(solve(), pfc()-start)

start = pfc()
print(solve(True), pfc()-start)