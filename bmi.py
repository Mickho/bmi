weight = input('PLease input your weight:')
hight = input('Please input your hight:')
weight = int(weight)
hight = int(hight)/100
bmi = weight/(hight**2)
bmi = float(bmi)
print('Your BMI=', bmi)
if bmi >= 18.5 and bmi <= 24:
    print('Your bmi is:', bmi, '正常範圍')
elif bmi < 18.5:
	print('Your bmi is:', bmi, '體重過輕')
elif bmi <= 24 and bmi < 27:
    print('Your bmi is:', bmi, '過重')
elif bmi <= 27 and bmi < 30:
    print('Your bmi is:', bmi, '輕度肥胖')
elif bmi <= 30 and bmi < 35:
    print('Your bmi is:', bmi, '中度肥胖')
else :
	print('Your bmi is:', bmi, '重度肥胖')