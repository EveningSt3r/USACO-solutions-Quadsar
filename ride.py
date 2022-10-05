from typing import Dict
"""
ID: daaweso1
LANG: PYTHON3
TASK: ride
"""

fhand = open('ride.in', 'r').read()


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
modcase1 = 1
modcase2 = 1
line1 = fhand.split('\n', 1) [0]
line2 = fhand.split('\n', 1) [1]
new1 = line1.strip()
new2 = line2.strip()

list1 = list(new1)
list2 = list(new2)
for i in new1:
  num1 = alphabet.index(i)+1
  modcase1 = modcase1*num1

for j in new2:
  num2 = alphabet.index(j)+1
  modcase2 = modcase2*num2
if((modcase1 % 47) == (modcase2 % 47)):
  open('ride.out', 'w').write("GO\n")
else:
  open('ride.out', 'w').write("STAY\n")
""" 
  num = alphabet.index(i)+1
  modcase = modcase*num
  temp = modcase % 47
"""
    
    
  