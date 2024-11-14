#Daniel Tugendhaft 318465291
#task_2 - Student.py

Details = input('Please enter student name (First and last name) and ID separated by space:').split()

if len(Details[2]) == 7 and Details[2].isnumeric() and Details[2][0] == '0':

    print(Details[0] ,Details[1], Details[2] )

else:

    print ('Error')
