import time
n = int(input("Vvedite chislo: "))
cache1 = {}
def fibonachi(n): 
  if n in cache1:
    return cache1[n]
  if n== 0:
    return 0

  elif n == 1:
    return 1
  else:
    result = fibonachi(n - 1) + fibonachi(n - 2)
    cache1[n] = result
    return result

print(fibonachi(n))
