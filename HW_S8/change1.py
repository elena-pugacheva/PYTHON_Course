# def ChangeName(data, number):
#     data = data.lower()
#     with open('file.txt', 'w', encoding='utf-8') as file:
#         file.write(f'{data} : {number} \n')
#     print('Данные изменены')
#     print('\n'*3)

def ChangeName(line):
    lines = open('file.txt', 'r', encoding='utf-8')
    phonebook=lines.readlines()
    for i in range (len(phonebook)):
        if line in phonebook[i]:
            phonebook[i] = (input('Введите новые ФИО: ')," : ", input('Введите новый номер: '),'\n')
            phonebook[i] = ''.join(phonebook[i])
            print(phonebook[i])
    
   
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.writelines(phonebook)
    print('Контакт изменен')
    print('\n'*3)