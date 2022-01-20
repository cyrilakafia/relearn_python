import calendar
print(">>>>>>>Leap Year Calculator<<<<<<<\n")
y1 = int(input("Enter the first year: "))
y2 = int(input("Enter the second year: "))
leaps = calendar.leapdays(y1, y2)
print("Number of leap years between", y1, "and", y2, "is:", leaps)
