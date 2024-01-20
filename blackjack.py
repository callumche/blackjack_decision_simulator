import random
def main():
    while True: #0 A1  2  3  4  5  6  7  8  9  10
        cards = [0,24,24,24,24,24,24,24,24,24,96] #each number is at index, ace is at index 1 and not 11. 6 decks
        print("Hello and welcome to my Blackjack Decision Simulator")
        print("Enter your cards If you have an ace just enter an A.")
        user_total = user_input(input("How many cards do you have: "))
        print("Now enter the dealers first card shown")
        dealer_total = deal_input()
        if sum(user_total)<=11 or hit_decision(user_total,dealer_total,cards):
            print("Hit")
        else:
            print("Stand")
        if input("Press X to stop looping ") == 'X':
            break
        print()

def hit_decision(user,dealer,cards):
    change_cards(user,dealer,cards)
    dealer_results = dealer_prob(dealer,cards)
    stand_prob = winning_prob(user,dealer_results)
    hit_prob = 0
    for i in range(10000):
        new_user = user[:]
        new_user.append(hit(cards))
        hit_prob += winning_prob(new_user,dealer_results)
    hit_prob /= 10000
    if hit_prob>stand_prob:
        return True
    else:
        return False
        
def winning_prob(user,d_results):
    u_sum = sum(user)
    if u_sum > 21:
        return 0
    winning_scenarios = d_results[5]
    for i in range(len(d_results)-1):
        if u_sum >= i+17:
            winning_scenarios += d_results[i]
    return winning_scenarios

def dealer_prob(dealer,cards):#hit 16 stand 17
    initial_dealer_sum = sum(dealer)
    dealer_sum = sum(dealer)
    results = [0,0,0,0,0,0] #index 0 is 17, 1 is 18, 2 is 19, 3 is 20, 4 is 21, 5 is bust
    for turns in range(10000):
        new_cards = cards[:]
        dealer_sum = initial_dealer_sum
        while dealer_sum < 17:
            #print(dealer_sum)
            dealer_sum += hit(new_cards)
            update_cards(dealer,new_cards)
        for i in range(17,22):
            if dealer_sum>21:
                results[5] += 1
                break
            else:
                if dealer_sum == i:
                    results[i-17] += 1
    return results


def hit(cards):
    undrawn_cards = sum(cards)
    num = random.randint(1,undrawn_cards)
    i = len(cards)-1
    while True:
        if (undrawn_cards - cards[i]) > num:
            undrawn_cards -= cards[i]
        else:
            return i
        i-=1


def change_cards(user, dealer, cards):
    for i in range(len(user)): 
        if user[i] == 'A':
            cards[1] -= 1
        else:
            cards[int(user[i])] -= 1
    for j in range(len(dealer)):
        if dealer[j] == 'A':
            cards[1] -= 1
        else:
            cards[int(dealer[j])] -= 1

def update_cards(dealer, cards):
    for j in range(len(dealer)):
        if dealer[j] == 'A':
            cards[1] -= 1
        else:
            cards[int(dealer[j])] -= 1

def user_input(num_of_cards):
    user_initial_total = []
    for i in range(int(num_of_cards)):
        user_initial_total.append(input("Enter Card #"+str(i+1)+": "))
    return user_initial_total
    
def deal_input():
    dealer_card = input("Insert dealer card here: ")
    return dealer_card

def sum(a): 
    sum = 0
    a_count = 0
    for i in range(len(a)):
        if a[i] == 'A':
            a_count +=1
        else:
            sum += int(a[i])
    for j in range(a_count):
        if sum < 11:
            sum+=11
        else:
            sum+=1
    return sum

if __name__ == "__main__":
    main()

