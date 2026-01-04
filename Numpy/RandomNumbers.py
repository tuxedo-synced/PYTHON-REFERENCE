import numpy as np 

rng = np.random.default_rng()

#   rng.integers(low,high) [low,high)
print(f"The die results: {rng.integers(low=1,high=7)}")

#   rng.integers(low,high,size)  [low,high)
print(f"The number spinned is: {rng.integers(low=1,high=101,size=(3))}") 
print(f"The number spinned is: {rng.integers(low=1,high=101,size=(4,4))}") 

# if you want same values but random for once we use seed parameter and set it to 1 .

rng2 = np.random.default_rng(seed=1)
print(f"The number spinned is: {rng2.integers(low=1,high=101,size=(4,4))}") 

#  for floating point numbers
print(f"I need 3 random floating point numbers: {np.random.uniform(low=-1,high=1,size=(3))}")

# shuffle an array 
# already created object named rng so can use its methods .
# same here too -> if seed is set to 1 the values will be shuffled only once and once set .
array_1 = np.array([1,2,3,4,5])
rng.shuffle(array_1)
rng2.shuffle(array_1)
print(array_1)
print(array_1)
