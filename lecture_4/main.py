"""
ПОЛНЫЙ СПРАВОЧНИК ПО МЕТОДАМ СПИСКОВ PYTHON
=========================================

Этот файл содержит подробные примеры всех методов списков Python
с различными вариантами использования каждого метода.
"""

# Исходные данные для примеров
numbers = [1, 2, 3, 4, 5, 2, 3, 6, 2]
fruits = ['яблоко', 'банан', 'вишня', 'яблоко', 'банан']
mixed = [1, 'hello', 3.14, True, [1, 2, 3]]

print("=== МЕТОДЫ ИЗМЕНЕНИЯ СПИСКОВ ===")

# 1. append(item) - добавляет элемент в конец списка
print("\n1. append(item) - добавляет элемент в конец списка:")
fruits_copy = fruits.copy()
print(f"Исходный список: {fruits_copy}")
fruits_copy.append('апельсин')
print(f"После append('апельсин'): {fruits_copy}")

# Можно добавлять любые типы данных
mixed_copy = mixed.copy()
mixed_copy.append({'key': 'value'})
print(f"Добавление словаря: {mixed_copy}")

# 2. extend(iterable) - расширяет список элементами из итерируемого объекта
print("\n2. extend(iterable) - расширяет список:")
numbers_copy = numbers.copy()
print(f"Исходный список: {numbers_copy}")
numbers_copy.extend([7, 8, 9])
print(f"После extend([7, 8, 9]): {numbers_copy}")

# Расширение строкой (добавит каждый символ)
fruits_copy2 = fruits.copy()
fruits_copy2.extend('киви')
print(f"Расширение строкой 'киви': {fruits_copy2}")

# Расширение другим списком
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"list1.extend(list2): {list1}")

# 3. insert(index, item) - вставляет элемент по указанному индексу
print("\n3. insert(index, item) - вставляет элемент по индексу:")
fruits_copy3 = fruits.copy()
print(f"Исходный список: {fruits_copy3}")
fruits_copy3.insert(1, 'манго')
print(f"После insert(1, 'манго'): {fruits_copy3}")

# Вставка в начало (index = 0)
fruits_copy3.insert(0, 'ананас')
print(f"Вставка в начало: {fruits_copy3}")

# Вставка в конец (index = len(list))
fruits_copy3.insert(len(fruits_copy3), 'груша')
print(f"Вставка в конец: {fruits_copy3}")

# Вставка с отрицательным индексом
fruits_copy3.insert(-1, 'персик')
print(f"Вставка с отрицательным индексом: {fruits_copy3}")

# 4. remove(item) - удаляет ПЕРВОЕ вхождение указанного элемента
print("\n4. remove(item) - удаляет первое вхождение:")
numbers_copy2 = numbers.copy()
print(f"Исходный список: {numbers_copy2}")
numbers_copy2.remove(2)
print(f"После remove(2): {numbers_copy2}")

# Попытка удалить несуществующий элемент вызовет ValueError
try:
    numbers_copy2.remove(10)
except ValueError as e:
    print(f"Ошибка при remove(10): {e}")

# 5. pop(index=-1) - удаляет и возвращает элемент по индексу
print("\n5. pop(index) - удаляет и возвращает элемент:")
numbers_copy3 = numbers.copy()
print(f"Исходный список: {numbers_copy3}")

# Удаление последнего элемента (по умолчанию)
last_item = numbers_copy3.pop()
print(f"pop() - последний элемент: {last_item}, список: {numbers_copy3}")

# Удаление по индексу
first_item = numbers_copy3.pop(0)
print(f"pop(0) - первый элемент: {first_item}, список: {numbers_copy3}")

# Удаление по отрицательному индексу
middle_item = numbers_copy3.pop(-2)
print(f"pop(-2) - предпоследний элемент: {middle_item}, список: {numbers_copy3}")

# 6. clear() - удаляет все элементы из списка
print("\n6. clear() - очищает список:")
temp_list = [1, 2, 3, 4, 5]
print(f"До clear(): {temp_list}")
temp_list.clear()
print(f"После clear(): {temp_list}")

print("\n=== МЕТОДЫ ПОИСКА И ИНФОРМАЦИИ ===")

# 7. index(item, start, end) - возвращает индекс первого вхождения элемента
print("\n7. index(item, start, end) - поиск индекса:")
fruits_copy4 = fruits.copy()
print(f"Исходный список: {fruits_copy4}")

# Поиск без параметров
index_apple = fruits_copy4.index('яблоко')
print(f"index('яблоко'): {index_apple}")

# Поиск с начальным индексом
index_banana = fruits_copy4.index('банан', 2)
print(f"index('банан', 2): {index_banana}")

# Поиск в диапазоне
index_apple_range = fruits_copy4.index('яблоко', 1, 4)
print(f"index('яблоко', 1, 4): {index_apple_range}")

# Попытка найти несуществующий элемент вызовет ValueError
try:
    fruits_copy4.index('груша')
except ValueError as e:
    print(f"Ошибка при index('груша'): {e}")

# 8. count(item) - возвращает количество вхождений элемента
print("\n8. count(item) - подсчет вхождений:")
numbers_copy4 = numbers.copy()
print(f"Исходный список: {numbers_copy4}")
count_2 = numbers_copy4.count(2)
print(f"count(2): {count_2}")

count_10 = numbers_copy4.count(10)
print(f"count(10): {count_10}")

print("\n=== МЕТОДЫ СОРТИРОВКИ И РЕОРГАНИЗАЦИИ ===")

# 9. sort(key=None, reverse=False) - сортирует список на месте
print("\n9. sort(key, reverse) - сортировка:")
numbers_copy5 = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Исходный список: {numbers_copy5}")

# Сортировка по возрастанию
numbers_copy5.sort()
print(f"После sort(): {numbers_copy5}")

# Сортировка по убыванию
numbers_copy5.sort(reverse=True)
print(f"После sort(reverse=True): {numbers_copy5}")

# Сортировка строк
fruits_copy5 = ['банан', 'яблоко', 'вишня', 'ананас']
print(f"Строки до сортировки: {fruits_copy5}")
fruits_copy5.sort()
print(f"Строки после sort(): {fruits_copy5}")

# Сортировка с ключом (по длине строки)
fruits_copy5.sort(key=len)
print(f"Сортировка по длине: {fruits_copy5}")

# Сортировка с ключом (по длине, обратная)
fruits_copy5.sort(key=len, reverse=True)
print(f"Сортировка по длине (обратная): {fruits_copy5}")

# 10. reverse() - разворачивает список на месте
print("\n10. reverse() - разворот списка:")
numbers_copy6 = [1, 2, 3, 4, 5]
print(f"До reverse(): {numbers_copy6}")
numbers_copy6.reverse()
print(f"После reverse(): {numbers_copy6}")

# 11. copy() - создает поверхностную копию списка
print("\n11. copy() - копирование списка:")
original = [1, 2, [3, 4]]
shallow_copy = original.copy()
print(f"Оригинал: {original}")
print(f"Копия: {shallow_copy}")
print(f"Одинаковые объекты: {original is shallow_copy}")
print(f"Равные значения: {original == shallow_copy}")

# Демонстрация поверхностного копирования
original[2].append(5)
print(f"После изменения вложенного списка:")
print(f"Оригинал: {original}")
print(f"Копия: {shallow_copy}")

print("\n=== ВСТРОЕННЫЕ ФУНКЦИИ ДЛЯ РАБОТЫ СО СПИСКАМИ ===")

# len(obj) - длина списка
print("\nlen(obj) - длина списка:")
print(f"len(numbers): {len(numbers)}")
print(f"len(fruits): {len(fruits)}")
print(f"len(mixed): {len(mixed)}")

# max(iterable, key=None) - максимальный элемент
print("\nmax(iterable, key) - максимум:")
print(f"max(numbers): {max(numbers)}")
print(f"max(fruits): {max(fruits)}")
print(f"max(fruits, key=len): {max(fruits, key=len)}")

# min(iterable, key=None) - минимальный элемент
print("\nmin(iterable, key) - минимум:")
print(f"min(numbers): {min(numbers)}")
print(f"min(fruits): {min(fruits)}")
print(f"min(fruits, key=len): {min(fruits, key=len)}")

# sum(iterable, start=0) - сумма элементов
print("\nsum(iterable, start) - сумма:")
print(f"sum(numbers): {sum(numbers)}")
print(f"sum(numbers, 10): {sum(numbers, 10)}")

print("\n=== ОПЕРАТОРЫ И ОПЕРАЦИИ СО СПИСКАМИ ===")

# Оператор принадлежности 'in'
print("\nОператор 'in' - принадлежность:")
print(f"2 in numbers: {2 in numbers}")
print(f"'яблоко' in fruits: {'яблоко' in fruits}")
print(f"10 in numbers: {10 in numbers}")
print(f"'груша' not in fruits: {'груша' not in fruits}")

# Конкатенация списков с помощью '+'
print("\nКонкатенация '+' :")
list_a = [1, 2, 3]
list_b = [4, 5, 6]
concatenated = list_a + list_b
print(f"[1, 2, 3] + [4, 5, 6] = {concatenated}")

# Повторение списка с помощью '*'
print("\nПовторение '*' :")
repeated = [1, 2, 3] * 3
print(f"[1, 2, 3] * 3 = {repeated}")
repeated_zero = [1, 2, 3] * 0
print(f"[1, 2, 3] * 0 = {repeated_zero}")

# Индексация []
print("\nИндексация []:")
numbers_list = [10, 20, 30, 40, 50]
print(f"numbers_list[0]: {numbers_list[0]}")
print(f"numbers_list[-1]: {numbers_list[-1]}")
print(f"numbers_list[2]: {numbers_list[2]}")

# Срезы [start:end:step]
print("\nСрезы [start:end:step]:")
print(f"numbers_list[:3]: {numbers_list[:3]}")
print(f"numbers_list[2:]: {numbers_list[2:]}")
print(f"numbers_list[::2]: {numbers_list[::2]}")
print(f"numbers_list[::-1]: {numbers_list[::-1]}")
print(f"numbers_list[1:4]: {numbers_list[1:4]}")

# Изменение элементов через индексацию
print("\nИзменение через индексацию:")
numbers_list[0] = 100
print(f"После numbers_list[0] = 100: {numbers_list}")

# Изменение через срезы
numbers_list[1:3] = [200, 300]
print(f"После numbers_list[1:3] = [200, 300]: {numbers_list}")

print("\n=== СПЕЦИАЛЬНЫЕ СЛУЧАИ ИСПОЛЬЗОВАНИЯ ===")

# Списковые включения (list comprehensions)
print("\nСписковые включения:")
squares = [x**2 for x in range(5)]
print(f"[x**2 for x in range(5)]: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"[x**2 for x in range(10) if x % 2 == 0]: {even_squares}")

# Фильтрация с условием
filtered = [x for x in numbers if x > 3]
print(f"[x for x in numbers if x > 3]: {filtered}")

# Преобразование типов
string_list = ['1', '2', '3', '4']
int_list = [int(x) for x in string_list]
print(f"[int(x) for x in ['1', '2', '3', '4']]: {int_list}")

# Вложенные списковые включения
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"[[i*j for j in range(3)] for i in range(3)]: {matrix}")

# Работа с несколькими списками одновременно
names = ['Анна', 'Борис', 'Виктор']
ages = [25, 30, 35]
combined = [f"{name} ({age} лет)" for name, age in zip(names, ages)]
print(f"[f\"{{name}} ({{age}} лет)\" for name, age in zip(names, ages)]: {combined}")

print("\n=== МНОГОМЕРНЫЕ СПИСКИ ===")

# Работа с вложенными списками
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nМногомерные списки:")
print(f"nested_list: {nested_list}")
print(f"nested_list[0]: {nested_list[0]}")
print(f"nested_list[1][2]: {nested_list[1][2]}")

# Изменение вложенных списков
nested_list[0].append(10)
print(f"После nested_list[0].append(10): {nested_list}")

# Списковые включения для многомерных списков
flattened = [item for sublist in nested_list for item in sublist]
print(f"flattened: {flattened}")

print("\n=== ПРОИЗВОДИТЕЛЬНОСТЬ И ПАМЯТЬ ===")

# Эффективные операции со списками
print("\nПроизводительность:")

# Предварительное выделение памяти
large_list = [0] * 1000000  # Быстрее, чем append в цикле
print(f"Создан список из 1,000,000 нулей")

# Избегайте частых append в цикле для больших списков
efficient_list = []
for i in range(10000):
    efficient_list.append(i)
print(f"Создан список из 10,000 элементов через цикл")

print("\n=== ЗАМЕЧАНИЯ ПО ИСПОЛЬЗОВАНИЮ ===")
print("1. Методы, изменяющие список на месте (in-place): append, extend, insert, remove, pop, clear, sort, reverse")
print("2. Методы, возвращающие новое значение: index, count, pop")
print("3. Методы, возвращающие новый список: copy")
print("4. Все операции изменения списка возвращают None")
print("5. Списки изменяемы, поэтому будьте осторожны с копированием")
print("6. Для больших списков используйте эффективные операции")

# Демонстрация возвращаемых значений
print("\nДемонстрация возвращаемых значений:")
my_list = [1, 2, 3]
result = my_list.append(4)
print(f"my_list.append(4) возвращает: {result}")

result2 = my_list.pop()
print(f"my_list.pop() возвращает: {result2}, список: {my_list}")

# Финальный пример - комплексное использование
print("\n=== КОМПЛЕКСНЫЙ ПРИМЕР ===")
shopping_list = []
print("Создаем список покупок:")

# Добавляем элементы
shopping_list.append('молоко')
shopping_list.append('хлеб')
shopping_list.extend(['яйца', 'масло'])
shopping_list.insert(1, 'сыр')

print(f"Список покупок: {shopping_list}")

# Ищем и удаляем
if 'хлеб' in shopping_list:
    shopping_list.remove('хлеб')
    print("Убрали хлеб из списка")

# Сортируем
shopping_list.sort()
print(f"Отсортированный список: {shopping_list}")

# Подсчитываем количество элементов
print(f"Всего элементов: {len(shopping_list)}")
print(f"Количество продуктов: {shopping_list.count('яйца')}")

print("\n=== КОНЕЦ СПРАВОЧНИКА ===")