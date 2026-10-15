
name = input("Enter your name: ")

mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
