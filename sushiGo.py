#!/usr/bin/env python3

# 108 cards in a standard deck

from numpy.random import choice

class Game:
    
    players = 0
    rounds = 0
    #TODO refactor the instances variable.
    deck = {
        'tempura': 14,
        'dumpling': 14,
        'maki3': 8,
        'maki2': 12,
        'maki1': 6,
        'sal_nigiri': 10,
        'squ_nigiri': 5,
        'egg_nigiri': 5,
        'pudding': 10,
        'wasabi': 6,
        'chopsticks': 4
    }
    
    hand1 = {
        'tempura': 0,
        'dumpling': 0,
        'maki3': 0,
        'maki2': 0,
        'maki1': 0,
        'sal_nigiri': 0,
        'squ_nigiri': 0,
        'egg_nigiri': 0,
        'pudding': 0,
        'wasabi': 0,
        'chopsticks': 0
    }

    hand2 = {
        'tempura': 0,
        'dumpling': 0,
        'maki3': 0,
        'maki2': 0,
        'maki1': 0,
        'sal_nigiri': 0,
        'squ_nigiri': 0,
        'egg_nigiri': 0,
        'pudding': 0,
        'wasabi': 0,
        'chopsticks': 0
    }
    
    hand3 = {
        'tempura': 0,
        'dumpling': 0,
        'maki3': 0,
        'maki2': 0,
        'maki1': 0,
        'sal_nigiri': 0,
        'squ_nigiri': 0,
        'egg_nigiri': 0,
        'pudding': 0,
        'wasabi': 0,
        'chopsticks': 0
    }
    
    def __init__(self, players, rounds):
        self.players = players
        self.rounds = rounds
        self.hand1 = self.draw_card(players)
        self.hand2 = self.draw_card(players)
        self.hand3 = self.draw_card(players)
    
    def __str__(self):
    
        format_str = 'DECK: {0}\nH1: {1}\nH2: {2}\nH3: {3}'
        return format_str.format(self.deck, self.hand1, self.hand2, self.hand3)

        
    def draw_card(self, players):
        
        card_num = 12 - players  #Just a arbitary rule
        card_list = []
        deck_list = self.expand_dict(self.deck)

        hand = {
            'tempura': 0,
            'dumpling': 0,
            'maki3': 0,
            'maki2': 0,
            'maki1': 0,
            'sal_nigiri': 0,
            'squ_nigiri': 0,
            'egg_nigiri': 0,
            'pudding': 0,
            'wasabi': 0,
            'chopsticks': 0
        }
        
        card_list = choice(deck_list, card_num, replace=False)
        
        for card in card_list:
            hand[card] += 1
            self.deck[card] -= 1

        return hand

        
    def expand_dict(self, deck):
        expanded = []
        for card, count in deck.items():
            expanded.extend([card]*count)

        return expanded


    # TODO
    # deal hands to players
    # 10 each in 2-player
    # 9 each in 3-player
    # 8 each in 4-player
    # 7 each in 5-player



class Card:

    def __init__(self, name, card_num):
        self.name = name
        self.card_num = card_num

    # number of cards this type have
    def get_card_number(self):
        return self.card_num






