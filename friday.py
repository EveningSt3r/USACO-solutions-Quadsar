
"""
ID: daaweso1
LANG: PYTHON3
TASK: friday
"""

""" 
Set constants for each month, read first (and only) line of text file of #years, 
intialize dictionary with month values (0 = january) 
Check for every year whether the modulo 4 is 0, (leap year) N cannot exceed 400 so the only
century leap is 2000. Disregard other century leaps. Append to a list
"""
fin = open("friday.in", "r").read().splitlines()
years = int(fin[0])
# print(years)
months = {}
"""
for i in range(12):
  if(i == 0 or 2 or 4 or 6 or 7 or 9 or 11):
    months[i] = 31
  elif(i == 3 or 5 or 8 or 10):
    months[i] = 30
  else: 
    months[i] = 28
"""
months[0] = 31
months[1] = 28
months[2] = 31
months[3] = 30
months[4] = 31
months[5] = 30
months[6] = 31
months[7] = 31
months[8] = 30
months[9] = 31
months[10] = 30
months[11] = 31
    

days = [0] * 7 # monday is first
# print(days)
# print(months)
leaps = []
for j in range (1900, 1900+years): # inclusive makes the N-1 part negligible, 1900 to 1919
  # print("Checking: " + str(j))
  if(j % 400 == 0 and j % 100 == 0):
    leaps.append(j)
  elif(j % 100 != 0 and j % 4 == 0):
    leaps.append(j)

# print(leaps)
"""
Iterate through years, then months. Create an array of days with 7 elements, initalized at 0.
days[0] = monday value. Initialize a day at 0. (Jan 1, 1900 monday) 
"""

weekday = 1
for y in range(1900, 1900+years):
  # print("Iterating year: " + str(y))
  if y in leaps:
    months[1] = 29
  else:
    months[1] = 28
  for m in range(12):
    # print("Iterating month " + str(m) + " of year " + str(y))
    day = 1
    for d in range(months[m]):
      # print("Iterating day " + str(day))
      day = day + 1
      weekday = weekday + 1
      if(weekday >= 7):
        weekday = 0
      if(day == 13):
        days[weekday] += 1

print(days)
""" 
print(str(days[5] + str(" ") + str(days[6])) + str(" ") + 
     str(days[0]) + str(" ") + str(days[1]) + str(" ") + str(days[1]) + str(" ") + str(days[2] + str(" ") + str(days[3]) + str(" ") + str(days[4]))) 
     """

# print(str(days[5]) + " " + str(days[6]) + " " + str(days[0]) + " " + str(days[1]) + " " + str(days[2]) + " " + str(days[3]) + " " + str(days[4]))

fout = open('friday.out', 'w')
fout.write((str(days[6]) + " " + str(days[0]) + " " + str(days[1]) + " " + str(days[2]) + " " + str(days[3]) + " " + str(days[4]) + " " + str(days[5])) + "\n")
fout.close()