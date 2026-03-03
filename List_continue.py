import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here

for i in range(len(random_numbers)):
    number = random_numbers[i]
    if number > 80:
        random_numbers[i] = -number # if the number is greater than 80, replace it with its negative value
    elif random_numbers[i] < 40:
        digit_sum = 0
        for digit in str(random_numbers[i]):
            digit_sum += int(digit)
        random_numbers[i] = digit_sum # if the number is smaller than 40, decompose it into single digits and sum them

print(random_numbers)