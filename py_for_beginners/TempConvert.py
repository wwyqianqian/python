val = input("Please input the temperature (Celsius or Fahrenheit) :")
if val[-1] in ['C', 'c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("It is %.2fF"%f)
elif val[-1] in ['F', 'f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("It is %.2fC"%c)
else:
    print("type error")
