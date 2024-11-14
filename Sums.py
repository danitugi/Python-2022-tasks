#Daniel Tugendhaft 318465291
#Program_3 - Sums.py:

Nums = input('Please enter the numbers (separated by space):').split() #list of the numbers

Len = len(Nums)

for x in range(0,Len) :

    Nums[x] = int(Nums[x])

for x in range(-2,Len) :

    for y in range(x,Len) :

        for z in range(y,Len) :

            if Nums[x] + Nums[y] == Nums[z] and x != y != z :

                print(Nums[x],'+',Nums[y],'=',Nums[z])
