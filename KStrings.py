#Daniel Tugendhaft 318465291
#task_4 - KStrings.py :

Ltrs = input('Search for a sequence of letters in:')
#Ltr -> letter

Seq = int(input('Sequence length:'))
#Seq -> Sequence

Lastltr = 'last'

Counter = 1

TheLtr = 'TheLtr'

for Ltr in Ltrs:

    if Ltr == Lastltr:

        Counter = Counter + 1
        TheLtr = Ltr

    else:

        if Counter == Seq:
            
            break
        
        Lastltr = Ltr
        Counter = 1
    
print ('For length', Seq, ', found the substring', TheLtr,'!')
        


