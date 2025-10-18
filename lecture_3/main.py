low = -1000
high = 1000


while True:
    mid = (low + high) // 2
    region =input(f"Скажите, ваше число <, > или == {mid} (или exit): ")
    if region== 'exit':
        print('EXIT')
        break
    elif region == '==':
        print('Win')
        break
    elif region == '<':
        high = mid - 1
    elif region == '>':
        low = mid + 1
    else:
        print('error')
