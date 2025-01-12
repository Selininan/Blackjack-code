import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
card_values = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

print("Welcome to Blackjack!")

players = []
num_players = int(input("Enter the number of players: "))
for i in range(num_players):
    name = input(f"Enter the name for Player {i + 1}: ")
    balance = int(input(f"Enter the starting balance for {name}: "))
    players.append({'name': name, 'balance': balance})

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(card_values[card] if card in card_values else int(card) for card in hand)
    if score == 21 and len(hand) == 2:
        return "Blackjack"
    if "A" in hand and score + 10 <= 21:
        return score + 10
    return score

def compare_scores(user_score, computer_score):
    if user_score == 'Blackjack' or computer_score == 'Blackjack':
        if user_score == computer_score:
            return "It's a draw!"
        elif user_score == 'Blackjack':
            return "You win!"
        else:
            return "You lose!"
    if user_score > 21:
        return "You lose!"
    if computer_score > 21:
        return "You win!"
    if user_score > computer_score:
        return "You win!"
    return "You lose!"

def blackjack():
    game_over = False
    while not game_over:
        for player in players:
            print(f"\n{player['name']}'s turn. Current balance: ${player['balance']}")
            bet = int(input("Enter your bet: "))
            while bet > player['balance'] or bet <= 0:
                print("Invalid bet. Bet must be greater than 0 and not exceed your balance.")
                bet = int(input("Enter your bet: "))

            user_hand = [deal_card(), deal_card()]
            computer_hand = [deal_card()]

            while True:
                user_score = calculate_score(user_hand)
                computer_score = calculate_score(computer_hand)

                print(f"\n{player['name']}'s cards: {user_hand}, current score: {user_score}")
                print(f"Computer's first card: {computer_hand[0]}")

                if user_score == 'Blackjack' or computer_score == 'Blackjack':
                    break

                action = input("Type 'h' to get another card, 's' to stand: ")
                if action == 'h':
                    user_hand.append(deal_card())
                else:
                    break

            while computer_score != 'Blackjack' and computer_score < 17:
                computer_hand.append(deal_card())
                computer_score = calculate_score(computer_hand)

            print(f"\n{player['name']}'s final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

            result = compare_scores(user_score, computer_score)
            print(result)

            if result == 'You win!':
                player['balance'] += bet
            elif result == 'You lose!':
                player['balance'] -= bet

            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                game_over = True

    # Display the winner and current balance for each player
    for player in players:
        print(f"{player['name']} has a final balance of ${player['balance']}.")
        if player['balance'] <= 0:
            print(f"{player['name']} has run out of money. Better luck next time!")

    # Determine and display the overall winner
    winner = max(players, key=lambda x: x['balance'])
    print(f"The winner is {winner['name']} with a balance of ${winner['balance']}!")

blackjack()




    
     
     
  
  
  


