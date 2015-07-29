__author__ = 'luke'
import random
master_deck = []

class game():
    player1_deck = []
    player2_deck = []
    player1_discard = []
    player2_discard = []
    player1_hand = []
    player2_hand = []

    def build_deck(self):
        deck = []
        for suit in range (1,5):
            for i in range(1,14):
                deck.append(i)
        return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    print deck
    return deck

def deal_all_cards(deck):
    player1_deck = []
    player2_deck = []
    has_player_one_been_delt = 0
    deal_from = deck
    for card in deal_from:
        if not has_player_one_been_delt:
            player1_deck.append(card)
            has_player_one_been_delt = 1
            print "player 1" + str(player1_deck)
        else:
            player2_deck.append(card)
            has_player_one_been_delt = 0
            print "player 2" + str(player2_deck)
    return [player1_deck,player2_deck]

def playhand(game_state):
    player1_deck = game_state[0]
    player2_deck = game_state[1]
    player1_card = player1_deck.pop()
    player2_card = player2_deck.pop()
    if player2_card > player1_card:
        player2_deck.insert(0,player1_card)
        player2_deck.insert(0,player2_card)
    elif player2_card < player1_card:
        player1_deck.insert(0,player1_card)
        player1_deck.insert(0,player2_card)
    else:
        print "WAR WAR "+ str(player1_card)+ " VS " + str(player2_card)


    print "+++++++++++++++++++++++++++++++++++"
    print "player 1 deck "+ str(player1_deck)
    print "player 2 deck "+ str(player2_deck)
    return [player1_deck,player2_deck]


deck = build_deck()
deck = shuffle_deck(deck)
game_state = deal_all_cards(deck)
game_state = playhand(game_state)

for i in range (100):
    if not (len(game_state[0])) == 0:
        game_state = playhand(game_state)
        print "this is turn " + str(i)



player1_deck = game_state[0]
player2_deck = game_state[1]



