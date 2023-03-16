def ChangeName(data, number):
    data = data.lower()
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(f'{data} : {number} \n')
    print('Данные изменены')
    print('\n'*3)