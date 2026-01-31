#Task A
temp = 9 
if temp >= 30: 
    print("i'ts a hot day, stay hydrated")
elif temp >= 20 and temp <= 29:
    print("i'ts a warm day, enjoy the whather")  
elif temp >= 10 and temp <= 19:
    print("i'ts a cool day, wear a jacket") 
else:
    print("it's a cold day stay warm!")
#Task b
numbers = list(range(1, 21))
divisible_by_three = []
for num in numbers:
    if num % 3 == 0:
        divisible_by_three.append(num)
print("Numbers from 1 to 20 that are divisible by 3:")
print(divisible_by_three)