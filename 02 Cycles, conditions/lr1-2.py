print(Симонов Сергей М8о-107М-22)

drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list

d = {}

for drone in drone_list:
  drone = drone.split(' ')
  drone[0] = drone[0].capitalize()
  if drone[0] == 'Dji':
    drone[0] = 'DJI'
  print(drone)
  tmp = ''
  for i in range(1, len(drone)):
    tmp += drone[i] + ' '
  if drone[0] not in d:
    d[drone[0]] = []
  d[drone[0]].append(tmp)

print(d)
  
#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel

print('TODO1')
print()

inp = input().capitalize()
if inp == 'Dji':
  print("Дроны компании DJI:\n")
  for i in d['DJI']:
    print(i)
else:
  print(f"Дроны компании {inp}:\n")
  for i in d[inp]:
    print(i)

print()
    
#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

print('TODO2')
print()

for dr in d:
  print(f'{dr}: {len(d[dr])}')

print()
  
    
#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

print('TODO3')
print()

print('Дроны которые нужно регистрировать:')
for drone, weight in zip(drone_list,  drone_weight_list):
  if weight > 150:
    print(drone, weight)

print()

print('Дроны которые не нужно регистрировать:')
for drone, weight in zip(drone_list,  drone_weight_list):
  if weight <= 150:
    print(drone, weight)
    
print()

#TODO4
#для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

print('TODO4')
print()

height = 100

closed_area = False
vlos = True


for drone, weight in zip(drone_list,  drone_weight_list):
  if height<= 150 and weight <= 150 and vlos and not closed_area:
    print(f'{drone} -- согласование для полета не требуется')
  else:
    print(f'{drone} -- нужно согласовать полет')

print()
#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine


print('TODO5')
print()

inp = input().capitalize()
tmp  = ''
if inp == 'Dji':
  print("Дроны компании DJI:\n")
  for i in d['DJI']:
    tmp += i[:len(i) - 1] + ', ' 
else:
  print(f"Дроны компании {inp}:\n")
  for i in d[inp]:
    # print(i)
    tmp += i[:len(i) - 1] + ', '

print(tmp[:len(tmp) - 2])
    
print()