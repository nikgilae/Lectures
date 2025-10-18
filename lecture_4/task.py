import math
stroka = int(input("Введите число строк, до которой будет идти треугольник: "))
otstup = " " * (stroka -1)
print(otstup, end=" ")
row = [1]
for number in row:
  print(number, end=" ")
print()

for i in range(stroka-1):
  
 print(otstup, end="")
 next_row = [1]
 for number in next_row:
   print(number, end=" ")
 print()
 for j in range(len(row)-1):
  number_1 = row[j]
  number_2 = row[j+1]
  sum1 = number_1 + number_2
  next_row.append(sum1)
 отступ = " " * (stroka - i - 2)

 row = next_row
  
  