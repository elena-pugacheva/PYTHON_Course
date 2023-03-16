def OutputAll():

    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
        print('\n'*3)
       


def Search(data):
    data = data.lower()
    with open('file.txt', 'r', encoding='utf-8') as file:
        flag = False
        for line in file:
            if data in line.lower():
                print(line)
                flag = True
                from allchanges import AllChanges
                AllChanges(line)
        print('\n'*3)
        if flag == False:
            print('\n не найдено \n')
            print('\n'*3)