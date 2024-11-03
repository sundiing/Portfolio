import random
import tkinter as tk

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы победили!"
    else:
        return "Компьютер победил!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()

    result_label.config(text=f"Вы выбрали: {user_choice}\nКомпьютер выбрал: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Результат: {result}")

window = tk.Tk()
window.title("Камень, Ножницы, Бумага")

user_choice_var = tk.StringVar()

user_choice_label = tk.Label(window, text="Выберите: камень, ножницы или бумага?")
user_choice_label.pack()

choices = ['камень', 'ножницы', 'бумага']

for choice in choices:
    choice_radio = tk.Radiobutton(window, text=choice, variable=user_choice_var, value=choice)
    choice_radio.pack()

play_button = tk.Button(window, text="Играть", command=play_game)
play_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()