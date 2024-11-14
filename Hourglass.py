#Daniel Tugendhaft 318465291
#Program_1 - Hourglass.py:

Num = int(input('Please enter a number of rows:'))

for x in range(Num,1,-2):
    
    for space in range(0,Num-x):

        print(' ', end = '' )
            
    for star in range(1,x+1):

        print('*', end = ' ' )

    print()

if Num % 2 == 0 :
    for x in range(2,Num+2,2):

        for space in range(Num-x,0,-1):

            print(' ', end = '' )

        for star in range(1,x+1):

            print('*', end = ' ' )

        print()

else :
    for x in range(1,Num+1,2):

        for space in range(Num-x,0,-1):

            print(' ', end = '' )

        for star in range(1,x+1):

            print('*', end = ' ' )

        print()

