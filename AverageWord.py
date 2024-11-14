#Daniel Tugendhaft 318465291
#task_3 - AverageWord:

lst = input('Please enter your sentence/list - separated by space:').split()

SumLtr = 0

Anser = 0

Wrds = len(lst)

for i in range(Wrds):

    SumLtr = SumLtr + len(lst[i])

Average = round(SumLtr/Wrds)

for i in range(Wrds):

    if Average < len(lst[i]):

        Anser = Anser + 1
        
print ('The number of strings longer than the average is:', Anser)
