def max_negative_element(arr):
    negatives = [x for x in arr if x < 0]
    if not negatives:
        return None
    return max(negatives)

numbers = [3, -7, 0, 12, -4, -15, 8]
print("Array:", numbers)
result = max_negative_element(numbers)
if result is None:
    print("No negative elements")
else:
    print("Max negative element:", result)
