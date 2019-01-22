from deck import SuperDeck, render_cards, render_card
from player import Player

sd = SuperDeck(2)

sd.shuffle()


def deal(num_cards):
    return [sd.draw() for i in range(0, num_cards)]


game_index = 0
num_players = 3
cards_per_player = 14

players = [
    Player(
        deal(
            cards_per_player + 1 if i is 0 else cards_per_player
        ),
        sd,
    ) for i in range(0, num_players)
]


def initial_deal():
    for index, player in enumerate(players):
        print(f'- Player {index + 1} -')
        print(render_cards(player.show_cards(), 6))
        print('----------------------')


def game_round():
    for index, player in enumerate(players):
        player_name = f'Player {index + 1}'
        player_input = input(f'Choose your action, {player_name}: ')
        p_inp = player_input.upper()

        if p_inp == 'D':
            print(f'Player {index + 1} drew a card:')
            print(render_card(player.draw()))
        elif p_inp == 'E':
            return False

        print('------------------')
    return True


initial_deal()
while True:
    if game_round() is False:
        break

