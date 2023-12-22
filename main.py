"""
BlackJack Game; Betting allowed
By Akshaj
"""
import random

suits=("Clubs","Diamonds","Hearts","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,
        "Queen":10,"King":10,"Ace":11}

total_money=int(input("How much money would like to play with today?\nYour answer: "))
money_play=total_money

game_on= True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_contains=""
        for card in self.deck:
            deck_contains+="\n"+card.__str__()
        return "Deck has: "+deck_contains
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        dealt_card=self.deck.pop()
        return dealt_card

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=="Ace":
            self.aces+=1

    def ace_value_dec(self):
        while self.value>21 and self.aces>=1:
            self.value-=10
            self.aces-=1

class Betting:
    def __init__(self):
        global money_play
        self.total=money_play
        self.bet=0
    def bet_win(self):
        self.total+=self.bet
    def bet_lose(self):
        self.total-=self.bet

def bet(amt):
    while True:
        try:
            amt.bet=int(input("Enter betting amount: "))
        except ValueError:
            print("Sorry, please enter an integer")
        else:
            if amt.bet>amt.total:
                print("Sorry your bet cannot exceed ",amt.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.ace_value_dec()

def hit_stand(deck,hand):
    global game_on
    while game_on:
        move=input("Hit or Stand?\n(Hit/hit/h/H/Stand/stand/s/S)\nYour answer: ")
        if move[0].lower()=="h":
            hit(deck,hand)
        elif move[0].lower()=="s":
            print("Standing. Dealer's play.")
            game_on=False
        else:
            print("Please Try Again!")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_win(player,dealer,amt):
    print("Player Wins!")
    amt.bet_win()

def player_lose(player,dealer,amt):
    print("Player Busts!")
    amt.bet_lose()

def dealer_win(player,dealer,amt):
    print("Dealer Wins!")
    amt.bet_lose()

def dealer_lose(player,dealer,amt):
    print("Dealer Busts!")
    amt.bet_win()

def push(player,dealer):
    print("Tie! Its a push.")

def main():
    global game_on
    while True:
        print("Welcome to Blackjack. Get as close as you can to 21 without going over. Dealer hits",
              "until 17. Aces: 1/11")
        deck=Deck()
        deck.shuffle()

        player_hand=Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand=Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_money=Betting()
        bet(player_money)

        show_some(player_hand,dealer_hand)

        while game_on:
            hit_stand(deck,player_hand)
            show_some(player_hand,dealer_hand)
            if player_hand.value>21:
                player_lose(player_hand,dealer_hand,player_money)
                break
        if player_hand.value<=21:

            while dealer_hand.value<17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value>21:
                dealer_lose(player_hand,dealer_hand,player_money)

            elif dealer_hand.value>player_hand.value:
                dealer_win(player_hand,dealer_hand,player_money)

            elif player_hand.value>dealer_hand.value:
                player_win(player_hand,dealer_hand,player_money)

            else:
                push(player_hand,dealer_hand)

            print("Players winnings are: ",player_money.total)

            new_game=input("Would you like to play again?\n(Yes/yes/y/Y/No/no/n/N)\nYour answer: ")
            if new_game[0].lower()=="y":
                game_on=True
                continue
            else:
                print("Thank you for playing!")
                break
main()