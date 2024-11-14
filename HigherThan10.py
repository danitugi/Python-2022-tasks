#Daniel Tugendhaft 318465291
#Program_2 - HigherThan10.py:

List = []

Num = 0

while Num != -1:

    Num = int(input('Please enter a number:'))

    if Num > 10:

        List.append(Num)

print('The numbers are:')
for num in List:
    print ('               ' , end = ' ')
    print(num)

