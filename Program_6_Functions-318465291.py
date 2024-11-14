#Daniel Tugendhaft 318465291
#Program_6 - Functions.py:

####Q1

##def mult_even_digits(n):
##    n = [int(x) for x in str(n)]
##    counter = 1
##    for x in n:
##        if x % 2 == 0:
##            counter *= x
##    return counter
##
##print(mult_even_digits(1223))
##print(mult_even_digits(33))
##print(mult_even_digits(324769))
            


####Q2


##def fix_grades(grades):
##    counter = 0
##    grde_loc = 0 #grade_location
##    for grade in grades:
##        if 0 < grade < 51:
##            grades[grde_loc] = 0
##        else:
##            counter += 1
##            if 50 < grade < 61:
##                grades[grde_loc] = 60
##        grde_loc += 1
##    return counter
##
##grades = [19,90,11,51,50]
##print(fix_grades(grades))
##print(grades)



####Q3
##
##def CreateFile(fileName, content):
##
##    outfname = fileName
##    outf = open(outfname, 'w')
##    outf.write(content)
##    outf.close()
##
##
##CreateFile("Yesh.txt", "Python is great,\nit really is!")
