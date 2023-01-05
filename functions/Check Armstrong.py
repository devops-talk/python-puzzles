def Armstrong_Number(Number):
           # Initializing Sum and Number of Digits
           Sum = 0
           Times = 0

           # Calculating Number of individual digits
           Temp = Number
           while Temp > 0:
                      Times = Times + 1
                      Temp = Temp // 10

           # Finding Armstrong Number
           Temp = Number
           for n in range(1, Temp + 1):
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** Times)
                      Temp //= 10
           return Sum
#End of Function

#User Input
Number = int(input())

if (Number == Armstrong_Number(Number)):
    print("true")
else:
    print("false")