def isYearLeap(year):
    if year%4 or (not(year%4) and not(year%100) and year%400):
        return False
    elif (year%100 and not(year%4)) or (not(year % 4) and not(year%100) and not(year%400)):
        return True

def daysInMonth(year, month):
    Months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year):
        Months[1] = 29
    else:
        Months[1] = 28
    return Months[(month-1)]

def dayOfYear(year, month, day):
    if day>0 and day<32 and month>0 and month<13 and daysInMonth(year, month)>=day:
        dia=0
        for i in range(1,month+1):
            if i==month:
                dia += day
            else:
                dia += daysInMonth(year, i)
    else:
        return None
    return dia

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 82, 1, 11]
testDays = [15, 21, 31, 101]
testResults = [46, None, 31, None]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    da = testDays[i]

    print(yr, mo, da, "->", end="")
    result = dayOfYear(yr, mo, da)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")

