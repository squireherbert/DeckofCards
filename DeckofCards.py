import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        if num_cards <= len(self.deck):
            dealt_cards = self.deck[:num_cards]
            self.deck = self.deck[num_cards:]
            return dealt_cards
        else:
            return None

    def count(self):
        return len(self.deck)

def main():
    print("Card Dealer")
    print("I have shuffled a deck of 52 cards.")

    deck = Deck()
    deck.shuffle()

    num_cards = int(input("How many cards would you like? "))
    dealt_cards = deck.deal(num_cards)

    if dealt_cards:
        print("Good luck!")
        print("Dealt cards:")
        for card in dealt_cards:
            print(f"{card.rank} of {card.suit}")
        
        remaining_cards = deck.count()
        print(f"Remaining cards in the deck: {remaining_cards}")
    else:
        print("Not enough cards in the deck.")

if __name__ == "__main__":
    main()
