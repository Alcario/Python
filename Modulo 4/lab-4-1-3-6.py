def isYearLeap(year):
    if year%4 or (not(year%4) and not(year%100) and year%400):
        return False
    elif (year%100 and not(year%4)) or (not(year % 4) and not(year%100) and not(year%400)):
        return True

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")