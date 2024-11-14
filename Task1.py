## daniel tugendhaft, 318465291, 4212510-01

#porgram n.1
fname = input('Please enter your first name: ')
lname = input('Please enter your last name: ')
print('Your name:', (fname),', Your last name', (lname))
print('      ')
print('*****************************')
print('      ')
 
#porgram n.2
num3 = input('Please enter a number: ')
print ('Reverse number:' ,num3[2],num3[1],num3[0])
print('      ')
print('*****************************')
print('      ') 

#porgram n.3
print ('Banknote printing program:')
num = int(input('Please enter number: '))
if num == 0 :
  print ('Error: You entered the number 0 !')
elif num < 0 :
  print('Error: You entered a negetive number !')
elif  num > 0:
  S200 = num/200
  S200 = int(S200)
  S100 = num/100 - 2*S200
  S100 = int(S100)
  S50 = num/50 - 2*S100 - 4*S200
  S50 = int(S50)
  S20 = num/20 - (5/2)*S50 - 5*S100 - 10*S200
  S20 = int(S20)
  S10 = num/10 - 2*S20 - 5*S50 - 10*S100 - 20*S200
  S10 = int(S10)
  S5 = num/5 - 2*S10 - 4*S20 - 10*S50 - 20*S100 - 40*S200
  S5 = int(S5)
  S2 = num/2 - (5/2)*S5 - 5*S10 - 10*S20 - 25*S50 - 50*S100 - 100*S200
  S2 = int(S2)
  S1 = num - 2*S2 - 5*S5 - 10*S10 - 20*S20 - 50*S50 - 100*S100 - 200*S200
  S1 = int(S1)
  print ('200 =', S200)
  print('100 =', S100)
  print('50 =', S50)
  print('20 =', S20)
  print('10 =', S10)
  print('5 =', S5)
  print('2 =', S2)
  print('1 =', S1)
print('   ')
print('*******************************')
print('   ')
  
#porgram n.4
print('A plan to print the percentage of tax to be paid on wages:')
Salary = input('Please enter your salary:')  
Salary = int(Salary)
if Salary < 0 : 
  print('Error: Input must be a positive number')
elif Salary == 0:
  print('your tax is 0%')
elif  0 < Salary < 10000:
  print('your tax is 10%')
elif  10000 < Salary < 20000:
  print('your tax is 20%')
elif  20000 < Salary < 30000:
  print ('your tax is 30%')
elif  30000 < Salary :
  print ('your tax is 40%')
print ('     ')
print ('************ Finish *************')