#Daniel Tugendhaft 318465291
#Program_8 - Recursion_Files.py:

####Q1

##def flipStr(Str):
##  return Str if len(Str) == 1 else Str[-1] + flipStr(Str[0:-1])
##
##print(flipStr('Str'))


####Q2

##def smallestNum(lst,min=10**10):
##  if len(lst) == 0:
##    return min if min != 10**10 else -1
##  if  min > lst[0]:
##    min = lst[0]
##  return smallestNum(lst[1:],min)
##
##nums = [9,6,12,4]
##print(smallestNum(nums))
##nums = []
##print(smallestNum(nums))



####Q3

from csv import reader
opened_file = open ('AppleStore.csv', encoding="utf8")
read_file = reader (opened_file)
apps_data = list(read_file)

def extract(n):
  Tlist = []
  for app in apps_data[1:]:
    Tlist.append(app[n])
  return (Tlist)

def freq_table(genre):
  gen_dict = {}
  for item in genre:
    if item in gen_dict:
      gen_dict[item] += 1
    else:
      gen_dict[item] = 1
  return gen_dict

def freq_table_ge(n):
  freqTable = freq_table(extract(n))
  counter = 0
  for key,value in freqTable.items():
    if value > counter :
      counter = value
      mostPopular = key
  return freqTable, mostPopular 

freqTable, mostPopular = freq_table_ge(3)

