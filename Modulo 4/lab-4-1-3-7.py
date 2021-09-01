def isYearLeap(year):
    if year%4 or (not(year%4) and not(year%100) and year%400):
        return False
    elif (year%100 and not(year%4)) or (not(year % 4) and not(year%100) and not(year%400)):
        return True

def daysInMonth(year, month):
    if isYearLeap(year):
        Months = [31,29,31,30,31,30,31,31,30,31,30,31]
        return Months[(month-1)]
    else:
        Months = [31,28,31,30,31,30,31,31,30,31,30,31]
        return Months[(month-1)]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")