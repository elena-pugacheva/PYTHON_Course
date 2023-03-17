print('\n'*10)
while True:
    
    choiсe = int(input('Введите нужное действие: \n 1 - Добавить новый контакт \
                    \n 2 - Показать все контакты \n 3 - Поиск по фамилии \n 4 - Удалить все контакты \n 5 - Выход \n'))
    match choiсe: 
        case 1: 
            import input1
            input1.Input(input('Введите ФИО: '), input('Введите номер: '))
        case 2: 
            from output import OutputAll
            OutputAll()
        case 3:
            from output import Search
            Search(input('Введите фамилию: '))
        case 4: 
            from delete import DeleteAll
            DeleteAll()
        case 5: break