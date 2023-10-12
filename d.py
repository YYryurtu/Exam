
import random

suits = ['♥', '♦', '♠', '♣']
ranks = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
deck = []

for suit in suits:
    for rank in ranks:
        deck.append({'rank': rank, 'suit': suit})

random.shuffle(deck)

player_hand = deck[:6]
computer_hand = deck[6:12]
deck = deck[12:]

trump_suit = random.choice(suits)
print(f"Козырь: {trump_suit}")

print('Ваша рука:')
for card in player_hand:
    print(f"{card['rank']} {card['suit']}")

while True:
    player_choice = input(
        "Выберите карту для хода (напишите номер карты от 1 до 6) или 'подкинуть' для подкидывания карт: ")
    if player_choice.lower() == 'подкинуть':
        pass
    else:
        try:
            player_choice = int(player_choice) - 1
            if 0 <= player_choice < len(player_hand):
                played_card = player_hand.pop(player_choice)
                print(f"Вы сыграли {played_card['rank']} {played_card['suit']}")
            else:
                print("Некорректный выбор карты. Попробуйте снова.")
                continue
        except ValueError:
            print("Введите число от 1 до 6.")
            continue

    if computer_hand:
        valid_cards = [card for card in computer_hand if
                       card['suit'] == played_card['suit'] and ranks.index(card['rank']) > ranks.index(
                           played_card['rank'])]
        if valid_cards:
            computer_card = max(valid_cards, key=lambda x: ranks.index(x['rank']))
            print(f"Компьютер сыграл {computer_card['rank']} {computer_card['suit']}")
        else:
            print("Компьютер принял вашу карту.")
            computer_hand.append(played_card)
            computer_card = played_card
    else:
        print("Компьютер не может сыграть карту, он взял карту из колоды.")
        computer_card = deck.pop(0)
        computer_hand.append(computer_card)


    if played_card['suit'] == trump_suit and computer_card['suit'] != trump_suit:
        print("Вы победили! Сыгранная вами карта - козырь.")
    elif computer_card['suit'] == trump_suit and played_card['suit'] != trump_suit:
        print("Компьютер победил. Его карта - козырь.")
    else:
        if ranks.index(played_card['rank']) > ranks.index(computer_card['rank']):
            print("Вы победили этот ход!")
        else:
            print("Компьютер победил этот ход.")

    if not player_hand:
        print("Вы победили! У вас больше нет карт в руке.")
        break
    if not computer_hand:
        print("Компьютер победил. У него больше нет карт в руке.")
        break