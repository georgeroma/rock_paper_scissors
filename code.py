import random
user_score = 0
computer_score = 0

def get_figure():
    number = random.randint(1,3)
    if number == 1:
        return [1,'Камень']
    elif number == 2:
        return [2,'Ножницы']
    else :
        return [3,'Бумагу']

def user_format_figure(number):
    if number == 1:
        return [1,'Камень']
    elif number == 2:
        return [2,'Ножницы']
    else :
        return [3,'Бумагу']

def who_win():
    a=user_figure[0]
    b=computer_figure[0]

    if a==1 and b==2:
        return 'user'
    elif a==3 and b==1:
        return 'user'
    elif a==2 and b==3:
        return 'user'

    elif a==2 and b==1:
        return 'computer'
    elif a==1 and b==3:
        return 'computer'
    elif a==3 and b==2:
        return 'computer'

    '''else :
        return 'draw'''


while True:
    print("-------------------------------------------------------------------------------------------------------")
    user_figure = int(input('Что вы хотите выкинуть на этот раз? \n | Камень - 1 | Ножницы - 2 | Бумага - 3 | \n'))
    user_figure = user_format_figure(user_figure)

    computer_figure = get_figure()
    #print(computer_figure)



    print ('Ты выбросил:', user_figure[1], '\n' 'Компьютер выбросил:', computer_figure[1])

    winner= who_win ()

    if winner == 'user':
        print ('Выиграл Ты')
        user_score+=1
    elif winner == 'computer':
        print ('Выиграл Компьютер')
        computer_score+=1
    else:
        print('Ничья')

    print('Таблица очков:\n Ты -',user_score,'\n Компьютер -', computer_score)
