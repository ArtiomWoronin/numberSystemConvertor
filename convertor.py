numRaw = input("Enter your number using decimal number system: ").replace(' ', '')
def factors(x):
	factorList = []
	for d in range(2,x // 2):
		if x % d == 0:
			factorList.append(d)
	factorList += [x // 2,x]
	return factorList



if '.' in numRaw and numRaw[0] != '.':
	numRaw = numRaw.split('.')
	number = int(numRaw[0])
	period = numRaw[1]
elif numRaw[0] == '.':
	number = 0
	period = numRaw[1::]
else:
	number = int(numRaw)
	period = ''
numSys = int(input("What number system do you want to convert this number in?(must be integer): "))



if numSys == 1 and period == '':
	print('1' * number, '\nAre you good now?')
	quit()
elif (numSys != int or numSys == 1) and period == '':
	print("Wrong value!")
	quit()

factorList = factors(numSys)

digits = []
digitDict = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")



if number != 0:
	remainder = number % numSys
	n = 0
	numOut = ''
	numOutPeriodRaw = ''
	if numSys <= 36:
		while number != 0:
			digits.insert(0, digitDict[number % numSys])
			number = number // numSys
	else:
		while number != 0:
			digits.insert(0, '('  +  str(number % numSys)  +  ')')
			number = number // numSys
	numOut = ''.join(digits)
else:
	numOut = '0'



if period != '':
	numOutPeriodRaw = ''
	periodLen = len(period)
	power = input("Please, enter your fractional precision: ")
	roundFlag = input("Round? Y/n ").lower()


	if ('max' in power) and numSys < 10:
		power = len(period) * len(period) + 1
	elif ('max' in power) and numSys >= 10:
		if 2 in factorList and 5 in factorList:
			power = len(period)
		else:
			power = len(period) * len(period) + 1
	else:
		power = int(power)



if period == '' or power < 1:
	numOutPeriodRaw = ''

elif period != '0' and numSys <= 36:
	i = 0
	numOutPeriodRaw = ''
	while i <= power:
		periodRaw = str(int(period) * numSys)[:-periodLen:]
		if periodRaw != '':
			numOutPeriodRaw += digitDict[int(periodRaw)]
		else:
			numOutPeriodRaw += '0'
		period = str(int(period) * numSys)[-periodLen::]
		i += 1
	numOutPeriodRaw = '.' + numOutPeriodRaw

elif period != '' and numSys > 36:
	i = 0
	numOutPeriodRaw = ''
	while i <= power:
		periodRaw = str(int(period) * numSys)[:-periodLen:]
		if periodRaw != '':
			numOutPeriodRaw += '(' + periodRaw + ')'
		else:
			numOutPeriodRaw += '(0)'
		period = str(int(period) * numSys)[-periodLen::]
		i += 1
	numOutPeriodRaw = '.' + numOutPeriodRaw

if 'y' in roundFlag:
	numOutPeriodRaw = list(numOutPeriodRaw)
	if numSys%2 == 0:
		numHalf = numSys // 2
	else:
		numHalf = numSys // 2 + 1
	if numSys <= 36:
		for i in range(len(numOutPeriodRaw)-1, 1, -1):
			if digitDict.index(numOutPeriodRaw[i]) >= numHalf:
				numOutPeriodRaw[i-1] = digitDict[digitDict.index(numOutPeriodRaw[i-1]) + 1]
				numOutPeriodRaw[i] = ''
				print(numOut + ''.join(numOutPeriodRaw))
				quit()
			else:
				numOutPeriodRaw[i] = ''
	else:
		for i in range(len(numOutPeriodRaw)-1, 1, -1):
			if int(numOutPeriodRaw[i].replace('(','').replace(')','')) >= numHalf:
				numOutPeriodRaw[i-1] = str(int(numOutPeriodRaw[i-1].replace('(','').replace(')','')) + 1)
				numOutPeriodRaw[i] = ''
				print(numOut + ''.join(numOutPeriodRaw))
				quit()
			else:
				numOutPeriodRaw[i] = ''


print(numOut + numOutPeriodRaw)
