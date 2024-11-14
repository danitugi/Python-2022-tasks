#Daniel Tugendhaft 318465291
#Program_4 - DividedByX.py:

Num = int(input('Please enter a number:')) 

List = []

AnsList = []

for x in range(1,92,10) :

    for num in range(x,x+10) :

        if num % Num == 0 :

            List.append(num)

        else :

            List.append(' ')

    AnsList.append(List)

    List = []

print(AnsList)

#Done
