import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count={
    "A" : 3,
    "B" : 7,
    "C" : 5,
    "D" : 6
}

symbol_value={
    "A" : 10,
    "B" : 4,
    "C" : 7,
    "D" : 8
}

#get deposit from user
def get_deposit():
    while True:

        deposit_amount = input("How much amount would you like to deposit? $")

        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                break
            else:
                print("Deposit must be greater than 10$.")
        else:
            print("Please enter a number.")

    return deposit_amount

#get number of lines to bet on
def get_no_of_lines():
    while True:

        no_of_lines = input(f"Enter number of lines to bet on (1- {MAX_LINES}):")

        if no_of_lines.isdigit():
            no_of_lines = int(no_of_lines)
            if 1 <= no_of_lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return no_of_lines

#get bet amount for each line
def get_bet():
    while True:

        bet_amount = input("How much would you like to bet on each line? $")

        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet must lie between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")

    return bet_amount

#get spin results
def spin_slot_machine(rows, cols, symbols):
    all_symbols = []

    #extract all symbols from the symbols dictionary argument
    for symbol, symbol_count in symbols.items():
         for _ in range(symbol_count):
             all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

#print results
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


#check if user won
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines


#spin the slot machine
def spin(balance):
    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough funds to bet that amount. Your current balance = ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")

    slots = spin_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = get_deposit()
    while True:
        print(f"Current balance = ${balance}")
        answer = input("Press enter to play(q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

if __name__=="__main__":
    main()  