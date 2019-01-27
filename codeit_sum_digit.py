def sum_digit(num):
    str_num = str(num)
    sum = 0

    for digit in str_num:
        sum = sum + int(digit)
    return sum

total = 0
for i in range(1, 1001):
    total = total + sum_digit(i)
print(total)
