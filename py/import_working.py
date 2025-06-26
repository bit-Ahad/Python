# # It will import mentioned functions
# from math import sqrt , pi

# # It will import all functions of module
# from math import *

# # It will just change the name of module
import math as m
print(m.sqrt(947673456))
from math import sqrt as s
print(s(144))

import math
print(math.sqrt(32432))

# It print all functions avaliable in module
print(dir(math))