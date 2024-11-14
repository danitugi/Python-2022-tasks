#Daniel Tugendhaft 318465291
#Assiment 4 - Dictionary.py:

##Question 1

D = {}
    
for NumLtr in range(97, 123): #The number that represents the letter
    D[chr(NumLtr)] = NumLtr - 96
   
for key, value in D.items():
    print(key, ' : ', value)



##Question 2

Wrd = input('In which word to look, for the most common letter?')
WrdD = {}    #The word dictionary
Bgst = 0     #The most common letter
Anser = '' 

for Ltr in Wrd :
    WrdD[Ltr] = WrdD.get(Ltr,0) + 1
    if WrdD[Ltr] > Bgst :
        Bgst = WrdD[Ltr]
        
for Ltr in WrdD:
    if WrdD[Ltr]==Bgst:
        Anser += Ltr

Anser = sorted(Anser)
Anser = ','.join(Anser)
        
print('The most common letter/s:', Anser)



##Question 3

name = input('Enter your input:')
num = int(input('What is the length of the letters to test?'))
x = 0
D = {}
lst = []

for i in range(len(name)):
    lst.append(name[i:i+num])  
for ltrs in lst :
    if ltrs not in D and len(ltrs) == num:
        D[ltrs] = [x]
    elif ltrs in D:
        D[ltrs].append(x)
    x += 1
print(D)
