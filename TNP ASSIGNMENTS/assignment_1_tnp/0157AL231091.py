# NAME : HIMANG SAHU
# ENROLLMENT : 0157AL231091
# BATCH : 5
# BATCH TIME : 10:30 TO 12:10



# Part 1: Basic If-Else Logic



# Q1. Check positive, negative, or zero
print("\n Q1. Check positive, negative, or zero")
entry = int(input("Enter a number to check: "))
if entry > 0:
    print("The number is Positive.")
elif entry < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


# Q2. Check even or odd
print("\n Q2. Check even or odd")
value = int(input("Enter an integer: "))
if value % 2 == 0:
    print(f"{value} is Even.")
else:
    print(f"{value} is Odd.")


# Q3. Check leap year
print("\n Q3. Check leap year")
year_val = int(input("Enter a year: "))
if (year_val % 4 == 0 and year_val % 100 != 0) or (year_val % 400 == 0):
    print(f"{year_val} is a Leap Year.")
else:
    print(f"{year_val} is not a Leap Year.")


# Q4. Greatest of two numbers
print("\n Q4. Greatest of two numbers")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 == num2:
    print("The numbers are equal.")
else:
    print(f"The greater number is {max(num1, num2)}.")


# Q5. Eligible to vote
print("\n Q5. Eligible to vote")
voter_age = int(input("Enter the age: "))
if voter_age >= 18:
    print("This person can vote.")
else:
    print("This person cannot vote.")


# Q6. Vowel or consonant
print("\n Q6. Vowel or consonant")
char_input = input("Enter a single character: ")
if char_input.lower() in 'aeiou':
    print("It's a Vowel.")
else:
    print("It's a Consonant.")


# Q7. Divisible by 5
print("\n Q7. Divisible by 5")
number = int(input("Enter a number: "))
if number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 5.")


# Q8. Single, two, or more digits
print("\n Q8. Single, two, or more digits")
num_entry = int(input("Enter a positive number: "))
if 0 <= num_entry < 10:
    print("It is a 1-digit number.")
elif 10 <= num_entry < 100:
    print("It is a 2-digit number.")
else:
    print("It is a number with more than 2 digits.")


# Q9. Pass or fail
print("\n Q9. Pass or fail")
grade_score = int(input("Enter the marks: "))
if grade_score >= 40:
    print("Student has Passed.")
else:
    print("Student has Failed.")


# Q10. Multiple of 3 and 7
print("\n Q10. Multiple of 3 and 7")
check_val = int(input("Enter a number: "))
if check_val % 3 == 0 and check_val % 7 == 0:
    print("It's a multiple of both 3 and 7.")
else:
    print("It's not a multiple of both 3 and 7.")



# Part 2: Ladder and Nested If Logic



# Q11. Greatest among three
print("\n Q11. Greatest among three")
x1 = int(input("Enter first number: "))
x2 = int(input("Enter second number: "))
x3 = int(input("Enter third number: "))
print(f"The greatest number is {max(x1, x2, x3)}.")


# Q12. Classify person by age
print("\n Q12. Classify person by age")
age_input = int(input("Enter an age: "))
if age_input > 59:
    group = "Senior"
elif age_input > 19:
    group = "Adult"
elif age_input > 12:
    group = "Teenager"
else:
    group = "Child"
print(f"The person is a {group}.")


# Q13. Assign grades
print("\n Q13. Assign grades")
score = int(input("Enter the score (0-100): "))
final_grade = "Fail"
if score >= 90:
    final_grade = "A"
elif score >= 75:
    final_grade = "B"
elif score >= 50:
    final_grade = "C"
elif score >= 35:
    final_grade = "D"
print(f"Grade is {final_grade}.")


# Q14. Type of triangle
print("\n Q14. Type of triangle")
side_a = int(input("Enter length of side A: "))
side_b = int(input("Enter length of side B: "))
side_c = int(input("Enter length of side C: "))
if side_a == side_b == side_c:
    tri_type = "Equilateral"
elif side_a == side_b or side_b == side_c or side_a == side_c:
    tri_type = "Isosceles"
else:
    tri_type = "Scalene"
print(f"The triangle is {tri_type}.")


# Q15. Character type
print("\n Q15. Character type")
char_val = input("Enter a character: ")
if 'a' <= char_val <= 'z':
    print("Lowercase letter.")
elif 'A' <= char_val <= 'Z':
    print("Uppercase letter.")
elif '0' <= char_val <= '9':
    print("A digit.")
else:
    print("A special symbol.")


# Q16. Electricity bill
print("\n Q16. Electricity bill")
units_used = int(input("Enter units used: "))
cost = 0
if units_used > 200:
    cost = (100 * 5) + (100 * 7) + ((units_used - 200) * 10)
elif units_used > 100:
    cost = (100 * 5) + ((units_used - 100) * 7)
else:
    cost = units_used * 5
print(f"Total bill is {cost}")


# Q17. Largest of four (nested if)
print("\n Q17. Largest of four (nested if)")
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
print(f"The largest is {max(n1, n2, n3, n4)}.")


# Q18. Century leap year
print("\n Q18. Century leap year")
year_to_check = int(input("Enter a year: "))
if year_to_check % 100 == 0:
    # It's a century year
    if year_to_check % 400 == 0:
        print("It is a century leap year.")
    else:
        print("It is a century year, but not a leap year.")
else:
    print("It is not a century year.")


# Q19. Classify BMI
print("\n Q19. Classify BMI")
bmi_val = float(input("Enter the BMI value: "))
category = ""
if bmi_val < 18.5:
    category = "Underweight"
elif 18.5 <= bmi_val < 25:
    category = "Normal"
elif 25 <= bmi_val < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"The classification is {category}.")


# Q20. Smallest of three (nested if)
print("\n Q20. Smallest of three (nested if)")
v1 = int(input("Enter number 1: "))
v2 = int(input("Enter number 2: "))
v3 = int(input("Enter number 3: "))
print(f"The smallest is {min(v1, v2, v3)}.")



# Part 3: For Loop Problems



# Q21. Armstrong numbers 100-999
print("\n Q21. Armstrong numbers 100-999")
print("Armstrong numbers found:")
for num in range(100, 1000):
    sum_of_cubes = 0
    for digit in str(num):
        sum_of_cubes += int(digit) ** 3
    if num == sum_of_cubes:
        print(num)


# Q22. First n prime numbers
print("\n Q22. First n prime numbers")
n = int(input("How many primes to find?: "))
primes_list = []
candidate = 2
while len(primes_list) < n:
    is_prime = True
    for i in range(2, int(candidate**0.5) + 1):
        if candidate % i == 0:
            is_prime = False
            break
    if is_prime:
        primes_list.append(candidate)
    candidate += 1
print(f"The first {n} primes are {primes_list}")


# Q23. Divisible by 3, digit sum <= 10 (1-500)
print("\n Q23. Divisible by 3, digit sum <= 10 (1-500)")
print("Numbers matching criteria:")
for i in range(1, 501):
    if i % 3 == 0:
        if sum(int(d) for d in str(i)) <= 10:
            print(i)


# Q24. Pyramid of stars
print("\n Q24. Pyramid of stars")
height = int(input("Enter pyramid height: "))
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


# Q25. Pangram check
print("\n Q25. Pangram check")
sentence = input("Enter a sentence: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True
for letter in alphabet:
    if letter not in sentence.lower():
        is_pangram = False
        break
if is_pangram:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")


# Q26. Twin primes 1-100
print("\n Q26. Twin primes 1-100")
primes = []
print("Twin primes found:")
for i in range(2, 101):
    is_p = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_p = False
            break
    if is_p:
        primes.append(i)
for k in range(len(primes) - 1):
    if primes[k+1] - primes[k] == 2:
        print(f"({primes[k]}, {primes[k+1]})")


# Q27. Harshad number
print("\n Q27. Harshad number")
num_str = input("Enter a number: ")
the_num = int(num_str)
digit_sum = sum(int(d) for d in num_str)
if the_num > 0 and the_num % digit_sum == 0:
    print("It is a Harshad number.")
else:
    print("It is not a Harshad number.")


# Q28. Pascal's Triangle
print("\n Q28. Pascal's Triangle")
rows = int(input("Enter number of rows: "))
level = [1]
for i in range(rows):
    print(" ".join(str(x) for x in level))
    new_level = [1]
    for j in range(len(level) - 1):
        new_level.append(level[j] + level[j+1])
    new_level.append(1)
    level = new_level


# Q29. Sum of squares
print("\n Q29. Sum of squares")
limit = int(input("Enter the limit n: "))
total = sum(i**2 for i in range(1, limit + 1))
print(f"The sum is {total}")


# Q30. Strong number
print("\n Q30. Strong number")
num_str = input("Enter a number: ")
total_fact = 0
for digit in num_str:
    fact = 1
    for i in range(1, int(digit) + 1):
        fact *= i
    total_fact += fact
if total_fact == int(num_str):
    print("It is a Strong number.")
else:
    print("It is not a Strong number.")




# Part 4: While Loop Problems



# Q31. Reverse number and check if prime
print("\n Q31. Reverse number and check if prime")
num_str = input("Enter a number: ")
rev_num = int(num_str[::-1])
is_prime_flag = True
if rev_num < 2:
    is_prime_flag = False
else:
    i = 2
    while i <= rev_num // 2:
        if rev_num % i == 0:
            is_prime_flag = False
            break
        i += 1
if is_prime_flag:
    print(f"The reverse ({rev_num}) is a prime number.")
else:
    print(f"The reverse ({rev_num}) is not a prime number.")


# Q32. Accept numbers until digit sum > 100
print("\n Q32. Accept numbers until digit sum > 100")
grand_total = 0
while grand_total <= 100:
    print(f"Current digit sum total: {grand_total}")
    entry = input("Enter a number: ")
    grand_total += sum(int(d) for d in entry)
print(f"Total {grand_total} has surpassed 100.")


# Q33. Duck number
print("\n Q33. Duck number")
num_entry_str = input("Enter a number: ")
if num_entry_str[0] != '0' and '0' in num_entry_str:
    print("It is a Duck number.")
else:
    print("It is not a Duck number.")


# Q34. Happy number
print("\n Q34. Happy number")
num = int(input("Enter a number: "))
path = set()
is_happy = False
while True:
    if num == 1:
        is_happy = True
        break
    if num in path:
        is_happy = False
        break
    path.add(num)
    num = sum(int(d)**2 for d in str(num))
if is_happy:
    print("It is a Happy number.")
else:
    print("It is not a Happy number.")


# Q35. Largest prime factor
print("\n Q35. Largest prime factor")
val = int(input("Enter a number: "))
factor = 2
largest = -1
while val > 1:
    if val % factor == 0:
        largest = factor
        val = val / factor
    else:
        factor += 1
print(f"The largest prime factor is {largest}")


# Q36. Accept string until palindrome
print("\n Q36. Accept string until palindrome")
while True:
    text = input("Enter some text: ")
    if text == text[::-1]:
        print("Palindrome found. Stopping.")
        break
    else:
        print("Not a palindrome. Please try again.")


# Q37. Digital root
print("\n Q37. Digital root")
num = int(input("Enter a number: "))
while num > 9:
    num = sum(int(d) for d in str(num))
print(f"The digital root is {num}.")


# Q38. Collatz sequence
print("\n Q38. Collatz sequence")
n_val = int(input("Enter a starting number: "))
print("Sequence is:")
while n_val != 1:
    print(n_val, end=", ")
    if n_val % 2 == 0:
        n_val = n_val // 2
    else:
        n_val = 3 * n_val + 1
print(1)


# Q39. Kaprekar number
print("\n Q39. Kaprekar number")
kap_num = int(input("Enter a number: "))
sq_val = kap_num * kap_num
sq_str = str(sq_val)
is_kap = False
for i in range(1, len(sq_str)):
    part_a = int(sq_str[:i])
    part_b = int(sq_str[i:])
    if part_a > 0 and part_b > 0 and part_a + part_b == kap_num:
        is_kap = True
        break
if is_kap:
    print("It is a Kaprekar number.")
else:
    print("It is not a Kaprekar number.")


# Q40. ATM machine
print("\n Q40. Simulate an ATM machine")
account_balance = 1000
while True:
    print("\n[ATM] 1=Balance, 2=Deposit, 3=Withdraw, 4=Exit")
    option = input("Select an option: ")
    if option == '1':
        print(f"Current balance is: {account_balance}")
    elif option == '2':
        dep_amount = int(input("Enter amount to deposit: "))
        account_balance += dep_amount
    elif option == '3':
        with_amount = int(input("Enter amount to withdraw: "))
        if with_amount > account_balance:
            print("Error: Insufficient funds.")
        else:
            account_balance -= with_amount
    elif option == '4':
        print("Exiting ATM. Thank you.")
        break
    else:
        print("Invalid selection.")
