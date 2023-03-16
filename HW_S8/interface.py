print('\n'*10)
while True:
    
    choiсe = int(input('Введите нужное действие: \n 1 - Добавить в справочник \
                    \n 2 - Вывести всех \n 3 - Поиск по фамилии \n 4 - Выход \n'))
    match choiсe: 
        case 1: 
            import input1
            input1.Input(input('Введите имя: '), input('Введите номер: '))
        case 2: 
            from output import OutputAll
            OutputAll()
        case 3:
            from output import Search
            Search(input('Введите фамилию: '))
        case 4: break