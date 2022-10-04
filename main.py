
# ******************************
# Make your Code
# ******************************

numbers = []

while len(numbers) < 5:
    try:
        numbers.append(int(input("Enter a number: ")))
    except ValueError:
        print("Value must be numeric")

average = sum(numbers) / len(numbers)

for i in range(5):
    if numbers[i] > average:
        print(numbers[i], end=' ')

