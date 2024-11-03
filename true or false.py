import random
list_of_question = ["Вопрос 1"]
list_of_action = ["Действие 1"]
gamer_list = []
def gamers(list):
    while True:
        name = input("Введите имя - ")
        list.append(str.capitalize(name))
        if len(list)>=2:
            need_next_player = input("Добавить еще игроков?")
            if need_next_player == str.lower("да")\
                or need_next_player == str.lower("yes"):
                continue
            else:
                break
gamers(gamer_list)
print(gamer_list)
def game(list_of_question, list_of_action, *args):
    while True:
        next_step = None
        for gamer in args:
            print(gamer)
            user_choise = input("Правда или действие?")
            if user_choise == str.lower("n") \
                or user_choise == str.lower("правда"):
                question_index = random.randit(0,len(list_of_question)-1)
                print(list_of_question[question_index])
                list_of_question.pop(question_index)
            elif user_choise == str.lower("д") \
                or user_choise == str.lower("действие"):
                action_index = random.randit(0, len(list_of_action)-1)
                print(list_of_action[action_index])
                list_of_action.pop(action_index)
            else:
