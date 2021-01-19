from time import perf_counter as pfc
import re


def load(file):
  with open(file) as f:
    return [re.findall(r'[\w\d+-]+', x) for x in f]


class Computer:
  def __init__(self, p, a):
    self.p = p.copy()
    self.pc = 0
    self.r = dict(a=a, b=0)

  def run(self):
    while True:
      if self.pc < 0 or self.pc >= len(self.p): return self.r['b']
      pc = self.pc
      progline = self.p[self.pc]
      if len(progline) == 2:
        cmd, a1 = progline
      else:
        cmd, a1, a2 = progline
      if cmd == 'inc': self.r[a1] += 1
      elif cmd == 'hlf': self.r[a1] //= 2
      elif cmd == 'tpl': self.r[a1] *= 3
      elif cmd == 'jmp': self.pc += int(a1)
      elif cmd == 'jie': self.pc += int(a2) if self.r[a1] % 2 == 0 else 0
      elif cmd == 'jio': self.pc += int(a2) if self.r[a1] == 1 else 0
      if self.pc == pc: self.pc += 1


def solve(puzzle):
  c = Computer(puzzle, 0)
  part1 = c.run()
  c = Computer(puzzle, 1)
  return part1, c.run()


puzzle = load('Tag_23.txt')

start = pfc()
print(solve(puzzle), pfc()-start)