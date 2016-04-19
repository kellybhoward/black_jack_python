#####################
# Black Jack        #
#####################
"""
What you need:
- 52 Playing Cards
- Dealer
- Player

Rules of the game:
- Aces are high and low
- No Double Down - Keep it Simple
- Dealer hits until 17+ => if 17 is soft (ace + 6), dealer hits
- No betting for now


Flow of game:
- Deck is shuffled
- Cards are dealt
- Player sees 1 of dealer's cards
- Player Chooses:
1) stay -> goes to dealer's turn
2) hit -> if not bust: Player Chooses:
                        1) stay -> goes to dealer's turn
                        2) hit -> etc
- if Dealer has hard 17 - Dealer stays check for winner
    else: hit-> until bust or H17

End of game scenarios:
- Either player is bust
- Both player's are bust
- Both stay, compare points

"""
