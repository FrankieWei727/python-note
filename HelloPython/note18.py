# generating random values

import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(3,8))

members = ['xuan', 'wei', 'yu']
leader = random.choice(members)
print(leader)
