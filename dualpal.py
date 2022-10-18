"""
ID: daaweso1
PROG: dualpal
LANG: PYTHON3
"""
num = open('dualpal.in', 'r').read()
nums = list(map(int, num.split()))
N = nums[0]
S = nums[1]
#print(nums)
#for i in range(9, 0, -1):
#O(logN) for base calculations
final = []
def convert(num, base):
  lst = []
  q,r = divmod(num, base)
  # 15,3 = 5,0
  lst.append(r)
  while(q != 0):
    n,p = divmod(q, base)
    lst.append(p)
    q = n
  rev = list(reversed(lst))
  # print(rev)
  return ''.join(str(e) for e in rev)
  
def is_palindrome(num):
  lst = [int(x) for x in str(num)]
  rev = list(reversed(lst))
  #O(n)
  for i in range(len(lst)):
    # print(i)
    if(rev[i] == lst[i]):
      continue
      return True
    else:
      return False
  return True

i = S + 1 # start counting numbers that are GREATER than
while(len(final)< N):
  count = 0
  for base in range(2,11):
    b = convert(i, base)
    if is_palindrome(b):
      count +=1
      if(count == 2):
        break
  if(count == 2):
    final.append(str(i))
    if(len(final) == N):
      break
  #print(i)
  i +=1
#print(final)
fout = open("dualpal.out", "w")
fout.write('\n'.join(final) + '\n')
fout.close()
