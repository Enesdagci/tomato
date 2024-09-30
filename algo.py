# if condition question

# Q-1
"""
j_angry = False
s_angry = True
if j_angry and s_angry:
	print(True)
else:
	print(False)
"""
# Q-2
"""
x = int(input("Enter the number: "))
if x % 2 == 0:
	print("Even")
else:
	print("Odd")
"""
# Q-3
"""
a = int(input("Enter the number: "))
b = int(input("Enter the second number: "))
if a < 0 and b < 0:
    print(True)
else:
    print(False)
"""
# Q-4
"""
sonuc = 0
n = int(input("N: "))
for i in range(1,11):
    sonuc = n * i
    print(sonuc,end=" ")
"""
# Q-5
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
buyuk = 0
if a >=b and a >=c:
	buyuk = a
elif b >= a and b >= c:
	buyuk = b
elif c >= b and c >= a:
	buyuk = c
print(buyuk)
"""
# Q-6
"""
ciftler = 0
tekler = 0

for i in range(1,101):
	if i % 2 == 0:
		ciftler += i
	else:
		tekler += i
print(tekler , ciftler)
"""
# Q-7
"""
x = int(input("Enter the number: "))
yuzler = x // 100
onlar_bas = x - (yuzler * 100)
onlar = onlar_bas // 10
birler = onlar_bas - (onlar * 10)
print(yuzler ,onlar ,birler)
"""
# Q-8
"""
i = 1
neg = 0
pos = 0
for i in range(1,11):
	x = int(input(f"Enter the {i}. number: "))
	if x < 0:
		neg += 1
	elif x > 0:
		pos += 1
print(pos , neg)
"""
# Q-9
"""
x = int(input("Enter the number: "))
kok = x ** (1/2)
kare = int(kok) ** 2
if x == kare:
	print("Karekök bir sayı")
else:
 	print("karekök bir sayı değil")
"""
# Q-10

tam_sayi = 0
for sayac in range(1,101):
	deger = (2 * sayac) + 1
	if deger % 5 == 0:
		tam_sayi += 1
print(tam_sayi)
