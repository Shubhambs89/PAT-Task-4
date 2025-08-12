my_list = [10, 501, 22, 37, 100, 999, 87, 351]

# 1. Finding Even and Odd numbers from my_list
print()
print('Even Numebrs: ')
for num in my_list:
    if num % 2 == 0:
        print(num)
  

print('Odd Numebrs: ')
for num in my_list:
    if num % 2 != 0:
        print(num)
print()

# 2. Finding the prime numbers and count of prime numbers from my_list
prime_numbers = []
for numb in my_list:
    if numb > 1:
        is_prime = True
        for i in range (2, numb):
            if numb % i == 0:
                id_prime = False
                break
    if is_prime:
        prime_numbers.append(numb)

prime_count= len(prime_numbers)

print('Prime numbers in the list:', prime_numbers)
print('count of the prime numbers:', prime_count)
print()

# 3. Finding the Happy numbers from the list given

for n in my_list:

    while n >= 10:
        sum = 0
        while n > 0:
            r = n % 10
            sum = sum + (r * r)
            n = n // 10
        n = sum

    if n == 1:
       print("Happy Number: ",n)
    else:
       print("Unhappy Number: ",n)
print()

# 4. Finding the sum of first and last digit of the interger 
a=my_list[0]
b=my_list[7]
print('The sum of first and last digit:',a+b)
print()

# # 5. ways to make 10 rs using coins of 1 rs, 2 rs, 5 rs and 10 rs
Total = 10
ways = 0

for coins_10 in range (Total // 10+1):
 for coins_5 in range (Total // 5 +1):
  for coins_2 in range (Total //2 +1):
   for coins_1 in range (Total +1 ):
    target = (coins_1 * 1) + (coins_2 * 2)+ (coins_5 * 5)+ (coins_10 *10)

    if Total == target:
     print(f'10x{coins_10}, 5x{coins_5}, 2x{coins_2}, 1x{coins_1}')
     ways += 1
     
print('Total number of ways are:', ways)
print()

# 6. Find the dulicates in three lists

Set1= {1, 2, 3, 4, 5, 6}
Set2= {3, 4, 5, 6, 7, 8}
Set3= {5, 6, 7, 8, 9, 10}

union_set= Set1 | Set2 | Set3
uni_set = sorted (union_set)
print("The duplicate in the three sets are: ", uni_set)

interger_set= Set1 & Set2 & Set3
intersection_set = sorted (interger_set)
print('The first duplicate in three list:',intersection_set[0])
print()

# 7. finding the non repeating number

for num in Set1:
    if num not in Set2 and num not in Set3:
        print("First non repeating number is :", num)
        break
print()    


# # 8. minimum element in rated and sorted list

union_set = Set1|Set2|Set3
ascending = sorted (union_set)

print("Minimum element in all set combined is:", ascending[0])
ascending1 = sorted(Set1)

print("Minimum element in Set1 is :",ascending1[0])

ascending2 = sorted(Set2)
print("Minimum element in Set2 is :",ascending2[0])

ascending3 = sorted(Set3)
print("Minimum element in Set3 is :",ascending3[0])
print()

# 9. Triplet used for the sum to get value of 59
values = [10, 20, 30, 9]
Sum= 59
for i in range (len (values) - 2):
   for j in range(i+1, len(values)-1):
      for k in range(j+1, len(values)):
         if values[i] + values[j]+ values[k] == 59:
            print("Trplets are:", values[i], values [j], values[k])
            break
print()


# 10. Sub list with sum equal to zero

given_list = [4, 2, -3, 1, 6]
found = False

for i in range(len(given_list)):
    current_sum = 0
    for j in range (i, len(given_list)):
        current_sum += given_list[j]
        if current_sum==0:
            print("sublist with sum zero found:", given_list[i:j+1])
            break