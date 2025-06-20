import time
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_digits = "₀₁₂₃₄₅₆₇₈₉"
⁷
def smaller_digits(num):
	for i in range(10):
		num = num.replace(f"{i}",small_digits[i])
	return num.replace('-','₋')

def conv(num, base):
	
	if len(num) > 1:
		frac = num[1]
	else:
		frac = "0"

	integ = int(num[0])
	integ = conv_int(integ, base)
	if frac != 0 and frac != '0':
		limited = input("Limit the fraction (skip for seeing full): ").lower()
		if limited != '':
			while True:
				try:
					int(limited)
					break
				except ValueError:
					print("\033[0;31mEntered value is not a number.\033[0;0m")
				except int(limited) < 0:
					print("\033[0;31mLength cannot be less than zero!\033[0;0m")
			lim = int(limited)
			frac = conv_frac_limited(frac, base,lim)
		else:
			frac = conv_frac(frac, base)
	if integ == '':
		integ = '0'
	if frac == '':
		frac = '0'
	result = integ 
	
	if base < 0 and int(num[0]) > 0:
		if frac != '0':
			result = conv_int_alt(int(num[0]), base)+smaller_digits(str(base)) + ' – 0.' + frac +smaller_digits(str(base)) +  '\nAlt: ' + result +  '.' + frac +  smaller_digits(str(base))
		else:
			result = conv_int_alt(int(num[0]), base) + '.0' +smaller_digits(str(base)) +  '\nAlt: ' + result +  '.0' +  smaller_digits(str(base))
			
	elif base < 0 and int(num[0]) < 0:
		if frac != '0':
			result = '–' + conv_int_alt(int(num[0])*(-1), base) + '.' + frac +smaller_digits(str(base)) +  '\nAlt: ' + result +smaller_digits(str(base)) +  '– 0.' + frac +  smaller_digits(str(base))
		else:
			result = '–' + conv_int_alt(int(num[0])*(-1), base) + '.0' +smaller_digits(str(base)) +  '\nAlt: ' + result +  '.0' +  smaller_digits(str(base))
	else:
		result += '.' + frac +smaller_digits(str(base))
	return result


def conv_int(integ, base):
	isNegative = False
	
	if base < 0:
		integ*=(-1)
		
	if integ < 0:
		integ*=(-1)
		isNegative = True
	
	integer_part = ''

	if base < 36 and base > -36:
		while integ != 0:
			#print(integ,base,abs(integ%base), integ//base)
			integer_part = digits[abs(integ%base)] + integer_part
			integ//=base
	else:
		while integ != 0:
			integer_part = f"[{abs(integ%base)}]" + integer_part
			integ//=base
	if integer_part == '':
		integer_part = '0'
	if isNegative:
		return "–" + integer_part
	return integer_part
	
	
def conv_int_alt(integ_alt, base):
	integer_part_alt = ''
	if abs(base) < 36:
		while integ_alt != 0:
			rem = -(integ_alt//(abs(base)))
			integer_part_alt = digits[integ_alt-(rem*base)] + integer_part_alt
			integ_alt = rem
	else:
		while integ_alt != 0:
			rem = -(integ_alt//(abs(base)))
			integer_part_alt = f"[{integ_alt-(rem*base)}]" + integer_part_alt
			integ_alt//=base
	if integer_part_alt == '':
		return '0'
	return integer_part_alt
	
def conv_frac(frac, base):
#converting fraction part of number
	fraction_part = ''
	length = 10**len(frac)
	frac = int(frac)


	if base%5==0 and base%2==0 and frac != 0:

		if base < 36:
			while frac != 0:
				frac = (frac*base)
				fraction_part = fraction_part + digits[abs(frac//length)]
				frac%=length

		else:
			while frac != 0:
				frac = (frac*base)
				fraction_part = f"[{abs(frac//length)}]" + fraction_part
				frac%=length

	elif frac != 0:
		fraction_part = []
		used = []
		count = 0
		if base < 36:
			while frac not in used:
				used.append(frac)
				count+=1
				frac = (frac*base)
				fraction_part.append(digits[abs(frac//length)])
				frac%=length

		else:
			while frac not in used:
				used.append(frac)
				count+=1
				frac = (frac*base)
				fraction_part.append("["+f"{abs(frac//length)}"+"]")
				frac%=length

		i = used.index(frac)
		#print(used)
		period = f"({''.join(fraction_part[i:count])})"
		if period != '(0)' and period != '([0])' :
			fraction_part = ''.join(fraction_part[0:i]) + period
		else:
			fraction_part = ''.join(fraction_part[0:i])

	if length == '':
		return '0'
	return fraction_part

#def Round(fraction_part,base):
#	nth = int(input("Digits after the point: "))
def conv_frac_limited(frac, base,lim):
#converting fraction part of number
	fraction_part = ''
	length = 10**len(frac)
	frac = int(frac)
	
	if base < 36:
		for _ in range(lim):
			if frac == 0:
				break
			frac = (frac*base)
			fraction_part = fraction_part + digits[abs(frac//length)]
			frac%=length

	else:
		for _ in range(lim):
			if frac == 0:
				break
			frac = (frac*base)
			fraction_part = f"[{abs(frac//length)}]" + fraction_part
			frac%=length
		
	if fraction_part == '':
		return '0'
	#print(fraction_part)
	if frac > 0:
		fraction_part += '…'
	return str(fraction_part)
		
def conv_comm_frac(num, denom,base):
	frac = '.'
	if abs(base) < 36:
		if base % denom == 0 or denom % base == 0:
			while num != 0:
				num *= base
				frac += digits[abs(num//denom)]
				num %= denom
			return frac
		else:
			used = []
			fraction_part = []
			count = 0
			while num not in used:
				used.append(num)
				count += 1
				num *= base
				fraction_part.append(f'{digits[abs(num//denom)]}') 
				num %= denom

			id = used.index(num)
			
			period = ''.join(fraction_part[id:count])
			if period != '0':
				frac +=  ''.join(fraction_part[0:id]) + f'({period})'
				return frac
			frac +=  ''.join(fraction_part[0:id])
			if frac == '.':
				return '.0'
			
	else:
		if base % denom == 0 or denom % base == 0:
			while num != 0:
				num *= base
				frac += f'[{abs(num//denom)}]'
				num %= denom
			return frac
		else:
			used = []
			fraction_part = []
			count = 0
			while num not in used:
				used.append(num)
				count += 1
				num *= base
				fraction_part.append(f'[{str(abs(num//denom))}]')
				num %= denom

			id = used.index(num)
			#print(fraction_part)
			period = ''.join(fraction_part[id:count])
			if period != '[0]':
				frac +=  ''.join(fraction_part[0:id]) + f'({period})'
				return frac
			frac +=  ''.join(fraction_part[0:id])
	return frac
	
#	return 0
#b35 = smaller_digits("35")
#b10 = smaller_digits("10")
#for num in range(0,100000):
#	print(f'{conv_int(num,35)}{b35} = {num}{b10}')

def b10(num,base):
	if base == 10:
		return int(num)
	num_b10 = 0
	if base < 36:
		num = num[::-1]
		for d in range(len(num)):
			num_b10 += digits.index(num[d])*(base**d)
	else:
		num = num.split(')(')
		num[0].replace('(','')
		num[-1].replace(')','')
		num = num[1:-1:]
		for d in range(len(num)):
			num_b10 += int(num[d])*(base**d)
	return num_b10

prev_num = '0'
prev_base = 0
while True:
	while True: 
		try:
			num = input("Enter a number: ")
			if num == '':
				num = prev_num + ''
				print("\033[0;32mEntered value is empty, previous one will be used.\033[0;0m")
			prev_num = num + ''
			if '/' in num and num.count('/') == 1:
				break
			if ',' not in num or num.count(',') > 1:
				float(num)
				break
			print("Try again.")
		except ValueError:
			print("\033[0;31mEntered value is not a number.\033[0;0m")
	num.replace(',','.')
	if num[0] == '.':
		num = ('0' + num).split('.')
	elif '.' not in num and '/' not in num:
		num = (num+'.0').split('.')
	elif '/' not in num:
		num = num.split('.')

	while True:
		try:
			base = input("Enter the base the number will be converted to: ")
			if base == '':
				base = prev_base + 0
				if prev_base != 0:
					print("\033[0;32mEntered value is empty, previous one will be used.\033[0;0m")
			prev_base = int(base)
			base = int(base)
			1/base
			break
		except ValueError:
			print("\033[0;31mExpected integer.\033[0;0m")
		except ZeroDivisionError:
			print("\033[0;31mBase must not be zero nor fraction.\033[0;0m")
			
	t = time.time()
	if '/' in num:
		num = num.split('/')
		denom = int(num[1])
		integ = int(num[0])//denom
		numer = int(num[0])%denom
		integ_part = conv_int(integ, base)
		frac_part = conv_comm_frac(numer, denom,base)
		print(f'{integ_part}{frac_part}'+smaller_digits(str(base)))
	else:
		number = conv(num,base)
		print(number)# + f'\nCalculating time: ~{round(t,3)}s')