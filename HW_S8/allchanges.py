def AllChanges(line):
    while True:
        change = int(input(' 1 - Изменить контакт \n 2 - Удалить контакт \n 3 - Вернуться в главное Меню \n'))
        match change: 
            case 1: 
                from change1 import ChangeName
                ChangeName(line)
            case 2: 
                from delete import DeleteName
                DeleteName(line)
            case 3: break
            
        


