#1
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area:.1f}")

#2
Temp_C = float(input("Enter temperature in Celsius: "))
Temp_F = (Temp_C * 9/5) + 32
print(f"Temperature in Fahrenheit: {Temp_F:.2f}°F")

#3
num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a prime number")
elif num >= 2:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")

#4
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n):
    if n % i == 0:
        total_sum += i
if total_sum == n and n > 0:
     print(f"{n} is a perfect number")
else:
     print(f"{n} is not a perfect number")

#5
color = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Blue", "Orange", "Purple", "Brown"]
fav_color = input("What is your favorite color? ")
lower_color = [c.lower() for c in color]
fav_color_lower = fav_color.lower()
if fav_color_lower in lower_color:
    index = lower_color.index(fav_color_lower)
    print(f"Your favorite color is at index {index} in the list.")
else:
    print(f"Sorry, I cannot find your color")

6
range1 = list(range(0, 7, 1))
print(range1)
range2 = list(range(1, 11, 3))
print(range2)
range3 = list(range(5, 0, -1))
print(range3)
range4 = list(range(6, -3, -2))
print(range4)

7
s = '100000$'
S_new = s.replace('$','')
print(S_new)

#8
l = [1, 4, 5, -1, 10]
even_list = []

for x in l:
    if x % 2 == 0:
        even_list.append(x)


#9
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(factorial) 

#10
n = int(input("Enter a number: "))
divisors = []

for i in range(1, abs(n) + 1):
    if n % i == 0:
        divisors.append(i)

print(divisors) 

#11
import math
p1 = (1, 2)
p2 = (4, 6)

distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print(distance)

#12
n = 5
m = 3

for _ in range(m):
    print("* " * n)
