a = list(range(1,1000))
even_num = list()
odd_num = list()
multiple_of_6 = list()
for n in a:
    if n % 6 == 0:
        multiple_of_6.append(n)
    elif n % 2 == 0:
        even_num.append(n)
    else:
        odd_num.append(n)
print("Even Numbers:", even_num)
print("Odd Numbers:", odd_num)
print("Multiples of 6:", multiple_of_6)