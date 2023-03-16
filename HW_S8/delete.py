
def DeleteName(line):
    lines = open('file.txt', 'r', encoding='utf-8')
    phonebook=lines.readlines()
    for i in range (len(phonebook)):
        if line in phonebook[i]:
            phonebook[i] = "" 
   
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.writelines(phonebook)
    print('Контакт удален')
    print('\n'*3)

