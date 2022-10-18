import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      self.key = value
      if value > 1:
        for i in range(value):  
          self.contents.append(str(key))

  def draw(self, num_draw):
    if num_draw > len(self.contents):
      print("Error:Insufficient amount of balls")
      return self.contents
    else:
      counter = 0
      random_balls = []
      while counter < num_draw:
        random_item = random.choice(self.contents)
        self.contents.remove(random_item)
        random_balls.append(random_item)
        counter += 1
      return random_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successes = 0
  for j in range(num_experiments):
    new_hat = copy.deepcopy(hat)
    experim = new_hat.draw(num_balls_drawn)
        
    balls_drawn = []
    for key, value in expected_balls.items():
      for i in range(value):
        balls_drawn.append(key)
    
    match_ball = 0
        
    for i in balls_drawn:
      if i in experim:
        experim.remove(i)
        match_ball += 1
    
      if match_ball == len(balls_drawn):
        successes += 1
    
    if successes == 0:
        return 0
    else:
        return successes / num_experiments

