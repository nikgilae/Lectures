from rich import print as rich_print


rich_print("[bold red]Привет мой друг из Москвы!")
rich_print("[bold red]Сегодня будет показ крутого фильм")
desicion = input("Пойдешь со мной ? [Да/Нет]: ")
desicion.lower()
if desicion.lower() == 'yes':
  age= int(input ('How old are you?: '))
  if age >= 18:
    print("Let's go")
  elif age <= 18:
    print("Sorry, you don't go")
    
elif desicion.lower() == 'no':
  print('fjejjwj')
else:
  rich_print('')