from random import randint

class Dice:
  def d3():
    return randint(1,3)
  def d4():
    return randint(1,4)
  def d6():
    return randint(1,6)
  def d8():
    return randint(1,8)
  def d10():
    return randint(1,10)
  def d12():
    return randint(1,12)
  def d20():
    return randint(1,20)
  def d100():
    return randint(1,100)

  def isCritSuccess(roll):
    return roll == 20
  def isCritFail(roll):
    return roll == 1

  def advantage(func):
    results = [func(), func()]
    print("With advantage, rolled", max(results), "from", results, "with", func.__name__)
    return max(results)

  def disadvantage(func):
    results = [func(), func()]
    print("With disadvantage, rolled", min(results), "from", results, "with", func.__name__)
    return min(results)
  
  def roll(dice):
    results = [(d(), d.__name__) for d in dice]
    print("Rolled", sum([r[0] for r in results]), "from", results)
    return sum([r[0] for r in results])

