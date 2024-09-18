# 

import sys
states = []
capitals = []
data = sys.argv
for i in range(1,len(data)):
    state_data = data[i].split()
    states.append(state_data[0])
    capitals.append(state_data[1])

print(f' {'States':20} Captitals')
print("_"*40)
for i in range(len(states)):
    print(f' {states[i]:20} {capitals[i]}')
print("_"*40)