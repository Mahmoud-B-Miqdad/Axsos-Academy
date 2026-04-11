# 1. Basic - Print all integers from 0 to 150
print("--- Task 1: Basic ---")
for i in range(151):
    print(i)

# 2. Multiples of Five - Print all multiples of 5 from 5 to 1,000
print("\n--- Task 2: Multiples of Five ---")
for i in range(5, 1001, 5):
    print(i)

# 3. Counting, the Dojo Way - Divisible by 5 (Coding), by 10 (Coding Dojo)
print("\n--- Task 3: Counting, the Dojo Way ---")
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge - Sum of odd integers from 0 to 500,000
print("\n--- Task 4: Whoa. That Sucker's Huge ---")
final_sum = 0
for i in range(1, 500001, 2):
    final_sum += i
print(f"Final Sum: {final_sum}")

# 5. Countdown by Fours - Positive numbers starting at 2018, counting down by fours
print("\n--- Task 5: Countdown by Fours ---")
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter
print("\n--- Task 6: Flexible Counter ---")
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)