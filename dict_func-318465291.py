#Daniel Tugendhaft 318465291
#Program_4 - Dictionary_Functions.py:

####Q1

import random
import math

def dices_many_times(num):
    if 1<num<13:
        rndm10k = int(random.random()*10000)+1000 #randon in 10k
        counter=0
        for i in range(rndm10k):
            if num == math.ceil(1+(random.random()*11)):
                counter += 1
        return counter/rndm10k

    else :
        print (num, 'not possible')
            
for num in range(2,13):
        print(num, '    ', dices_many_times(num))



####Q2

##def area_to_perimeter(Area):
##    Perimeter=(Area**0.5)*4
##    return (Perimeter)
##
##Num = 5 #int(input('Please enter the side of a square:'))
##NumArea = Num**2
##print('The perimeter of the square is',int(area_to_perimeter(NumArea)))
##
##Num = 3 
##NumArea = Num**2
##print('The perimeter of the square is',int(area_to_perimeter(NumArea)))



####Q3
##
##def division_remainder(num1,num2):
##    return (num1%num2)
##
##print('The division remainder from 5/3 is:',division_remainder(5,3))
##print('The division remainder from 19/5 is:',division_remainder(19,5))
