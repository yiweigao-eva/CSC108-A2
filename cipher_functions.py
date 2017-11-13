# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.


def clean_message(message):
    """(str) -> str
    
    Return message, converted to all caps and without whitespace.
    
    >>>clean_message('caesar salad')
    'CAESARSALAD'
    """
    
    copy_message = ''
    
    for char in message:
        if char.isalpha() == True:
            copy_message = copy_message + char
            
    
    return copy_message.upper()
    
def encrypt_letter(letter, keystream):
    """(str, int) -> str
    
    Precondition: len(letter) = 1
    
    Return the letter encrypted by applying the keystream
    
    >>>encrypt_letter('D', 34)
    'L'
    """
    ord_diff = ord(letter) - ord('A')
    
    new_char_ord = (keystream + ord_diff) % 26
    
    return chr(new_char_ord + ord('A'))

def decrypt_letter(letter, keystream):
    """(srt, int) -> str
    
    Return the letter decrypted by applying the keystream
    
    >>>decrypt_letter('L', 34)
    'D'
    """
    
    ord_diff = ord(letter) - ord('A')
    
    new_char_ord = (ord_diff - keystream) % 26
    
    return chr(new_char_ord + ord('A'))
        
def swap_cards(deck, index):
    """(list of int, int) -> NoneType
    
    Swap the card in deck at index with the card underneath it. Deck is circular
    
    >>>swap_cards([1, 3, 4, 2, 5], 1)
    >>>return deck
    [1, 4, 3, 2, 5]
    """
    i = index % len(deck)
    hold = deck[(i + 1) % len(deck)]
    
    deck[(i + 1) % len(deck)] = deck[i]
    deck[i] = hold

    
def get_small_joker_value(deck):
    """(list of int) -> int
    
    Return the value of the second highest card in the given deck
    
    >>>get_small_joker_value([1, 2, 3, 4, 5,])
    4
    """
    
    return len(deck) - 1
    
def get_big_joker_value(deck):
    """(list of int) -> int
    
    Return the value of the highest card in the given deck
    
    >>>get_big_joker_value([1, 2, 3, 4, 5])
    5
    """
    
    return len(deck)

def move_small_joker(deck):
    """(list of int) -> NoneType
    
    Move the small joker one card down in the deck. Deck is circular.
    
    >>>move_small_joker([1, 2, 3, 4, 5])
    >>>return deck
    [1, 2, 3, 5, 4]
    """
    small_joker_index = deck.index(get_small_joker_value(deck))
    
    swap_cards(deck, small_joker_index)

def move_big_joker(deck):
    """(list of int) -> NoneType
    
    Move the big joker two cards down in the deck. Deck is circular.
    
    >>>move_big_joker([1, 2, 3, 4, 5])
    >>>return deck
    [2, 5, 3, 4, 1]
    >>>move_big_joker([2, 4, 3, 1])
    >>>return deck
    [2, 3, 1, 4]
    >>>move_big_joker([1, 2, 4, 3])
    >>>return deck
    [4, 2, 3, 1]
    """
    
    big_joker_index = deck.index(get_big_joker_value(deck))
    
    swap_cards(deck, big_joker_index)
    
    big_joker_index = (big_joker_index + 1) % len(deck)
    
    swap_cards(deck, (big_joker_index))
    
    
def triple_cut(deck):
    """(list of int) -> NoneType
    
    Do a triple cut on the deck
    
    >>>triple_cut([1, 2, 8, 4, 5, 6, 9, 7, 3])
    >>>return deck
    [7, 3, 8, 4, 5, 6, 9, 1, 2]
    >>>triple_cut([8, 1, 2, 3, 4, 9, 5, 6, 7])
    >>>return deck
    [5, 6, 7, 8, 1, 2, 3, 4, 9]
    >>>triple_cut([1, 2, 3, 9, 8, 7, 6, 5, 4])
    >>>return deck
    [7, 6, 5, 4, 9, 8, 1, 2, 3]
    """
    big_joker_index = deck.index(get_big_joker_value(deck))
    small_joker_index = deck.index(get_small_joker_value(deck))
    
    first_joker_index = min(big_joker_index, small_joker_index)
    second_joker_index = max(big_joker_index, small_joker_index)
   
    # slice at index of first joker (1)
    up_to_first = deck[:first_joker_index]  
    
    # slice at index + 1 of second joker (2)
    after_second = deck[((second_joker_index + 1) % len(deck)):]  
    
    # create middle slice (cards between jokers) (3)
    
    up_to_second = deck[:(second_joker_index + 1)]
    
    middle_slice = up_to_second[first_joker_index:]  
    
    # extend (2) - (3) - (1) 
    

    deck = []
    deck.extend(after_second)
    deck.extend(middle_slice)
    deck.extend(up_to_first)
    
def insert_top_to_bottom(deck):
    """(list of int) -> NoneType
    
    Moves the value of the last card in deck number of cards to the bottom of 
    the deck, above the last card. If the last card is the big joker, use the 
    value of the small joker instead.
    
    >>>insert_top_to_bottom([1, 2, 3, 5, 6, 7, 4])
    >>>return deck
    [6, 7, 1, 2, 3 5, 4]
    >>>insert_top_to_bottom([1, 2, 3, 4, 5, 6, 7])
    >>>return deck
    [1, 2, 3, 4, 5, 6, 7]  
    
    """
    
    #find last card value
    
    last_card_value = deck[-1]
    
    if len(deck) == last_card_value:
        last_card_value = last_card_value - 1
    
    #find first [last value]
    
    top_x = deck[:last_card_value]
   
    
    bottom_pile_size = len(deck) - len(top_x)
    
    #pop out first x
 
    while len(deck) > (bottom_pile_size):
        deck.pop(0)
    
    
    #insert first x before last index
    
    last_card = []
    last_card.append(deck[-1])
    
    deck.pop(-1)  
    deck.extend(top_x)
    deck.extend(last_card)
     
def get_card_at_top_index(deck):
    """(list of int) -> int
    
    Return the card at index of value of the top card in the deck. 
    If the first card is the big joker, use the value of the small joker. 
    
    >>>get_card_at_top_index([1, 2, 3])
    2
    >>>get_card_at_top_index([4, 3, 2, 1])
    1
    """
    
    #get value of top card
    top_card_value = deck[0]
    #special case
    if top_card_value == get_big_joker_value(deck):
        top_card_value = top_card_value - 1
    
    return deck[top_card_value]

def get_next_keystream_value(deck):
    """(list of int) -> int
    
    Return a keystream generated from deck
    
    >>>get_next_keystream_value([1, 2, 3, 4])
    1243
    4231
    4231
    2341
    4
    >>>get_next_keystream_value([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    """
    move_small_joker(deck)
    
    move_big_joker(deck)
    
    triple_cut(deck)
    
    insert_top_to_bottom(deck)
    
    get_card_at_top_index(deck)
    
    return get_card_at_top_index(deck)

    
def process_messages(deck, messages, direction):
    """(list of int, list of str, str) -> list of str
    
    Precondition: direction must be either ENCRYPT or DECRYPT
    
    Return a list of either encrypted or decrypted messages, in the order they 
    appear in messages
    
    >>>process_messages([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], ['A real message', 
    'ALL CAPS', 'NOSPACES', '     whitespace     ', '345678'], 'ENCRYPT')
    ['LTWGRKSAQPMT', 'MFXIMBD', 'OXVATVLB', 'COUILEEHCE', '']
    >>>process_messages([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], ['LTWGRKSAQPMT', 
    'MFXIMBD', 'OXVATVLB', 'COUILEEHCE'], 'DECRYPT')
    ['AREALMESSAGE', 'ALLCAPS', 'NOSPACES' 'WHITESPACE']
    """
    #the constant can not be a string
    if direction == ENCRYPT:
        
        encrypted_list = []
        for message in messages:
        
            encrypted_message = ''
            for letter in clean_message(message):
                encrypted_letter = encrypt_letter(letter, 
                                                  get_next_keystream_value(deck))
        
                encrypted_message += encrypted_letter    
            encrypted_list.append(encrypted_message)
        return(encrypted_list)
    
    if direction == DECRYPT:
        
        decrypted_list = []
        for message in messages:
            
            decrypted_message = ''
            for letter in message:
                decrypted_letter = decrypt_letter(letter, get_next_keystream_value(deck))
                
                decrypted_message += decrypted_letter
            decrypted_list.append(decrypted_message)
        return(decrypted_list)
    
    
def read_messages(file):
    """(file open for reading) -> list of str
    
    Read and Return the contents of the file as a list of messages.
    """
    
    list_of_message = []
    
    contents = file.readlines()
    
    for lines in contents: #wrong varible name
        
        list_of_message.append(lines.strip()) #missing () after line.strip
    
    return list_of_message
    
    
def is_valid_deck(deck):
    """(list of int) -> bool
    
    Return True iff the candidate deck contains every integer from 1 up to the number of cards in the deck
    
    >>>is_valid_deck([1, 2, 3 ,4])
    True
    >>>is_valid_deck([1, 2, 3, 5, 6])
    False
    >>>is_valid_deck([1, 2, 3, 4, 9])
    False
    >>>is_valid_deck([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    True
    """
    
    i = 0
    
    while i < len(deck):
        
        i = i + 1
        
        if i not in deck:
            
            return False
    
    return True
                
        
        
def read_deck(current_deck_file):
    """(file open for reading)-> list of int
    
    Read and return the deck that is stored in current_deck_file
    """
    
    return_list = []
    
    deck_lines = current_deck_file.readlines()
    
    deck_list_of_str = []
        
        #strip deck of \n characters
    for line in deck_lines:
        stripped_line = line.strip()
            
        line_list_of_str = stripped_line.split()
        deck_list_of_str.extend(line_list_of_str)    
    
    for card in deck_list_of_str:
        card_value = int(card)
        return_list.append(card_value)
    
    return return_list
        
