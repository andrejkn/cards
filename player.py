class Player:
    def __init__(self, cards, deck):
        self.cards = cards
        self.deck = deck

    def draw(self):
        return self.deck.draw()

    def show_cards(self):
        return self.cards
