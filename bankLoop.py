#VARIABLES
totalD = 0
totalW = 0
totalI = 0
year = 12

#CODE BEGINS HERE
balance = int(input('What is your starting balance'))
apy = float(input('What is the anual interest rate'))
   
for deposit in range(3):
   deposit = int(input('How much was deposited this month:'))
   withdrawal = int(input('How much was withdrawn this month:'))
   totalD += deposit
   totalW += withdrawal
   endingBalance = (balance + totalD - totalW)   
   interest = ((apy/year)/100)
   totalI = (interest * endingBalance)
   endingBalance = endingBalance + totalI

print 'Your starting balance was:',balance
print 'The toal amount deposited for the last 3 months is:',totalD
print 'The total amount withdrawn for the last 3 months is:',totalW
print 'You accumulated',totalI,'dollars in interest'
print 'Your remaining balance is:',endingBalance
