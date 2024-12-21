def find_hidden_card(cards):
    
    same_suit_cards = {}
   
    
    for card in cards:
        value, suit = card.split('_')
        if suit not in same_suit_cards:
            same_suit_cards[suit] = []
        same_suit_cards[suit].append(value)
   
    
    for suit, values in same_suit_cards.items():
        if len(values) == 2:
            card1_value = int(values[0]) if values[0].isdigit() else values[0]
            card2_value = int(values[1]) if values[1].isdigit() else values[1]
           
            
            value_mapping = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
            card1_value = value_mapping.get(card1_value, card1_value)
            card2_value = value_mapping.get(card2_value, card2_value)
           
            
            distance = (card2_value - card1_value) % 13
           
            
            if 1 <= distance <= 6:
                hidden_card = f'{card1_value}_{suit}'
            else:
                hidden_card = f'{card2_value}_{suit}'
           
            return hidden_card
