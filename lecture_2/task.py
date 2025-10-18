# Запросить у пользователя хочет ли он сняться в кино 
# Если да - предложить две разных роли: Халк или Локи
# Если халк, запросить сколько у него бицепс в объеме
#    Если меньше 60 - отправить домой, если больше - то сказать, что он принят
# Если локи - спросить кого он больше любит маму или папу
#      Если папу - отправить домой, если маму - отправить к папе, чтобы спросить кого он больше любит
# Если нет - попрощаться
# Во всех условиях обрабатывать белебирду и неправильные выборы ошибкой для пользователя 
from rich import print as rich_print
film = input('Хочешь ли ты сняться в кино ??:[yes/no] ')

if film.lower()== 'yes':
  role = input('Есть две роли Халк и Локи, кого выберешь ??: [Hulk/Loki]')
  if role == 'Hulk':
    biceps = int(input('Какой у тебя обхват бицепса ?: '))
    if biceps >= 60:
      rich_print('[bold green] Вы приняты')
    elif biceps <= 60:
      rich_print('[bold red] Идите домой')
    else:
      rich_print(' [bold black] Error')
  elif role == 'Loki':
    love = input('Кого ты больше любишь ?:[dad/mom] ')
    if love.lower() == 'dad':
      rich_print('[bold red] Идите домой')
    elif love.lower() =='mom':
      rich_print('[bold green] Иди к отцу, спроси кого любит он')
    else:
      rich_print ('[bold black] Error')
  else:
    rich_print('[bold black] Error')  
elif film.lower()=='no':
  rich_print('[bold red] Идите домой')
else:
  rich_print('[bold black] Error')
