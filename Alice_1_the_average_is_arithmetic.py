list_num = []
print('Для вычисления среднего значения введите "q"')
print('____________\n')

while True:
    try:
        while True:
            i = input('Введите значение: ')
            if i != 'q':
                list_num.append(int(i))
            else:
                mess = 'Вычисляется среднее занчение...'
                print('\n##############')
                print(mess.strip())
                print('##############\n')
                print(f'Среднее значение = {sum(list_num)/len(list_num)}\n')
                break
    except ValueError:
        print('Неверный формат ввода!!!')
        print('____________\n')
    except ZeroDivisionError:
        print('Значения не были указаны...')
        print('____________\n')
        
    
