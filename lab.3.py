# while example: sum 1..10
i, s = 1, 0
while i <= 10:
    s += i
    i += 1
print("Sum 1..10 =", s)

# for example: squares of numbers
nums = [1, 2, 3, 4]
squares = [x * x for x in nums]
print("Squares:", squares)
