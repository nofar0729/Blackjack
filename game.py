import random

suits = ("Hearts", "Diamonds", "Spades", 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        for card in self.deck:
            print(card)
        return ""

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.shuffle()
        return self.deck.pop()


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.aces = 0

    def add_cards(self,card):
        self.cards.append(card)
        self.score += card.value
        if card.rank == "ace":
            self.aces += 1

    def adjust_for_ace(self):
        ace = 0;
        while ace < self.aces:
            if self.score > 21:
                self.score -= 10
            if self.score-31 < self.score-21:
                self.score -= 10


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        return self.total



def take_bet():
    while True:
        try:
            bet = int(input("Please enter your bet"))
            if bet <= player_chips.total:
                print("You bet {} chips".format(bet))
                break
            else:
                print("Not enough chips to bet that amount!")
                continue
        except:
            print("wrong input, please try again.")
            continue


def hit(deck, hand):
    deck.shuffle()
    new_card = deck.deal()
    hand.add_cards(new_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    user_input = int(input("Do you want to hit or stand?"))
    if user_input == 1:
        hit(deck, hand)
    else:
        playing = False


def show_some(player, dealer):
    print("Players cards:")
    for cards in player_hand.cards:
        print(cards)
    print("Dealer's cards:")
    i = 1
    while i < len(dealer_hand.cards):
        print(dealer_hand.cards[i])
        i += 1


def show_all(player, dealer):
    print("Players cards:")
    for cards in player_hand.cards:
        print(cards)
    print("Dealer's cards:")
    i = 0
    while i < len(dealer_hand.cards) - 1:
        print(dealer_hand.cards[i])
        i += 1


def player_busts():
    print("Player Busts!")
    player_chips.lose_bet()
    playing = False


def player_wins():
    print("Player won!")
    player_chips.win_bet()


def dealer_busts():
    print("Dealer Busts!")


def dealer_wins():
    print("Dealer won!")


def push():
    print("The game ended with a tie")


while True:
    print("Welcome to the Black Jack Game, Lets get started!")
    # create and shuffle the deck:
    deck = Deck()
    deck.shuffle()

    # Deal two cards to each player:
    player_hand = Hand()
    dealer_hand = Hand()
    i = 0
    while i < 2:
        card1 = deck.deal()
        card2 = deck.deal()
        player_hand.add_cards(card1)
        dealer_hand.add_cards(card2)
        i += 1

    # Set up the player's chips:
    player_chips = Chips()

    # Prompt the player for their first bet:
    take_bet()

    # Show cards(but keep one dealer card hidden):
    show_some(player_hand, dealer_hand)

    # The main game loop:
    while playing:
        hit_or_stand(deck, player_hand)
        print("The current hands are:")
        show_some(player_hand, dealer_hand)
        if player_hand.score > 21:
            player_busts()
            break
        else:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)

    if player_hand.score <= 21:
        while dealer_hand.score <= 17:
            hit(deck, dealer_hand)
        if dealer_hand.score > 21:
            dealer_busts()

    if dealer_hand.score - 21 < player_hand.score - 21:
        dealer_wins()
    if player_hand.score - 21 < dealer_hand.score - 21:
        player_wins()
    if dealer_hand.score - 21 == player_hand.score - 21:
        push()
    print("The end")
    replay = int(input("Do you want to play again? (1- yes, 0- no)"))
    if replay == 0:
        break






