# since you keep pestering me, mr i.
import string
import random
import functools

END_TRIGGER = 'bye'

def add_question(questions, q, ans, ci):
  questions.append((q, ans, ci))

def add_arith_question(questions, eq, gen):
  ans = eval(eq)
  ind = random.randint(1, gen)
  ansl = [None] * gen
  for a in range(gen):
    if a != ind:
      z = random.randint(1, round(ans) if round(ans) > 0 else random.randint(1, gen))
      tas = ans - z if random.randint(0, 1) == 1 else ans + z
      ansl[a] = random.randint(0, 100) if tas in ansl else tas
    else:
      ansl[ind] = ans
  questions.append((eq, ansl, ind))

def generate_arith_questions(questions, num, divider):
  ops = '*,+,-'.split(',') # removed / and ** because python is gay
  def diff_ranges(diff):
    return (1 if diff < divider else diff * 50, 75 * diff if diff < divider else diff ** 3)
  def appendage(a):
    (l, h) = diff_ranges(a)
    return ' {} {}'.format(random.choice(ops), random.randint(l, h))
  for x in range(1, num):
    diff = random.randint(1, num)
    lgth = diff if diff < divider else round(diff * 1.5)
    buf = str(random.randint(1, 10) if diff < divider else random.randint(100, 3 ** diff))
    for _ in range(0, lgth):
      buf += appendage(diff)
    add_arith_question(questions, buf, 4 if diff < divider else random.randint(5, 10) )
    
def repl(questions):
  correct = 0
  print('say {} to leave anytime.'.format(END_TRIGGER))
  for (q, a, ci) in questions:
    resp = ''
    ans = string.ascii_lowercase[ci]
    options = list(map(lambda x: '{}) {}'.format(string.ascii_lowercase[a.index(x)], x) , a))
    print('{}?\n{}'.format(q, '\n'.join(options)))
    while resp.lower() != END_TRIGGER.lower():
      resp = input('[a -> {}]?'.format(string.ascii_lowercase[len(a) - 1]))
      if not resp.lower() in string.ascii_lowercase or (resp.lower() in string.ascii_lowercase and not resp.lower() in string.ascii_lowercase[:len(a)]):
        print('print a valid letter')
      elif resp.lower() == ans:
        print('correct, moving on')
        correct += 1
        break
      elif resp.lower() in string.ascii_lowercase:
        print('wrong.')
        break
  print('you scored {} out of a total {} points. gj ({}%)'.format(correct, len(questions), (correct / 100) * 100))
  
def main():
  questions = []
  # add_question(questions, "what is 2 + 2", ["4", "5", "6", "-1"], 0 )
  # add_arith_question(questions, '10 / 100', 10)
  n = 10
  generate_arith_questions(questions, n, 8)
  repl(questions)
  
main()
