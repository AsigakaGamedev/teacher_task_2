#Вторая задача

import math

def optimal_burn_time(c1, b1):
  total_hours = c1 * 2
  new_lights = math.floor(total_hours / (b1 * 2))
  total_hours += new_lights * 2
  optimal_burn_time = total_hours / (c1 + new_lights)
  return optimal_burn_time
  
  
c1 = 6
b1 = 3
optimal_burn_time = optimal_burn_time(c1, b1)
print(optimal_burn_time)