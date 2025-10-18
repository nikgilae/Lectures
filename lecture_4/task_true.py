
stroka = int(input("Введите число строк, до которой будет идти треугольник: "))
row = [1]
print(row)


for i in range(stroka - 1):
    
    next_row = [1]
    for j in range(len(row) - 1):
        number_1 = row[j]
        number_2 = row[j + 1]
        sum1 = number_1 + number_2
        next_row.append(sum1)
    next_row.append(1) 
    print(next_row)

   
    row = next_row