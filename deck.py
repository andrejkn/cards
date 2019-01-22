# -*- coding: utf-8 -*-

from collections import namedtuple
from random import shuffle
from functools import reduce

Card = namedtuple('Card', ['rank', 'suit'])

Suit = namedtuple('Suit', ['name', 'symbol'])

ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')

suits = [
    Suit('spades', '♤'),
    Suit('diamonds', '♢'),
    Suit('clubs', '♧'),
    Suit('hearts', '♡'),
]

CARD_HEIGHT = 7
CARD_WIDTH = 10


def create_deck():
    return [Card(rank, suit) for rank in ranks for suit in suits]


def render_card_row(i: int, row: str, card: Card):
    new_row = row[:2] + card.rank + row[2+len(card.rank):] if i is 0 else \
        row[:2] + card.suit.symbol + row[3:] if i is 1 else \
        row[:len(row) - 4] + card.suit.symbol + row[len(row) - 3:] if i is CARD_HEIGHT - 4 else \
        row[:len(row) - 3] + card.rank + row[len(row) - 3 + len(card.rank):] if i is CARD_HEIGHT - 3 else \
        row
    return new_row


def render_card_rows(card: Card):
    frame_length = CARD_WIDTH
    card_height = CARD_HEIGHT
    horizontal_middle = ('═' * (frame_length - 2))
    horizontal_top = '╔' + horizontal_middle + '╗'
    horizontal_bottom = '╚' + horizontal_middle + '╝'

    row = '║' + ((frame_length - 2) * ' ') + '║'

    rows = [render_card_row(i, row, card) for i in range(0, card_height - 2)]
    return [
        horizontal_top,
        *rows,
        horizontal_bottom,
    ]


def array_2d_to_str(arr, num_cols):
    arr_str = ''
    for row_index in range(0, CARD_HEIGHT):
        row_arr = [arr[col_index][row_index] for col_index in range(0, num_cols)]
        row_str = ''.join(row_arr)
        arr_str += row_str + '\n'

    return arr_str


def render_cards(cards: [Card], cards_per_row: int = 3):
    rend_str = ''

    cards_rows = [render_card_rows(card) for card in cards]

    for i in range(0, len(cards_rows), cards_per_row):
        start = i + cards_per_row
        end = cards_per_row if start < len(cards) else (len(cards) % cards_per_row)
        rend_str += array_2d_to_str(cards_rows[i:start], end)

    return rend_str


def render_card(card):
    return render_cards([card])


# SuperDeck is a set of one or more decks
# it contains a number of cards which is a multiple of 52
class SuperDeck:
    def __init__(self, num_decks):
        decks = [create_deck() for i in range(0, num_decks)]
        self.cards = reduce(lambda d1, d2: d1 + d2, decks)

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def __repr__(self):
        return render_cards(self.cards)

    def __len__(self):
        return len(self.cards)
