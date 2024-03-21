numRaw = input("Enter your number using decimal number system: ").replace(' ', '')
if '.' in numRaw and numRaw[0]!='.':
	numRaw = numRaw.split('.')
	number = int(numRaw[0])
	period = numRaw[1]
elif numRaw[0]=='.':
	number = 0
	period = numRaw[1::]
else:
	number = int(numRaw)
	period = ''
numSys = int(input("What number system do you want to convert this number in?: "))
digits = []
digitDict = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if number!=0:
	remainder = number%numSys
	n = 0
	numOut = ''
	nOPR = ''
	if numSys<=36:
		while number!=0:
			digits.insert(0, digitDict[number%numSys])
			number = number//numSys
	else:
		while number!=0:
			digits.insert(0, '(' + str(number%numSys) + ')')
			number = number//numSys
	numOut = ''.join(digits)
else:
	numOut = '0'
periodLen = len(period)
nOPR = ''
power = int(input("Please, enter your fractional precision: "))
if period == '' or power<1:
	nOPR = '0'
elif period!='0' and numSys<=36:
	i = 0
	nOPR = ''
	while i<=power:
		periodRaw = str(int(period)*numSys)[:-periodLen:]
		if periodRaw!='':
			nOPR += digitDict[int(periodRaw)]
		else:
			nOPR += '0'
		period = str(int(period)*numSys)[-periodLen::]
		i+=1

elif period!='' and numSys>36:
	i = 0
	nOPR = ''
	while i<=power:
		periodRaw = str(int(period)*numSys)[:-periodLen:]
		if periodRaw!='':
			nOPR += '(' + periodRaw + ')'
		else:
			nOPR += '0'
		period = str(int(period)*numSys)[-periodLen::]
		i+=1
print(numOut+'.'+nOPR)
