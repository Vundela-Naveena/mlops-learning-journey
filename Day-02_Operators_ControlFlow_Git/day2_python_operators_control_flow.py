# =====================================
# DAY 2: PYTHON OPERATORS & CONTROL FLOW
# =====================================

print("=== DAY 2 PYTHON PRACTICE ===")

# -------------------------------
# 1. ARITHMETIC OPERATORS
# -------------------------------
a = 10
b = 3

print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

# -------------------------------
# 2. COMPARISON OPERATORS
# -------------------------------
x = 5
y = 8

print("\nComparison Operators")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# -------------------------------
# 3. LOGICAL OPERATORS
# -------------------------------
age = 25

print("\nLogical Operators")
print(age > 18 and age < 30)
print(age > 18 or age > 60)
print(not age > 30)

# -------------------------------
# 4. ASSIGNMENT OPERATORS
# -------------------------------
num = 10
num += 5
num -= 2
num *= 3

print("\nAssignment Operators")
print("Final value:", num)

# -------------------------------
# 5. MEMBERSHIP OPERATORS
# -------------------------------
text = "MLOps"

print("\nMembership Operators")
print("M" in text)
print("z" not in text)

# -------------------------------
# 6. IF / ELIF / ELSE
# -------------------------------
marks = 75

print("\nIf Elif Else Example")
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# -------------------------------
# 7. NESTED IF
# -------------------------------
age = 22
has_id = True

print("\nNested If Example")
if age >= 18:
    if has_id:
        print("Allowed to vote")
    else:
        print("ID required")
else:
    print("Not eligible")

# -------------------------------
# 8. FOR LOOP
# -------------------------------
print("\nFor Loop Example")
for i in range(1, 6):
    print(i)

# -------------------------------
# 9. WHILE LOOP
# -------------------------------
print("\nWhile Loop Example")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# -------------------------------
# 10. BREAK & CONTINUE
# -------------------------------
print("\nBreak Example")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue Example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# -------------------------------
# 11. EVEN / ODD CHECK
# -------------------------------
number = 7
print("\nEven or Odd Check")
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# -------------------------------
# 12. SUM OF NUMBERS
# -------------------------------
total = 0
for i in range(1, 6):
    total += i
print("\nSum of 1 to 5:", total)

# -------------------------------
# 13. MULTIPLICATION TABLE
# -------------------------------
num = 5
print("\nMultiplication Table")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# -------------------------------
# 14. COUNT DIGITS
# -------------------------------
number = 12345
count = 0

temp = number
while temp > 0:
    temp //= 10
    count += 1

print("\nTotal digits:", count)

# -------------------------------
# 15. REVERSE NUMBER
# -------------------------------
num = 1234
reverse = 0

temp = num
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("\nReversed number:", reverse)

# -------------------------------
# 16. SIMPLE LOGIN CHECK
# -------------------------------
username = "admin"
password = "admin123"

print("\nLogin Check")
if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Login Failed")

# -------------------------------
print("\n=== DAY 2 COMPLETED SUCCESSFULLY ✅ ===")