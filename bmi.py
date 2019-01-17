weight = input('PLease input your weight:')
hight = input('Please input your hight:')
weight = int(weight)
hight = int(hight)/100
bmi = weight/(hight**2)
bmi = float(bmi)
print('Your BMI=', bmi)
if bmi >= 18.5 and bmi <= 24:
    print('Your bmi is normal')
elif bmi < 18.5:
	print('Your bmi is low')
else :
	print('Your bmi is high')