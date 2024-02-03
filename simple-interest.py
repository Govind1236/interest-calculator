def getfloat(hint):
    return float(input(hint))

def cal_int(principle, time, rate):
    if principle <= 0 or time <= 0 or rate <= 0:   
        print("Value cannot be less than equal to zero")
        return 
    interest = principle * time * rate / 100 
    return interest

principle = getfloat("Enter Principle: ")
time = getfloat("Enter Time: ")
rate = getfloat("Enter Rate:")
interest = cal_int(principle = principle, time = time, rate = rate)
print("Your accumulated interest is: ", interest)