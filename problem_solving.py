import numpy as np
import re

# Uncomment and implement two of the following.  Refer to the Problem solving brief for specifications.

def censor(s):
    words=s.split(" ")
    l=len(words)
    print(words)
    print(l)
    for i in range(l):
        if re.match(words[i],'a') or re.match(words[i],'an') or re.match(words[i],'the') :
            print('on est la')
            words[i]=len(words[i])*'#'
    r=" ".join(words)
    return r

 def fertiliser(an, ap, bn, bp, n, p):
   det=an*bp-ap*bn
   if det==0:
      return None
   else:
      mat=np.array([[an,bn],[ap,bp]])
      vector=np.array([[n],[p]])
      amswer=np.linalg.inv(mat)@vector
      a=answer[[0]]
      b=answer[[1]]
      return a, b

# def makeBet(headsOdds, tailsOdds, previousOutcome, state):
#  # bet =
#  # state = 
#  return (bet, state)


# The following will be run if you execute the file like python3 problem_solving.py
# Your solutions should not depend on this code.
# The automated marker will ignore any changes to this code; feel free to modify it
# but keep the if and the indenting as is
if __name__ == '__main__':
   try:
      print(censor('The cat ate a mouse.')) # should give "### cat ate # mouse. <n1234567>"
   except NameError:
      print("Not attempting censoring problem")

   try:
      print(fertiliser(1, 0, 0, 1, 2, 2)) # should give (2.0, 2.0)
   except NameError:
      print("Not attempting fertiliser problem")

   import random
   try:
      random.seed(0)
      totalprofit = 0
      for round in range(10000):
         if random.randint(0,1) == 0:
            headsprob = 0.7
         else:
            headsprob = 0.4

         previousOutcome = None
         state = None
         profit = 0
         odds = dict()
         for _ in range(100):
            odds['heads'] = random.uniform(1, 3)
            odds['tails'] = random.uniform(1, 3)
            
            bet, state = makeBet(odds['heads'], odds['tails'], previousOutcome, state)
            
            previousOutcome = 'heads' if random.random() < headsprob else 'tails'
            if bet == previousOutcome:
               profit += odds[bet] - 1
            elif bet != 'no bet':
               profit -= 1          # stake lost

         print("Probability of heads was", headsprob, "Profit was", profit)
         totalprofit += profit
      print("Average profit per run:", totalprofit / 10000)

   except NameError as e:
      print("Not attempting probability problem")